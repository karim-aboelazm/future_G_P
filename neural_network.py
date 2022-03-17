# [1] Numpy >> pip install numpy
# nltk >> Natural Language Toolkit >> pip install nltk

import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

# tokenize >> التعرف علي الكلام 
def tokenize(stm):
    return nltk.word_tokenize(stm)

# stem >> تفكك الكلام
def stem(word):
    return stemmer.stem(word.lower())

# bag >>  حقيبة  
def bag_of_words(word_tokenize,words):
    stm_word = [stem(word) for word in word_tokenize]
    bag = np.zeros(len(words),dtype=np.float32)
    for indx , w in enumerate(words):
        if w in stm_word:
            bag[indx] = 1
    return bag

