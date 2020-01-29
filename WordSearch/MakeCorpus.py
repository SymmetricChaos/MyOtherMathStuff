import pickle
import re
import csv

C = []
with open('Corpus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row[0]) >= 3:
            C += row

print(C)
print(len(C))