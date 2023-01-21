from pathlib import Path

import spacy
import typer
from spacy.tokens import DocBin

ASSETS_DIR = Path(__file__).parent.parent / "assets" / "development"
CORPUS_DIR = Path(__file__).parent.parent / "corpus" / "development"


def read_csv(csv, sep=","):
    """Read csv and return each line."""
    with open(csv, encoding="utf8") as file_:
        for line in file_:
            yield line.split(sep)


def convert_record(nlp, text, label, start, end):
    """Convert a record from the tsv into a spaCy Doc object."""
    doc = nlp.make_doc(text)
    span = doc.char_span(int(start), int(end), label=label)
    doc.ents = [span]
    return doc


def main(
    assets_dir: Path = ASSETS_DIR,
    corpus_dir: Path = CORPUS_DIR,
    lang: str = "en"
):
    """Convert the corpus's csv files to spaCy's binary format."""
    nlp = spacy.blank(lang)
    for csv_file in assets_dir.iterdir():
        if not csv_file.parts[-1].endswith(".csv"):
            continue
        docs = (
            convert_record(nlp, *record)
            for record in read_csv(csv_file) if record
        )
        if docs:
            out_file = corpus_dir / csv_file.with_suffix(".spacy").parts[-1]
            out_data = DocBin(docs=docs).to_bytes()
            with open(out_file, "wb") as file_:
                file_.write(out_data)


if __name__ == "__main__":
    typer.run(main)
