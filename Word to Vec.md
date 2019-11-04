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
- 
