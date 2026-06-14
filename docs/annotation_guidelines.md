# Annotation Guidelines

## Core principle

Only actions that the user actually wants the system to execute should be annotated as task tokens.

Negated, cancelled, corrected, filler, and connector expressions should generally be labeled as `O`.

## Boundary labels

- `B-TASK`: beginning token of an executable task segment
- `I-TASK`: continuation token of the same executable task segment
- `O`: outside any executable task segment

## Important rules

1. Negated actions are not executable.
2. Fillers such as "hayır", "yanlış oldu", "şey", "sadece", "ama" are generally `O`.
3. Arguments that are part of an executable action receive the same task-token label.
4. Multiple executable actions in a command are annotated as separate segments.
5. Use `DİĞER` only for executable actions not covered by specific labels.

## Common confusions

- `GEÇ` vs. `GİT`
- `GEÇ` vs. `SEKME_DEĞİŞTİR`
- `DEĞİŞTİR` vs. `YENİDEN_ADLANDIR`
- `DİĞER` vs. specific task labels
