# Stastical properties of words

- Large corpus
- Collection of written text in a digital form
- These are verify a hypothesis about a language
- contain most of the word of the language
- the corpus should cover all the area and must be large enough
- goes to the corpus and then find how it is used in the corpus and then find the synset for the word in each situation
-  lexical resources :
    - A Corpus is a collection of machine readable text
    - representation of collection of the text
    - use statical analysis
    - validate the linguistic rules
    - eg) brown corpus, sussane (subset of brown)
- Operation of text of corpus
  - identify the paragraph and sentence 
  - extract the token
  - count the token and fing the vocabulary count
  - find pattern of the word
  - find the co occurance of the word

### Incidence matrix

- let G be a grapb with n vertices (v1,v1..) and m edges (e1,e2...) then incident matrix is size of m*n defined as

  - Xij = 1 if there is an edge
        = 0 otherwise
- It is also called vertex-edge incident matrix and is denoted by X(G)

- Binary incident matrix : if there is a connection then 1 else put a 0
- Term document binary incident matrix - is a matrix created with all matrix with the document as the column
- if the word is present in the document it set as 1 else 0

- term is a word or cobination of words
- each term at the end is represented as a binary vector
- mathematical operations like and and not will be done on the vector and can retrieve the data

### words and terms 
- word is atomic unit 
- we use term as well as a atomic unit 
- we have to consider the count / frequenct as well 
- vocabulary size = v and v = set of unique words
- term frequency - how many times a term occured in a document
- adjust the frequency with the document length
- also we can yake the log of the weighting = freq - 1 + log t*freq if t*freq > 0 else 0

### Disadvatages
- common words which will not help in the classification 
### Bag of words
- The collection of term*freq is known as bag of words
- the ordering of the terms are not at all important
- It is the quantitative representation of the document

### Type - token ratio

- the lexical variety of the text is defined the type- token ratio (ttr)
- It can be used to measure the vocabulary variation or lexical density of the written text and speech 
- type is the unique word which is devoid of any repetition 
- TTR = V/Tn
- Where V is th vocabulary and Tn is the number of token in the speech or written text

### Inverse document frequency
- IDF = log(N/Df)
- N is the total no of documents
- DFt - count of the documnt which containing t(term)

### TF- IDF
where the tf and idf are multiplied together

- In order to attenuate the effect of frequently occuring terms, It is important to scale it down and at the same time it is necessary to increase th weight of terms that occur rarely.

- IDF is the measure of the informativeness
- rare document gets a significant higher value
- commonly occuring terms are attenuated
- It is a measure of informativeness
- Reduce the tf weight of a term by a factor that grows with its collection frequency


### ZIPF law
- This law states that for a given copora the frequency of any words is inversely proportional to its rank in the term frequency table.
- fr inversely proportional to 1/r^alpha
- alpha is approximately equal to one r is the frequency rank in the document , fr is the frequency in the corpus
- The most frequent word will have the value 1 the word ranked second in frequency will have 1/2^alpha ...
- This emperical law models the frequency distributio of words in languages. This distribution is observed across several languages with a large corpora
- the rank * freq of the term is a constant for a corpora

### MANDELBORT APPOX
- Mandelbort derived a more generalized law to closely fit the frequency distribution in language by adding an offset to the rank
- f(r) proportional to 1/(r+beta)^alpha where alpha = 1 and beta is approx = 2.7 It is still a wonder how such a intricate language generation fits into a simple mathematical relationship. It seems so unreal and perhaps unreasonable

### Heaps law
- This is used to estimate the number of unique terms M in a corpus given the total number of token
- M proportional to T^b 
- M = k*T^b
- where 10<= k<=100 and b approx = 0.49 
- According to the emperical law the dictionary or the vocabulary size increase linearly with the total number of token or words in the corpus .It emphasizes that the importance of the compression of the dictionary
- This law emphasises that we need to reduce the vocab by stemming and lemmatization



