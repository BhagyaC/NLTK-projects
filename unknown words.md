### Out of vocabulary

- In a closed vocabulary language model , there is no unknown words or out of vocabulary words
- In an open vocabulary system you may find new words that are not present in the trained model
- pick some words which are below frequency and replace them as OOV
- Treat  OOV as a regular word
- During testing the new words would be treated as OOV and the corresponding frequency will used for computation 
- This will eliminate the zero probability for the sentences cotaining OOV

### Curse of dimensionality 

- A fundemental problem tha makes langauge modeling and other learning problems difficult is curse of dimensionality 
- The joint probability of 10 words in laguage of million words are vocabulary then we need to estimate 10^60 - 1 free parameters

## Naive bayes algorithm for classification
- Used for classification purposes
- Consider two set of emails from ram and raj and we have to classify a new mail is created by ram or raj
- We are usign BOW
- each word will have a frequency count

### Bayes theorem 
- Let us consider random variable X and Y
- `P(X,Y) = P(Y|X) * P(X) = P(X|Y)*P(Y)`
- `P(Y|X) = {P(X|Y)P(Y)}/P(X)`
- Map the bayes theorem to the classification problem
- Let X and Y are random variables X is a set of attributes and Y represent a class
- The relationship between X and Y can be found out with the help of conditional probability 
- In the classification P(Y|X) is very important
- given the set of data - TF_IDF(it can be also n gram)
- we have to find the class to which the email fall in 
 - **Supervised and classification**
 - set of input parameters and a fixed set of classes
 - Every element of the training set is manually assigned a class
 - Goal is to learn the classifier so that it can map a new document any of the class
 - Bayes classifier would assign a probability based on the observation to the new document to aid the class selection
 - class is the max(P(Y|X)
 - P(Y|X) - P(X|y)*P(y)
 - p(y) is the probability of the class in the whole document
 - and others are the parameter probability 
 - if there is a probability of zero then we have to add the smoothing variable
 - We have to look into the content before we come to the attribute
 - Then have to think about the what kind of parameters that we need to apply
