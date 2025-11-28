"""
Text cleaning utilities for Spanish text analysis.
"""

import re
import unicodedata
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Lazy loading for spacy model
_nlp = None


def get_nlp():
    """Get or load the Spanish spacy model with only lemmatizer enabled, downloading it if necessary."""
    global _nlp
    if _nlp is None:
        import spacy
        try:
            # Load model and disable all components except lemmatizer
            # Disable parser, ner, and other unnecessary components for efficiency
            _nlp = spacy.load("es_core_news_md", disable=["parser", "ner", "attribute_ruler"])
        except OSError:
            logging.info("Spanish spacy model not found. Downloading es_core_news_md...")
            import spacy.cli
            spacy.cli.download("es_core_news_md", quiet=False)
            # Load model and disable all components except lemmatizer
            _nlp = spacy.load("es_core_news_md", disable=["parser", "ner", "attribute_ruler"])
            logging.info("Spanish spacy model downloaded and loaded successfully.")
    return _nlp


def clean_text(text: str) -> str:
    # Lowercase and remove punctuation, but preserve accents
    text = text.lower()
    # Remove punctuation but keep accented characters
    text = re.sub(r"[^\w\s]", "", text)
    return text


def clean_word(word: str) -> str:
    # Lowercase and remove accents using Unicode normalization
    word = word.lower()
    word = "".join(
        char
        for char in unicodedata.normalize("NFD", word)
        if unicodedata.category(char) != "Mn"
    )
    return word


def lemmatize_text(text: str) -> str:
    """
    Lemmatize a text string, handling multi-word phrases.
    Returns the lemmatized version of the text.
    """
    nlp = get_nlp()
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return " ".join(lemmas)


def lemmatize_word(word: str) -> str:
    """
    Lemmatize a single word or phrase.
    For phrases, lemmatizes each word and joins them.
    """
    nlp = get_nlp()
    doc = nlp(word)
    lemmas = [token.lemma_ for token in doc]
    return " ".join(lemmas)
