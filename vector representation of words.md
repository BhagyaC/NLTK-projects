## Vector representation of words

Let V be the unique terms and mod(V) be the size of the vocabulary. Then every vector representing the word R would point to a vector in the V dimensional space.

- How to represent a word

- **One hot encoder** 
- every word is represented independetly.The term,house apartment all are coded independently(allwords in dictionary represented independtly) 
- It will create a huge vector space
- The main goal is to reduce the similar terms to sub spaces
- We could represent the synonyms in a single axis
- Is a vector method - color axis will contain all the type of colors
- Has a vector method - classroom - board, student, teacher
- The normal entity extraction in spacy is an example of IS-A method

# Contextual understanding of the text

- The study of meaning and contxt should be central to linguistics
- Exploding the context-dependent nature of words
- Language pattern cannot be accounted for in terms of a single system
- The collocation gives enough clue to understand a word and its meaning 
- Now we are considering the co-occurances of the word
- "you shall know a word by the company it keeps"
- No study of meaning apart from context can be taken seriously 
- For example consider the word BANK - we can understand the meaning only when we know the context
- The collocation, a particular word consistently co-occurs with the other words, gives wnough clue to understand a word and its meaning

### Co-occurance matrix

- A co- occurance is a combination of terms that are likely to be used in the same context. A co-occuranc matrix stores co-occurance of words. The count of a pair of words that appears in a context window is represented as an element of matrix
- all words in the document is represented as row and column in the document and if they are comes as neighbours then the matrix where they meets will be put a 1
- There are unigram , bigram , trigram is named because of how many words are we considering at a time
- N-gram means sequance of words of length n 
- Consider the text "peter piper picked a peck of pickled peppers"
- unigram `<s>`
- bigram `<s>`peter
- trigram `<s><s>`peter
these are the gram for the first round
- unigram peter
- bigram peter piper
- trigram `<s>`peter piper
this is for the second round
and so on

### Collocation and Dense word vectors

- it is a juxtaposition of two or more words that moves together than by chance
- Identify a model that enumerate the relationship betwenn term and document
- Identify the model that put similar item close together
- Model that discovers /uncovers the sematic similarity between words and documents
- devolop a distrubuted word vectors or dense vectors that captures the linear combination of words
- **Methods to create a dense vector**
- The main idea is distribute and create a vector that is dense
- Latent sematic analysis /indexing
- Neural netword using skip gram and CBOW
- CBOW - uses surrounding words to predict the center of words
- Skip gram use the center of words to predict the surrounding words
- Brown clustering : statistical algorithm for assigning words to classes based on the frequency of their co-occurance with other words
- Dense vectors are always need for ML purposes

### Singular value decomposition 
 - This is a method to factorise a single matrix into three matrices
 - A = U sigma  V^t
 where A = M*N matrix
 - U is M*K
 - sigma = diagonal matrix K*K
 - V^t = K*N
 - the row vectors of U are called as the left-singular vectors
 - Row vectors of U form an orthogonal set
 
 -The column of v^t is called right singular matrix 
 - The row of V^t form an orthonormal set
 - The sigma is the singular matrix. It is a diagonal matrix and its values are arranged in the descending order
 - SIngular values are the values in sigma
 - singular values reflects teh major and associative patterns in the data and ignore the smaller less important influences
 - The highest varience in the original data set or most of the information related to term-document matrix is captured by the higher order dimension 

- **Dimensionality reduction**

- SVD is better suited for measuring the similatiy between documents, by exploding the similarity pattern s that exists in the word co-occurance
- The co-occurance terms are mapped into the same dimensions thereby reducing the dimensions
- Increase the similarity representation of the sematically similar documents
- SVD takes the original matrix in the m dimesinal space and transforms it À the reduced dimesional space k <= m  
- while reducing the dimesion it should be in such a way that the the difference between the new matrix and the old one must be less
- **Least square method**
- Along with reducing the dimension it also maps to a same plane
- Its is like fitting a line to a set of words
- similar documents are put into same plane and similar words are put in the same axis
- svd find the strongest pattern in the data
- Most variability is captured by a small fraction of the data total set of dimesions
- the patterns among the terms are captured by the left sigular matrix and the patterns among the documents is captured by the right singular matrix
- The eigen vectors associated with the last largest eigen value indicates the direction of largest varience

### Query processing in SVD(latent sematic indexing)
- The data set is loaded
- the tokens are extracted
- dictionary created
- doc term matrix created using doc2bow from the tokens
- tf-idf model created and using that model with doc_term_matrix and passing the doc_term_matrix to the tf_idf model the corpus created
- LSI - LSI (Latent Semantic Indexing) [8] is one of the most popular linear document indexing methods which produce low dimensional representations using word co-occurrence which could be regarded as semantic relationship between terms. LSI
aims to find the best subspace approximation to the original document space in the sense of minimizing the global reconstruction error (the Euclidean distance between the original matrix and its approximation matrix). It is
fundamentally based on SVD (Singular Value Decomposition) and projects the document vectors into the subspace so that cosine similarity can accurately represent semantic similarity. 
- the new doc selected and tokenised
- doc to vec generated for the new tokens of doc (which is known as the query creation)
- lsi created with the corpus and id2word as the dictionary and num_topics as 1 (The K value or the eigen value that is the value of the inner set)
- similarity  index created and the new doc token is send to the index
- And the sorted 

### Topic modeling
- Using the LSI ie the SVD they used to predict the topics from the entire document corpora
- The data is loaded and preprocessed and as earlier only diff is the topic is defines and classified
- Here the document contains different topics
- K value = 200
- Token = 25000
- But it is not a good classifier becuase the noise in tf-idf
- So look at the document the and think about how we can preprocess then in a better way so that the sigma value can be reduces in a much faster method
- And think about preprocessing methods so that it can aid the preprocessing

- 



