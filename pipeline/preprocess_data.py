"""
@author: Ahmed Ga'al
Data preprocessing & Word Segmentation
"""
import os
import json
import string
import numpy as np
from functools import lru_cache




def get_dzo_frequencies():
    """
    
    """
    with open(os.path.join(BASE_DIR, 'PROBS_json'), 'r') as f:
        probs = json.load(f)

    max_len = max([len(w) for w in probs.keys()])
    n = sum(probs.values())
    return probs, max_len, n


@lru_cache(maxsize=None, typed=True)
def segment(text, probs=probs, MAX_LEN=max_len, N=n):
    """
    
    """
    text = text.lower()
    candidates = []
    if not text:
        return []

    for first, other in [(text[:i+1], text[i+1:]) for i in range(min(len(text), MAX_LEN))]:
        candidates.append([first] + segment(other))
    segments = max(
        candidates, key=lambda x: np.prod(
            np.array([probs.get(word, 10. / (N * 10 ** len(word))) for word in x])
        )
    )

    return segments


def remove_punctuation(s):
    punc = string.punctuation
    pun = s.translate(str.maketrans("", "", punc))
    return pun


def preprocess(s):
    rem_pun = remove_punctuation(s.lower())
    return rem_pun


