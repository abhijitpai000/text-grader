import nltk
from nltk import word_tokenize, sent_tokenize
import pyphen
nltk.download("punkt")


def clean_text(text):
    """
    Removes Non-ASCII characters from text.
    """
    return str(text.encode().decode("ascii", errors="ignore"))


def compute_counts(text):
    """
    Tokenize and Compute Word Count, Sentence Count and Syllables count.
    Returns
    -------
        sentence_count, word_count, syllable_count
    """
    sentences = sent_tokenize(text)
    sent_count = len(sentences)
    words = [word_tokenize(sentence) for sentence in sentences]
    punctuation = ".,!?/"
    sybl_count = 0
    word_count = 0

    for word_list in words:
        for word in word_list:
            if word not in punctuation:
                word_count += 1
                x = syllable_count(word)
                sybl_count += x
    return sent_count, word_count, sybl_count


def syllable_count(word):
    """
    Count the Number of Syllables

    Parameters
    ----------
        word: str.

    Returns
    -------
        syllable_count
    """
    dictionary = pyphen.Pyphen(lang="en_US")
    hyphenated = dictionary.inserted(word)
    return len(hyphenated.split("-"))