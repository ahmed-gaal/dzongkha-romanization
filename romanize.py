

#import transliterate
from src import dzongkha_pack
import pandas as pd
from transliterate import translit



# Load DDC parallel corpus
df = pd.read_csv('data/ddc.csv')

df.columns = ['english', 'dzongkha']

def romanize_text(col: str, reverse: bool):
    """
    Utility function to romanize text.
    Params:
        col: (str) Name of column to romanize
        reverse: (bool) Whether to perform reverse romanization
    Returns: 
        array of romanized text
    """
    romanized = []
    if reverse:
        for idx, sentence in df[col].astype(str).items():
            romanized.append(translit(sentence, 'dz', reversed=True))
    else:
        for idx, sentence in df[col].astype(str).items():
            romanized.append(translit(sentence, 'dz'))

    return romanized


df['romanized'] = romanize_text('dzongkha', reverse=False)
df['reversed'] = romanize_text('romanized', reverse=True)

df.to_csv('data/romanized_corpus.csv', index=None)
