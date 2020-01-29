import pickle

file = open('Corpus.p', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

for i in data:
    print(i)