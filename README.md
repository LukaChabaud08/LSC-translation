# Neural Based Machine Translation from Catalan Sign Language glosses to written Catalan

This repository contains the augmentation and embedding scripts used for the training of a Neural Translation Network from Catalan Sign Language glosses to spoken catalan.

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)

## Description

This repository provides 3 main scripts:

- Data augmentation script: scripts that create synthetic data. See [synthesize_glosses.py](synthesize_glosses.py)
- Data preparation script: scripts that help preparing the data. See [extract_sentences.py](extract_sentences.py)
- Embeddings script: scripts to create word embedding models. See [embeddings.py](embeddings.py)

## Installation

You can install the project with the following commands:

```bash
# Example installation steps
git clone https://github.com/LukaChabaud08/LSC-translation.git
cd LSC-translation
pip install -r requirements.txt
```
