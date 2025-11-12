from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["jumping","jumps","jumped","running","runner"]
stem_words=[stemmer.stem(word) for word in words] 
print(stem_words)

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
words=["jumping","jumps","jumped","running","runner"]
lemm_words=[lemmatizer.lemmatize(word,pos='v') for word in words]
print(lemm_words)