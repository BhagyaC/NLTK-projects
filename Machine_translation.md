# Introduction and historical approach to machine traslation
- machine traslation is convertion of one language to another
- there are various methods
- word to word traslation
- syntatic translation - parse tree translation
- semantic translation
- interlingua - knowledge representation formalism for multi- language translation

# AMT 
- Automatic machine translation - The idea of the ability to make anyone speak to anyone without the boundary of language is the most appealing idea
- The goal of the automatic machine translation is to produce error free translation
- This must preserve the source of the language
- AMT is a hard problem
- Parellel corpora aids in the devolopment of AMT
- Prallel copora is a collection of corpus that contains a collection of original text and its translation in various languages. In most cases, parallel corpora contain data from two languages

## MT from examples
- Translation by analogy - Example based machine traslation(lazy learning)
 from example find the matching pairs from two language
 
- MT model from data - statistical machine learning - Translation model with language specific parameters
- Train model parameters and apply to unseen data
### Statistical machine traslation
- Traslations ate generated using parameters and models which are derived from the analysis of biligual text corpora
- Let us assume that the task is to translate a french sentence f with a sequence of  length m . Translated language english sentence will be assumed to have the sequence and n is the length of the English sentence.

## ARGMAX
- The arguments of the maxima function f is defined for a set D as 
`arg max f(x) = x|f(x)>= f(y),for all y belons to D`
- The sentence with the library from there the one with the maximum probability is created

## ARGMAX - MT
- The given french sentence f , find the most likely Englist sentence e that maxima function f is defines as argmaz P(e|f)     
- In english sentence e, out of all such entence, which yields the highest value for P(e|f).
- It is  possible to have more than one translation for a given sentence . In such cases argmaz finds one English sentence that yields the highest value for P(e|f)

## The noisy channel model for MT
- In a transmission channel the source language will get manipulated with noise at the reciever  guesses the the source words the same method is used here.
- There will be a source language generator P(e) ---> Noise channel translation P(f|e)---> decoder arg max P(e|f) = P(e)*P(f|e)----> é
- The noisy channel model , The language model generates an English sentence e . The traslation model transmits e as the French sentence f. The decoder finds the english sentence é which is modt likely to have the words.
- P(e) is the distribuition over which sentence arelikely in English and P(f|e) is the translation model that indicates the likelihood seeing the french     sentence f as a translation of e
- Many bilinguals whose mother tongue is not english may think of the sentence they want to speak in their mother tongue first and then speak out the translated version English
- Instead of argmax different decorder use different function

## Bayes rule for MT
- By applying bayes theorem the translation problem is broken down into two smaller problems. Assume that we have a french sentence f and we would like to translate into an english sentence e
- From the probabilistic perspective , we want to find the English sentence e that has maximal probability given the french sentence f.  Using bayes rule we can write this problem as `P(e|f) = P(f|e)*P(e)/P(f)` we know that P(f) is an independent variable so we can neglet it and rewrite the equation as `P(e|f) = P(f|e)*P(e)` and we will calcualte the argmax of this to get the english sentence
- P(f|e) is called the translation model
- P(e ) - is a the english model
- The problem is reduced to modeling these 2 distribution Now we have to estimate the parameters of the P(f|e) from the training examples

### sparsity and smoothing
- Newer ways of forming a sentence is common 
- It is possible that a trained model will see a new n'gram 
- These n gram results in P(x|y) = 0
- P(x|y) = 0 this will propagate though and produce a zero probability for the entire sentence 
- Smaller probabilities too create a very small value 
- To avoid P(x|y) = 0 linear interpolation is used
- Then for new words in the n-gram model P(x|y) will always have a small value
- Using skip gram or CBOW the context is captured and we are able to fill the words in the sentence
- To avoid the underflow of values of multiplication to find P(e), one can use log .Which will result in adding addition
### Evaluation of the language model
- Can we apply Bayes rule for evaluation the model 
- A model can be evaluated based on the test data
- A better model is one which assign a higher probability to the word that actually occurs 
- The best model is the one that optimizes the P(model)P(testing dataset)
- A model that outputs zero probability for any unknown sentence will be discarded

### Perplexity 
- The tiny numbers of P(e) may underflow any floating points scheme 
- An n-gram model will assign a very tiny P(e) for long sequence 
- Many n-gram conditional probabilities may also be a very small value
- The product for P(e) will be tiny
- To compare models P= 2^(-log2(P(e))/|V|) is computed |V| is the number of words in the test data
- P is known as the perplexity score
- A good model will have relatively small perplexity score

