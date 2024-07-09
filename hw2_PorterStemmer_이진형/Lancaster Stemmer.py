from nltk.stem import LancasterStemmer

stemmer = LancasterStemmer()

print(stemmer.stem("working"), stemmer.stem("works"), stemmer.stem("worked"))
print(stemmer.stem("amusing"), stemmer.stem("amuses"), stemmer.stem("amused"))
print(stemmer.stem("happier"), stemmer.stem("happiest"))
print(stemmer.stem("fancier"), stemmer.stem("fanciest"))
print(stemmer.stem("was"), stemmer.stem("love"))
