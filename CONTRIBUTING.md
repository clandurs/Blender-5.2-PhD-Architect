# Contributing

Contributions should make the skill more accurate, discriminating, and testable without turning it into a copied manual or an opinionated studio rulebook.

## Before changing guidance

1. Identify whether the claim is **[5.2]**, **[Evergreen]**, **[Pipeline choice]**, **[Experimental]**, or **[Inference]**.
2. For Blender behavior, prefer a versioned 5.2 Manual or API page. Use release and compatibility notes for migrations and experimental features.
3. For algorithms and theory, cite a reputable university source. Do not use a university course page to prove a Blender UI or API detail.
4. For interchange or production infrastructure, prefer the governing specification or project documentation.
5. Reproduce the behavior when practical. Record exact Blender version, operating system, scene assumptions, and observable result.

## Writing standard

- Add decision criteria, failure signatures, or validation checks that change how an expert agent acts.
- Keep detailed topic guidance in `knowledge/` or `workflows/`; keep `SKILL.md` as the router and shared operating contract.
- Do not copy long passages from sources. Paraphrase, link, and preserve source meaning.
- Do not state “always” unless violating the rule creates a concrete, explained failure.
- State coordinate spaces, units, domains, ownership, evaluation order, and downstream consumer when relevant.
- Separate a Blender check from an exporter check and a consumer check.
- Do not convert a Blender Studio convention into a universal requirement.

## Adding or changing a source

Add the canonical URL to exactly one source registry:

- `references/official-blender.md`
- `references/academic-sources.md`
- `references/production-pipeline-sources.md`

Record verification date, authority, scope, and version status. Update every claim that depended on the old source. Avoid `latest` URLs when a 5.2 URL exists.

## Module template

Each knowledge module should contain:

1. Scope and version notes.
2. Decision framework.
3. Working method.
4. Validation gates.
5. Common failure signatures and discriminating tests.
6. Authoritative sources.

Workflows should define inputs, phased outputs, gates, and stop conditions rather than duplicating the knowledge modules.

## Validation

Run from the repository root:

```powershell
python scripts/validate_repository.py
```

Also test changed instructions on a minimal scene or fixture when the change affects actual Blender behavior. A text-only check cannot validate a render, simulation, export, or consumer result.

## Pull-request checklist

- [ ] No unfinished placeholders.
- [ ] New Blender claims are version-labeled and linked to a 5.2 authority.
- [ ] Experimental features include a fallback.
- [ ] Destructive actions preserve a rollback path.
- [ ] Validation evidence matches the claim being made.
- [ ] New external links are in a verified source registry.
- [ ] Repository validation passes.
- [ ] Public redistribution terms have been chosen by the repository owner.
