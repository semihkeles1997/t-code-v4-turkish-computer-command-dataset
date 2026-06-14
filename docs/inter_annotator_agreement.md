# Inter-Annotator Agreement

To assess annotation reliability, a second independent annotator re-annotated a subset of 300 commands without access to the gold labels.

Agreement was calculated over 2,521 token-level decisions using Cohen's kappa. Boundary labels and task-token labels were evaluated separately.

## Results

| Layer | Tokens | Accuracy | Cohen's kappa |
|---|---:|---:|---:|
| Boundary labels | 2,521 | 0.9540 | 0.9234 |
| Task-token labels | 2,521 | 0.9429 | 0.9385 |

These results indicate a high level of agreement between annotators and support the consistency and reproducibility of the annotation scheme.

## Main boundary-label disagreements

| Gold | Second annotator | Count |
|---|---|---:|
| O | B-TASK | 35 |
| B-TASK | I-TASK | 33 |
| O | I-TASK | 27 |
| I-TASK | B-TASK | 8 |
| I-TASK | O | 7 |
| B-TASK | O | 6 |

## Main task-token disagreements

| Gold | Second annotator | Count |
|---|---|---:|
| O | AÇ | 17 |
| AÇ | YENİ_OLUŞTUR | 12 |
| O | BUL | 11 |
| O | ARA | 6 |
| GİT | DİĞER | 6 |
| GEÇ | GİT | 5 |
| YAZ | SEÇ | 5 |
| YÜKLE | TIKLA | 4 |
| TIKLA | DİĞER | 4 |
| AZALT | DEĞİŞTİR | 4 |

The disagreements mainly arise from boundary decisions around contextual expressions and from semantically close task labels such as GEÇ/GİT, AÇ/YENİ_OLUŞTUR, and DEĞİŞTİR/YENİDEN_ADLANDIR.
