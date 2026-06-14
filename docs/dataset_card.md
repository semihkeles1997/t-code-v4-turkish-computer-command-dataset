# T-Code v4 Dataset Card

T-Code v4 is a Turkish computer-control command dataset designed for token-level decomposition of compound user commands into executable subtasks.

## Dataset size

- Final dataset: 2700 records
- Domains: 4
- Task-token labels: 33 including `O`
- Boundary labels: 3

## Domains

- `temel_bilgisayar`
- `tarayıcı_internet`
- `ofis_metin_düzenleme`
- `dosya_yazılım_geliştirme`

## Main files

- `data/final/tcode_v4_2700.jsonl`
- `data/challenge/challenge_gold_100.jsonl`
- `data/challenge/challenge_filtered_99_no_neardup.jsonl`
