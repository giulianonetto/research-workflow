# Domain docs

One context: `GLOSSARY.md` and `docs/adr/` at the root. Both are created lazily, when the first term or decision is agreed. The glossary file is `GLOSSARY.md`: `/domain-modeling` (and `/grill-with-docs`, which loads it) calls it `CONTEXT.md`, but never create `CONTEXT.md` here.

Task-level choices are DECISION lines in the task's `PROGRESS.md` (format in `plans/README.md`); an ADR is only for the few that meet the rules below, and its DECISION line links to it.

Before exploring an area of the code, read `GLOSSARY.md` and the ADRs whose filenames match the area (`ls docs/adr/`). Use the glossary's terms in plans, code and commit messages. If a change contradicts an ADR, say so before going on.

## Glossary and ADRs

These rules override the `/domain-modeling` defaults.

- **Glossary: key terms only.** Propose a term and add it only once the user agrees. A term qualifies when all three hold:
  1. **Project-specific meaning:** we use it in a way a researcher in the field wouldn't assume, or we picked one of several competing definitions. Standard field terms stay out.
  2. **Costly if misread:** confusing it would silently change results.
  3. **Used across tasks:** it appears in more than one plan or module.

  Aim for about 10-15 entries in total.
- **ADRs: one paragraph, descriptive filename.** `docs/adr/NNNN-<slug>.md`, where the slug names the decision (`0003-fixed-cutoff-across-methods.md`), so an agent can pick the relevant ADRs from `ls docs/adr/` alone. Write one only when the decision is hard to reverse, surprising without context, and a real trade-off. ADRs hold the methodological choices a reviewer would question. A changed decision gets a new ADR that says which one it supersedes.
