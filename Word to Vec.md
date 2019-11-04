## Feed forward and backpropagation Neural Network
- The sequential nature of data
- examples - speech , documents, videos, weather forecast, financial stock market
- Properties of ANN
- Massively parallel distributed structure
- Ability to learn 
- Ability to find the patterns in the data
- Generalize and associate data

### Back propagation model 
- The idea is to change the weight so that the estimated target  is  approx equal to target
- Thereby minimizing the error for each neuron and the network as a whole
- The goal is to minimize J(0)
- calculate the input to each neuron using the dot product between the input and weight
- Once we find there is an error then back propagate the error and edit the weights
-  find the partical derivative of J(0) with y1{output from the final layer sigmoid function} , y1 with g1{g1 fed into the sigmoid function used in the final layer as a activation function to get y1},g1 with V11{weights on the final layer}
- all these are multiplied together to get the derivative of loss function on   weights to the final layer
- By the similar fashion then we can adjust the input hidden layers as well
- That is partial derivative of the J(0) on the W 
- **Steps with the algorithm**
- Initialize the the weights
- feed input 
- compute the z{input to the hidden layer},h{output from the hidden layer},g{input to the output layer},y{The output} --> that is the forward propagation
- Back propagate the and calculate  ΔV and ΔW
- Update the weihgts Vnew = Vold - η ΔV
- Wnew = Wold - ηΔW
- ΔW is calculated using the chain rule 

# Word to Vec
- Word embedding using word2Vec
- Devoloped by Google 
- IN LSI we have a term context matrix which will be converted into 3 matrices one is left singular matrix, singular matrix, right singular matrix
- The Left singular matrix is the word embeddings and right singular matrix is the context
- singular matrix can be reduces and along with LS and RS will be reduces 
- The goal is to process each word in a vocabulary of words to obtain a respective numeric representation of each word in the vocabulary
- Reflect the sematic similarities and syntantic similarities or both between words they represent 
- Map each of the plurality of words to a respective vector and output a single merged vector that is a combination of the respective vectors

### Introduction to CBOW and skipgram models
## Context words and central word
- continuous bag of words models - Central word is surrounded by context words- Given the context words identify the central word
- Skip gram model - Given the central word, identify the surrounding words
- we will select a window size and find the central word and then predict the context words
- In skip gram model the window is given and it will give the context words have to predict the surrounding words
- In continuous bag of words the inputs are the context words and the weighted sum is taken predict the word
- Maximize probability of word based on the word co-occurance within a distance of n
- Skip gram model - the central word will be given as the input and the model will predict the context words
- SG maximize probability of words based on the word co-occurance within a distance of [-n,+n] from the central word

## One word learning architecture
- source preparation for training
- source text - wish you many more happy  returs of the day
- consider there is a start symbol
- then in first epoch the window will contain start symbol and wish you many , where wish is the central word
- then consider the bigram with the central word - wish you , wish many
- the input layer of size V , hidden layer of size N and output layer is V dim
- Only one input at a time
-Consider One hot vector as a input to the vector
### Forward pass for word2vec
- **Hidden layer**
- This is a neural network is fully connected- Input vector is one-hot vector
-  h = W^T X
- where X is the input and W is the weight
- If we are using the onehot vector it is just copying the row correspond to the word in one hot to the h
- In the similar way calculate the output later input
- uj = Vw^T* h
- In the output layer we apply the softmax then we will get the output
- At the output layer we apply the softmax to get the posterior distribution of the words It is obtained by `p(wj|wI)= yj`
- How to update the weight- almost similar to the back propagation and we are using another error mechanism
- The learning / training objective is to maximize ot minimize the error between the target and the computed value of the of the target which is yj* - t and t is same as the input vector in this case .We use cross-entropy as it provides us with a good measure of "error distance"
- minimising the error is also same as maximising the probability
- w0 is the output word and E is the loss function . It is the special case of cross- entropy measurement between two probabilistic distribution uj* and uj'
- why cross entropy - log p(x) is well scaled
- selection of step size is easier
- with p(x) multiplication may yield to naer zero causing underflow
- For better optization logp(x) is considered
- we update the weight using partial derivatives
- yj-tj = ej which is the prediction error
- Then use the chain rule 
- calculate the   new weight using the old values
- Once the weights are changed we have another set of values to the hidden layer as inputs
- **Some more insights**
- The prediction error E propagates the weighted sum of all words in the vocabulary to every output vector vj'
- The change in the input vector is defined by the output vector which in turn is updated due to the prediction error
- Ideally vj.vj' results in an identity- it is for the learning the same words and creating their vectors
- The rows of the input hidden layer vj stores the features of the words in the vocabulary v
- model parameters accumulate the changes until the system reaches a state of equilibrium
### Matrix operations
- The words we want to train - we love NLP and machine learning
-  `we --> [1 0 0 0 0 0]` etc
- construct a matrix of size 6*10 - 10 is the hidden layer
- the 6*10 is the input to the hidden layer xw^T
- then in h = 10*1
- then v = will be 6
- h*v^T will create *6which is the input to the output layer
- softmax - will give a 6*1 
 - 6*1 error also calculated
 - passed to h (1*10) and the error for w is calculated
 - and the weights are updated like `[wij(new)] = [wij(old)] - η[e.h^T]`
 - Once the training is completed we can neglet the context and hidden layer the embedding layer will give the index of the word, the index of the row in the embedding matrix word  is a word vector
 ## Multiple words model using the CBOW
 - C is the number of context word
 - V is the vocabulary
 - hi recieves the average of the vectors of the input context word
 - The output vector v' is the colomn vector in V represent the relation between the context word and the target word
 - sofmax is used for the output layer for the probability distribution of the target word
 - uj is the context vector
 - uj = V^T*h
 - h = 1/C*W^T*(x1+x2+...)
 - find the error value using cross entropy
 - update the input parameter using `vnew = vold - 1/c*η*EH^T`
 - It will have a distributed representation of vectors 
 - The learned vector explicitly encodes many linguistic regularities and patterns
 - The learning should produce similar word vectors for those words that appeared in the similar context
 - In the example we have to figure out about the cosine similarity 
 - Is it deal with the stemming
 - car and automobiles
 - good awesome fantastic
 
