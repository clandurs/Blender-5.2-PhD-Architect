#!/usr/bin/env python3
"""Validate the Blender 5.2 PhD Architect skill repository.

Offline validation is deterministic and dependency-free. Pass --online to make
best-effort HTTP requests for every registered external source.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "blender-5-2-phd-architect"

KNOWLEDGE = [
    "modeling.md",
    "sculpting.md",
    "topology-retopology.md",
    "uv-texturing.md",
    "materials-shaders.md",
    "rigging.md",
    "animation.md",
    "geometry-nodes.md",
    "simulations.md",
    "lighting-camera.md",
    "cycles-eevee-rendering.md",
    "compositing-vfx.md",
    "grease-pencil.md",
    "python-scripting.md",
    "addons-tools.md",
    "optimization.md",
    "troubleshooting.md",
    "production-pipelines.md",
]

WORKFLOWS = [
    "character-production.md",
    "environment-production.md",
    "animation-production.md",
    "procedural-production.md",
    "cinematic-production.md",
    "debugging-playbook.md",
]

REFERENCE_FILES = [
    "official-blender.md",
    "academic-sources.md",
    "production-pipeline-sources.md",
]

REQUIRED = [
    "SKILL.md",
    "README.md",
    "CONTRIBUTING.md",
    "agents/openai.yaml",
    *(f"knowledge/{name}" for name in KNOWLEDGE),
    *(f"workflows/{name}" for name in WORKFLOWS),
    *(f"references/{name}" for name in REFERENCE_FILES),
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://[^\s)>]+")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME|CHANGEME)\b|\[TODO", re.I)


def normalize_url(url: str) -> str:
    url = url.strip().strip("<>").rstrip(".,;")
    parsed = urllib.parse.urlsplit(url)
    path = re.sub(r"/{2,}", "/", parsed.path)
    if path != "/":
        path = path.rstrip("/")
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, "")
    )


def markdown_links(text: str) -> list[str]:
    links: list[str] = []
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        # Markdown may include an optional quoted title after the URL.
        target = re.split(r'\s+["\']', target, maxsplit=1)[0]
        links.append(target)
    return links


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_skill(errors: list[str]) -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not frontmatter:
        errors.append("SKILL.md has no valid YAML frontmatter block")
        return
    block = frontmatter.group(1)
    name_match = re.search(r"^name:\s*([^\n]+)$", block, re.M)
    description_match = re.search(r"^description:\s*(.+)$", block, re.M)
    if not name_match:
        errors.append("SKILL.md frontmatter has no name")
    else:
        name = name_match.group(1).strip().strip('"\'')
        if name != SKILL_NAME:
            errors.append(f"skill name is {name!r}, expected {SKILL_NAME!r}")
        if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
            errors.append("skill name must contain only lowercase letters, digits, hyphens")
        if ROOT.name != name:
            errors.append(f"skill directory {ROOT.name!r} does not match name {name!r}")
    if not description_match:
        errors.append("SKILL.md frontmatter has no description")
    else:
        description = description_match.group(1).strip().strip('"\'')
        if len(description) < 40:
            errors.append("skill description is too short to be discriminating")


def check_description(errors: list[str]) -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    match = re.search(r"\*\*GitHub description:\*\*\s*(.+)", text)
    if not match:
        errors.append("README.md does not declare a GitHub description")
        return
    description = match.group(1).strip()
    if len(description) >= 100:
        errors.append(
            f"GitHub description is {len(description)} characters; it must be under 100"
        )


def check_placeholders(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".py"}:
            if path.resolve() == Path(__file__).resolve():
                continue
            text = path.read_text(encoding="utf-8")
            if PLACEHOLDER_RE.search(text):
                errors.append(f"unfinished placeholder in {path.relative_to(ROOT)}")


def check_module_shape(errors: list[str]) -> None:
    for name in KNOWLEDGE:
        path = ROOT / "knowledge" / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "## Authoritative anchors" not in text:
            errors.append(f"knowledge/{name} lacks Authoritative anchors")
        if "Validation" not in text and "validation" not in text:
            errors.append(f"knowledge/{name} lacks validation guidance")


def check_links(errors: list[str]) -> set[str]:
    registry_urls: set[str] = set()
    for name in REFERENCE_FILES:
        path = ROOT / "references" / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "Verified:" not in text:
            errors.append(f"references/{name} lacks a verification date")
        registry_urls.update(normalize_url(url) for url in URL_RE.findall(text))

    cited_urls: set[str] = set()
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in markdown_links(text):
            parsed = urllib.parse.urlsplit(target)
            if parsed.scheme in {"http", "https"}:
                normalized = normalize_url(target)
                cited_urls.add(normalized)
                if normalized not in registry_urls:
                    errors.append(
                        f"external citation not in verified registry: "
                        f"{path.relative_to(ROOT)} -> {target}"
                    )
                continue
            if parsed.scheme or target.startswith("#"):
                continue
            relative = urllib.parse.unquote(parsed.path)
            if not relative:
                continue
            destination = (path.parent / relative).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"internal link escapes repository: {path.relative_to(ROOT)} -> {target}"
                )
                continue
            if not destination.exists():
                errors.append(
                    f"broken internal link: {path.relative_to(ROOT)} -> {target}"
                )

    uncited = registry_urls - cited_urls
    if not registry_urls:
        errors.append("verified source registry contains no external URLs")
    if uncited:
        # Registry-only entries are allowed; they are maintained authorities for future use.
        print(f"INFO: {len(uncited)} registered source(s) are not cited outside registries")
    return registry_urls


def fetch_url(url: str) -> tuple[str, str | None]:
    headers = {"User-Agent": "blender-5-2-phd-architect-link-validator/1.0"}
    request = urllib.request.Request(url, method="HEAD", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            if response.status >= 400:
                return url, f"HTTP {response.status}"
            return url, None
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405, 429}:
            return url, f"HTTP {exc.code}"
    except (urllib.error.URLError, TimeoutError) as exc:
        return url, str(exc)

    # Some documentation hosts reject HEAD. Read only a small prefix with GET.
    request = urllib.request.Request(
        url, method="GET", headers={**headers, "Range": "bytes=0-1023"}
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            response.read(1024)
            if response.status >= 400:
                return url, f"HTTP {response.status}"
            return url, None
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        return url, str(exc)


def check_online(urls: set[str], errors: list[str]) -> None:
    print(f"Checking {len(urls)} registered source URL(s) online...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(fetch_url, sorted(urls)))
    for url, problem in results:
        if problem:
            errors.append(f"online source check failed: {url} ({problem})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--online", action="store_true", help="perform best-effort live HTTP checks"
    )
    args = parser.parse_args()

    errors: list[str] = []
    check_required(errors)
    if (ROOT / "SKILL.md").is_file():
        check_skill(errors)
    if (ROOT / "README.md").is_file():
        check_description(errors)
    check_placeholders(errors)
    check_module_shape(errors)
    registry_urls = check_links(errors)
    if args.online and registry_urls:
        check_online(registry_urls, errors)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PASS: repository structure, frontmatter, description, placeholders, "
        "module shape, internal links, and citation registry are valid"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
