# T-Code v4: Turkish Computer-Control Command Dataset

This repository contains the T-Code v4 dataset and experimental materials for token-level task labeling of Turkish computer-control commands.

## Overview

T-Code v4 is a Turkish natural-language computer-control command dataset. Each command is annotated with task segments, boundary labels, and task-token labels.

The final dataset contains 2700 command records across four balanced domains:

- `temel_bilgisayar`
- `tarayıcı_internet`
- `ofis_metin_düzenleme`
- `dosya_yazılım_geliştirme`

The task-token annotation schema contains 33 labels including `O`.

## Repository Structure

- `data/final`: Final 2700-record dataset
- `data/intermediate`: 1600 and 2500 development-stage datasets
- `data/challenge`: Human-written challenge test sets
- `data/augmentation`: Robustness-oriented augmentation data
- `data/labels`: Label mappings
- `scripts`: Data preparation, validation, training, and evaluation scripts
- `notebooks`: Exported Colab notebooks
- `results`: Evaluation outputs
- `llm_audit`: LLM-assisted consistency audit files
- `models`: Notes about model checkpoints
- `docs`: Additional documentation

## Main Experiments

The accompanying manuscript compares:

- BiLSTM-CRF
- mBERT
- XLM-RoBERTa-base
- BERTurk

Evaluation includes internal ID/batch holdout test, human-written challenge test, filtered challenge test, domain-wise analysis, task-count-wise analysis, and LLM-assisted consistency audit.

## Model Checkpoints

Large trained model checkpoints are not stored directly in this repository due to file-size limitations. If needed, they should be shared separately through GitHub Releases, Zenodo, OSF, or Hugging Face Hub.

## Citation

Please cite the accompanying manuscript if you use this dataset or code.
