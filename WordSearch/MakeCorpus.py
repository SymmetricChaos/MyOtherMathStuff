import pickle
import re
import csv

C = []
with open('Corpus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # Remove words too short to use
        # Really even three letters is too short
        # but they are good for kids word search
        if len(row[0]) < 3:
            continue
        # Remove proper nouns
        if any([x.isupper() for x in row[0]]):
            continue

        C += row

print(C)
print(len(C))
file = open( "Corpus.p", "wb" )
pickle.dump(C, file )
file.close()