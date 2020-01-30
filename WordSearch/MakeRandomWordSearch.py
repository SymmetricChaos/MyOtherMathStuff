import pickle
import random
from MakeWordSearch import word_search_pdf

file = open('Corpus.p', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

def random_word_search_pdf(num_words,size,corpus,
                           min_length=0,max_length=float("Inf"),
                           directions=[],filltype="alphabet"):
    c = [w for w in corpus if (len(w) >= min_length and len(w) <= max_length)]
    words = random.sample(c,num_words)
    G = word_search_pdf(words,size,directions,filltype)
    return G


if __name__ == '__main__':
    random_word_search_pdf(12,20,corpus=data,min_length=10,max_length=10)