# Vector space models

- How can we do the mathematical rules of the text and can we do the text arithmetic or not

- The words in the corpus is linearly independet
- If we are using the stemming then atleast the some words can be understood with the similarity
- Using vector space model defines the position in the space and it is easy to find the distance between all the words
- If there are *n* unique words in the data then there are *n* different axises in the space
- It will create a higher dimensional space
- If we are using the semtantically connected vectors where we want to find the relation to the terms in the documents
- we have to put some terms nearer to define the relationship
- While converting the text to the vectors it have to contain all the relationship as in the text
- the synonyms and all other relationship must be represented to the dense vectors
- If we are able to the convert with any representatio where all the knowledge in the text (which is not possible) - then we try to find the patterns in the text which will reduce the lack of sufficient knowledge.
- patterns give some help to predict the outcome
- consider the linear and non linear classification along with NN and related algorithms


## Word embedding 
find sematic and syntax similarity with words and create the dense vector
- Why , an what and how are the main questions to solve NLP
- there are many way to create the dense vector like CBOW, skip-gram model and another word to vec model 

## Sequence learning

- first consider the count the word in the corpus and did some prediction based the count and started learning more about the words based on the syntatic and sematic structure
- using vector space and Ml model 
- sequence learining is the considering of sentence as a whole
-  sequence learning is the study of machine learining algorithms designed for application that require sequential data and temporal data

## Recurrent Neural Network 
- sequential data prediction is considered as a key problem in machine learning and AI
- we read the text document sequentially to understand the content
- The earlier sequence is important to predict the next word sentence and paragraph
-  create a fixed size vector to deal with the use of NN
- If a word is occured twice in the sentence but could not be accomodated in the sliding window then the word is learned twice
- some issues like exploding and vanishing gradients
- LSTM and GRU
