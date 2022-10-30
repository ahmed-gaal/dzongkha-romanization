"""
@author: Ahmed Ga'al
Data preprocessing & Word Segmentation
"""
import os
from re import L
from tokenize import Token
import gdown
import json
import string
import tensorflow
import numpy as np
from functools import lru_cache
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from params import Params


# Create paths to extract frequencies and tokenizers
Params.probs.parent.mkdir(parents=True, exist_ok=True)
Params.tokenizer.parent.mkdir(parents=True, exist_ok=True)

# Define a constant TSHEG storing the char ་ for later use
TSHEG = r"་"


def extract():
    gdown.download(
        os.environ.get("FREQ"),
        str(Params.probs)
    )
    gdown.download(
        os.environ.get("DZO_TOK"),
        str(Params.tokenizer / 'dzo_tokenizer.pickle')
    )


def get_dzo_frequencies(freq):
    """
    
    """
    with open(os.path.join(freq), 'r') as f:
        probs = json.load(f)

    max_len = max([len(w) for w in probs.keys()])
    n = sum(probs.values())
    return probs, max_len, n


@lru_cache(maxsize=None, typed=True)
def segment(text, PROBS, MAX_LEN, N):
    """
    
    """
    text = text.lower()
    candidates = []
    if not text:
        return []

    for first, other in [(text[:i+1], text[i+1:]) \
        for i in range(min(len(text), MAX_LEN))]:
            candidates.append([first] + segment(other))
    segments = max(
        candidates, key=lambda x: np.prod(
            np.array(
                [PROBS.get(word, 10. / (N * 10 ** len(word))) for word in x]
            )
        )
    )

    return segments


def remove_punctuation(s):
    punc = string.punctuation
    pun = s.translate(str.maketrans("", "", punc))
    return pun


def preprocess(s):
    rem_pun = remove_punctuation(s.lower())


# Tokenization
def tokenize(lan):
    tok = Tokenizer()
    tok.fit_on_texts(lan)
    return tok


def vectorize(lan, tok):
    vect = tok.texts_to_sequences(lan)
    return vect


def pad_sen(vect, sen):
    lan_pad = pad_sequences(vect, sen, padding='post')
    return lan_pad



def new_func(train: bool):
    if train:
        eng = df_train["english"].values
        dzo = df_train["dzongkha"].values
    else:
        eng = df_test['english'].values
        dzo = df_test['dzongkha'].values
    return eng,dzo

eng, dzo = new_func()

extract()
PROBS, MAX_LEN, N = get_dzo_frequencies()

# Applying standardization to English & Segmentation to dzongkha
eng = [preprocess(s) for s in eng]
dzo = [" ".join(segment(s)) for s in dzo]

# getting rid of extra TSHEGs between 'words'
to_replace = " " + TSHEG + " "
dzo = [sentence.replace(to_replace, " ") for sentence in dzo]

# getting rid of extra spaces
dzo = [' '.join(sentence.split()) for sentence in dzo]

eng_tok = tokenize(eng)
dzo_tok = tokenize(dzo)

def max_sen(lan):
    return max(len(s.split(" ")) for s in lan)

eng_max_sen = max_sen(eng)
dzo_max_sen = max_sen(dzo)

eng_vect = vectorize(eng, eng_tok)
dzo_vect = vectorize(dzo, dzo_tok)

eng_pad = pad_sen(eng_vect, eng_max_sen)
dzo_pad = pad_sen(dzo_vect, dzo_max_sen)





