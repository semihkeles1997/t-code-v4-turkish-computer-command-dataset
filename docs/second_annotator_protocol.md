# Second Annotator Protocol

A second independent annotator re-annotates a blind subset of the dataset.

The annotator receives only:

- `id`
- `domain`
- `raw_command`
- `tokens`

The annotator must not see:

- `normalized_command`
- `task_segments`
- `task_labels`
- `boundary_labels`
- `task_token_labels`

Cohen's kappa is calculated separately for boundary labels and task-token labels.
