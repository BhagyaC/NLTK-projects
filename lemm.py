import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat flying cardboard"""

stop_words=set(stopwords.words("english"))
tokenized_sent=word_tokenize(text)


filtered_sent=[]
for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)

ps = PorterStemmer()

lemme_words=[]
for w in filtered_sent:
    lemme_words.append(lem.lemmatize(w,"v"))

print("Filtered Sentence:",filtered_sent)
print("lemmatized Sentence:",lemme_words)