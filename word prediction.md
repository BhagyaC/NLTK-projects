## Examples of word prediction

### Probabilistic Language Model

- Google Ngram is used to predict words from a sentence
- The maximum number of N gram is retured as a result

### Probability in NLP
-  In order to predict the result the human need domain knowledge and syntatic and lexical  knowledge , knowledge about the sentence structure
- Some words are hard to find
- Natural language is not deterministic in general 
- Some sentences are familiar or had been heard/seen / used several times 
- They are more likely to happen than others hence we could guess


- **Why probability**
- probability is used when we need to predict the next word
- This gaves some mechanism to make the prediction
- Make informaed decision when there a certain degree of uncertainily and some observed data
- Give the quantitative description / likelihoods associated with various outcomes
-  The probability of the next word in the sentence
- Likelyhood of the next word is formalized through an observation by conducting experiments- counting the word in the document
- The count the document problem is such that the entire document is split into tokens and the probability of the token that to become a next word is 1/total number of tokens
- The event for the sample space is that we will select the unique words from the sample 
- An event is a sample of same type
- Probability of the event is defined as the sum of probability of all words defined in that type
- Random variable - is a variable whose possible value are numerical outcome of random phenomenon
- There are two type - continuos and discrete
- To capute the type-token distinction we use random variable W and maps to the sample space
- V is the set of type and  values represented by a variable v
- P(V=v) = P(X E sample : V(X) =v)
- random variables are useful in describing various events
 
 
### Joint probability
- given two events E1 and E2 the probability of their conjuction is called joint probability
- the probability of `t` and `h` must be higher than probability of `the` 
- Conditional probability `p(A|B) = p(A^B)/p(B)
- conditional probability can aid the bi and trigram example
- The two events are dependent if the probability of one relies on occurance of the other, if there is no other interaction then the events are independent
- The events E1 and E2 are independent if and only if `P(E1,E2) = P(E1)P(E2)


### The language model

- Natural language sentences can be described by parse trees which use the morphology of the word syntax and sematics
- Probabilistic thinking - finding how likely a sentence occurs or formed given the word sequence. In a probabilistic world the language model is used to assign a probability to every possible word sequence W
- The current research in language model focuses more on the building the model from the huge corpus of text
- In the language model the input sentence is given and then the language model will look into the corpus and predict the next word
- the goal of the probabilistic language model is that compute the probability of the sequece of word
- task is to predict the next word using the probability - that is the probability of cat roars is  less compared to the the sentence cat meows

### Chain rule and markovs assumption
- It is difficult to compute the probability of the entire sequence `chain rule` is used to decompose the joint probability of a sequence into a product of conditional probability
- It is possible to P(w|h){h is the history} but it does not really help in reducing the computational complexity 
- We use innovative waus to string words to form new sentences
- Finding the probability for a long sentence may not yield good outcome as the context may never occur in the corpus
- short sentence may provide better results
- **Markov assumption**

- the future behavior of a dynamic system depends on its recent history and not on the entire history
- The product of the conditional probabilities ca be written approximately for a bigram as `P(wk|w1 ^k-1) approx == P(wk|wk - k+1 ^ k-1)` 
- for a single word we are considering a small number of n grams to predict it other than taking all the words in the sentence
- we are considering the nearest the neighbours and we find the answer at most of the times

### Generative models 
- we are try to create a model with a given corpus
- we can try for the unigram trigram and etc
- generate a a document containing N words using N gram 
- A good model addigns higher probability to the word that actually occurs
- The location og the word in the document is not important 
- P(N) is the distrubution over N and is same for all documents. Hence it is ignored
- Wi to be estimated in this model is P(Wi) and it must satisfy the sum of probability of all indivitual words must be 1
- **Maximum likely hood estimate**
- The one of the method to find the unknown parameter(s) is the use of Maximum likelihood esimation 
- Estimate the parameter value for which the observed data  have the highest probability 
- Training data may not have all the words is presented then MLW is Zero 
- Add a smoothing parameter to the equation without affecting the overall probability requirements - that is adding some parameters such that when an unknown word comes and the entire probability becomes zero situation can be avoided
- 
- ***Bigram language model*
- this model generates a sequence one word at a time. starting with the first word and then generating each suceeding word conditioned on the previous one
- Estimates the parameter for all bigrams
- The parameter estimation does not depends on the location of the word
- IN this they are considering how many times two w and w1 words are coming together and to the number of times w appears inthe bigram sequence 
- few sentence will be given for language model generation
- for a bigram it will select a window of two and then will predict the frequecy of the window in the entire corpus
- if a new sentence is given and have to find out that the sentence is legel or not 
- then find the joint probability of the sentence using markov assumption
- `p(w|s)*p(w2|w1).....P(e|wn)`
 
 


 
