import os.path
import sys

fname = input("Enter the filename: ")

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
lineList = infile.readlines()

for i in range(min(4, len(lineList))):
    print(i + 1, ":", lineList[i].strip())

word = input("Enter a word: ")
cnt = 0

for line in lineList:
    cnt += line.count(word)

print("The word", word, "appears", cnt, "times in the file")

infile.close()
