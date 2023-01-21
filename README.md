<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Spacy training project template.

This project is a template for spaCy training project. 

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `init` | init project |
| `preprocess` | Convert the corpus to spaCy's format |
| `train` | Train a spaCy pipeline using the specified corpus and config |
| `evaluate` | Evaluate on the test data and save the metrics |
| `package` | Package the trained model so it can be installed |
| `assemble` | Combine the model with a pretrained pipeline. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `train` &rarr; `evaluate` &rarr; `package` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/development/train.csv`](assets/development/train.csv) | Local | The training data |
| [`assets/development/dev.csv`](assets/development/dev.csv) | Local | The development data |
| [`assets/development/test.csv`](assets/development/test.csv) | Local | The test data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
