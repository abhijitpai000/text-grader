"""Script for Computing Score."""

from backend.preprocess import clean_text, compute_counts


def _grade_level(total_sentences, total_words, total_syllables):
    """
    Flesch-Kincaid Grade Level Score.

    Parameters
    ----------
        total_sentences: int, number of sentences.
        total_words: int, number of words.
        total_syllables: int, number of syllables.

    Returns
    -------
        grade_level_score.
    """
    grade_level_score = (0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words)) - 15.59
    return grade_level_score


def _reading_ease(total_sentences, total_words, total_syllables):
    """
    Flesch Reading Ease Score Test (FRES).

    Parameters
    ----------
        total_sentences: int, number of sentences.
        total_words: int, number of words.
        total_syllables: int, number of syllables.

    Returns
    -------
        fres.
    """
    fres = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)

    if fres <= 60:
        if 50 < fres <= 60:
            remark = "&#129300 Fairly difficult to read. "
        elif 30 < fres <= 50:
            remark = "&#128565 Difficult to read. "
        elif 10 < fres <= 30:
            remark = "&#128560 Very difficult to read. Best understood by university graduates. "
        elif 0 < fres <= 10:
            remark = "&#128561 Extremely difficult to read. Best understood by university graduates."
    elif fres > 60:
        if 60 < fres <= 70:
            remark = "&#128522 Plain English. Easily understood by 13 to 15-year-old students."
        elif 70 < fres <= 80:
            remark = "&#128515 Fairly easy to read. "
        elif 80 < fres <= 90:
            remark = "&#128516 Easy to read, Conversational English. "
        elif 90 < fres <= 100:
            remark = "&#128513 Very easy to read. " \
                     "Easily understood by an average 11-year-old student. "
        elif fres > 100:
            remark = "&#128519 Very easy to read."
    return fres, remark


def compute_score(input_text):
    """
    Processes input text and Computes Scores.

    Parameters
    ----------
        input_text: str.

    Returns
    -------
        scores, stats
    """
    # Process Input.
    clean_input = clean_text(input_text)

    # Stats
    total_sentences, total_words, total_syllables = compute_counts(clean_input)
    stats = {'total_words': total_words,
             'total_syllables': total_syllables,
             'total_sentences': total_sentences}

    # Readability Tests.
    fres, remark = _reading_ease(total_sentences, total_words, total_syllables)
    grade_score = _grade_level(total_sentences, total_words, total_syllables)

    # Fixing Negative Grade Scores.
    if grade_score < 0:
        grade_score = 0

    # Response.
    scores = {'fres': round(fres, 2),
              'remark': remark,
              'grade_score': round(grade_score, 2)}

    return scores, stats
