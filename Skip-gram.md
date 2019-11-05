# Skip-gram model
## How to implement skip-gram model with python
- 1. create a init model function with parameters as context window size ,word embedding size epochs and eta
- 2. create another function called initialize weights and intialize the weights for embedding weights and context weights
- 3. create the foraward pass create H with the dot(transpose(embedding weight) , X) and U with the dot(transpose(context weight), H)
and calculate the output as the result of softmax return H,U,Y
- 4.ceate a function for back propagation - X,H,E are the parameters called the outer function and calculate delta error of both context weights and embedding weights. Then update the weights for the context and embedding
- 5. Then create the train function - for all epochs for all target vallue , context word pairs
    - call forward pass function
    - compute the errors for all context words and take the sum as the total error
    - call back propagation with the target word, H, error
    - compute the error for the each epochs and evaluate the model minimizes or not
    - the graph of the error will not be smooth if the learning parameter is apt and error in the calculation
## Reduction of complexity
-There may be words like of, the don't gives much information about the words - context word is not giving any meaning to the context
- there can be situation vise versa
- how to reduce the complexity
- check for the duplicates in the bigram or trigram context words they may be just switched in the order in the context words
- normally we use 5 gram generally 
- we can also remove some words based on the frequency like [the,of ,return..]
- words with less frequency or infrequent words appearing as context words could be discarded as they may not provide contextual information to the central word
- subsampling used by word2vec.c that randomly remove a word from the sample
- where vocab[word].cn is the count of the word and train_word represents all the training words. Then the probability of the word in decided based on the generalised random value random. If ran< radom keep it else discard the word
- another mechanism to reduce the computation is called negative sampling - The size of the network is the size of the vocabulary
- For every training cycle of input the every weight in the network needs to be updated
- For every training cycle Softmax function computes the sum of the output neuron values
- The cost of updating all the weights in the fully connected network is very high
- Is it possible to change only a small percentage of the weights?
- Select a small number of negative word
- while updating the weights these samples output zero while positive samples wiil retain its values
- During the backpropagation the weights related to the negative and positive words are changed and the rest will remain untouched for the current updates and it reduce the computation drastically
- Select the most frequent words as the negetive samples
- Then the equation will increase the probability of choosing the less frequent words
- One way to implement it is to create a unigram table filled with the words according to their probability
- The frequent words would be appearing several times according to their frequency thereby increasing the probability of choosing the frequent words for the negative samples
- apply some mechanism that boost the probability of less frequent words and reduce the probability of the high frequent words (f(w)^3/4)
## Binary tree and hierarchial softmax
### Softmax
- How can we reduce teh computational complexity from the softmax layer
- softmax is a normalized exponential function
- It has a flat hierarchy with a probability value for every output node of depth =1
- Normalized over the probability of all |V| words
- error correction happens for every output --> hidden units 
- Huge cost if the vocabulary size |V| is of the order of several thousands

### Balance binary tree
- consider the words in the vocabulary is in a binary tree format
- balance binary tree is a - complete binary tree and left node < root < right node
- The all words are represented in the leaf nodes only
