# Artificial neural network
- Another mechanism to process the corpus and find the insights on them 
- Why we need ANN?
- In standard of algorithm the steps to solve the problem are well defined
- But the rules are unambiguous
- The probelm with the subtle input can't follow the standard algorithm 
- train with examples and system learns from it
- The learning is the key to the ambiguous world
- The models are not going to being a static one and we have to keep learning with them 

### Classification 

- classification is the task of assigning predifiens dis-joint categories to objects 
- based on teh tuple given we have to find a line/ plane that seperate the two classes
- the classification model will find the fuction that will connect the input variable to the output class
- If the inputs are linear seperable then classification model find the fuction as a line and seperate the fuction as two spaces
- the classes are disjoint and the input should fall in to only one class
- ex) decision boundary for OR gate
- ex) decision boundary for sentiments
- There are problems that are not linear seperable problems(eg)XOR)

## Perceptron 
### Laws of association
- Aristotle's attempts on fundamental laws of learning and memory
- **Law of similarity** : If two thigs are similar the thought of one will tend to trigger the thought of the other
in LSI it decompose the tf-idf to three matrices
One is the left singular matrix (U) diagonal matrix - singular matrix (sigma ) and the right singular matrix(V^T)
- The raws of U represent the words - the raws represent the features of the the words from all documents
- We can able to capture the similar words
- The context related to the word will be learned
- If we are picking one word then the context related to the word is learned from LSI aswell as the word to vec
- It will be able to tell you that what are all the words related to it based on the cosine distance
- **Law of contrast** : Seeing or recalling something will trigger the completly opposite
- **Law of contiguity** : Things or events that occur close to each other in space or time tend to ger linked together in the mind.
- **Law  of frequency** : The more often two things or events are linked the more powerful will be that association think of next word prediction the strength of the association decides who is the probable candidate
- the artificial neuron is called perceptron
- There is a activation fuction that reads the product of input and weight and smashes the value and the threshold defines the result
- There is a bias function as well
- Numpy is helpful for mathematical operations
### Perceptron Learning
- It have to learn the weight
- They adjust until the output is consistent with the target output in the training example
- weight is updated on every iteration
- The weights are updated along with a parameter (learning parameter)called eta and it is difficult to find an accurate value for it
- **Simple algorithm**
- Total number of inputs vector = k 
- Total number of features = n
- Learning parameter = 0.01
- set epoch count = 1
a- initialise the weights with random numbers 
- initialise the input layer
- calculate the output
- calculate the error
- update the weights
- repeat the steps from a until error is less than threshold or predefined number of epochs are over
### Acivation functions examples
- Hard threshold
- Sigmoid - middle layer
- Tanh - middle layer
- Relu - rectified linear unit
- Leaky relu 
- softmax - popular in NLP used in out put layer 
### Logical XOR
- When the problem is not linear seperable and then try to include more hidden layer then it will help to find an answer
- In that case the hidden layer reflect as a 0,0 - 1,0 - 1,0 - 1,1 
- It can be imagined as SVD
- U will represent the entire words as row
- But the actual values of X is not like the values in U it will represent the term in more accurate manner
- Shrink the input to hidden layer then process it will become easier
- The input space is tranformed into hidden space
- Hidden layer represent the input layer
- Learn automatically the input representation and patterns
- 0,1 and 1,0 are merged into the h space
- Patterns yielding similar results are merged into one space
- Dimensionality reduction

### Activation function
- Why do we need different activation fuction ?
- **Sigmoid** : limit the value to `[0,1]`
- the value closer to the tail become zero or one
- At the bottom tail most value become zero and the most important aspect of learning of neural network is inhibited
- sigmoid output are not zero centered
- It is undesirable to have all values squashed near the tails where the gradient is zero 
- The activation fuction have to be differentiable then only we can able to learn
- sigmoid is differentiable
- **Tanh** : similar to sigmoid with limit `[-1,1]`
- **Rectified linear unit**
- For values lesser than zero it will be zero otherwise log(1+e^x) for leaky relu for greater than zero its x other wise 0.01x
- There is a continuous gradient for the neuron to be in the active state
- Computationally efficient unbounded and not zero centered

### Multiclass decision function
- All linear classifier  are used for binary classification
- In the case of more than two classes are there then we need a decision fuction that predicts more than two classes by providing appropriate values
- An extension to the case funcion may hard to manage
**Softmax**
- Need a function that takes as inlut a vector of size with N real numvers and normalize it into a K classes
- Need a function that normalizes the net output and classes well separated 
- Need a function that fits the classes using probability and distributes the probability density
- The one hot encoder can be change to the probability distribution of the input range to the entire output set
## Gradient descent
- LOSS function : It is computed based on the mean square error
- `L = 0.5*(y-ÿ)^2`
- COST function : It is a function of model parameters and bias
- J(θ) - 0.5*Σ L(y,ÿ)^2
- θ = (w,b) weight and bias
- We use gradient descent to adjust the weights and as a result to minimize the cost function
- Initialize the weights to random values
- Iteratively adjust the weights in the direction of steepest descent or in the direction that most decreases the cost fuction
- The learning parameter eta is used
- It is used to get into the minimum

- It is used to reduce any arbitary function
- J(θ0, θ1) have to be reduced
- The function is a point in the function and we will take a 360 degree rotation and then we will take a step that will take you down to a local minimum
- The local minimum the it goes with the steepest descent will defined with the initial point which is defined with the funcion
- θj = θj - α partial derivative of  J(θ0,θ1)
- here we are simultaneously updating the θ0 and θ1

