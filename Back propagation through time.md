# Back Propagation through time - BPTT
- All the function we are using as an activation functions have to be continuous and they have to be in differentiable
- When we are considering the derivatives of the activation function there will be a peak point and that point is said to be the ideal point where we can have the value for the input for a desirable output
## Forward Pass in RNN
- We have total of 5 equations
- `1 . ht = W*xt + Uht-1 `
- `2. st = tanh(ht)`
- `3. Zt = Vst`
- `4. ÿt = softmax(zt)`
- `5. E = Σ yt log(ÿt)`
- If the corpus have T words coming in then we have x1,x2...xt as the corresponding word vectors
- Ÿt is the probability distribution of predicted word at time step t for the given context of x1...xt where |V| is the size of the vocabulary
- we have t words in the vocabulary - we can define the vocabulary size a 100 ,300 etc
- D is the dimention of the word vector
- R^D is the dimenstion of W
- R^D*D is the dimention of U which is a result of previous layer
- R^ (|V|*R^D) is the dimention of V
- R^|V| is the dimension of the output layer

## Derivatives of W, V and U
- we have to reduce the error Et inorder to that we have to  find the lowest value of E  then we have to find the derivatives of all these parameters and which is the lowest value of them(local minimum)
- Find out what is the change that we have to make when a error is coming to the variables
- So consider the derivatives of all variable so that we can make a clear idea about how are they working
- Consider the derivative of E   with resepect to V we calculate it with the chain rule of partial derivatives from the E it will calculate the partial derivatives and will multiply each other inorder to get the derivatives
- δoutwill be calculated with the PD(Et,ÿt)*PD(y,zt)
- and PD(zt,V) is called st
- so PD(Et,V) = δout*st
-  Derivative of W is the PD(E,W) since the hidden layer activation depends on the previous time state we have another similar term  δt-1 that get added to ----(9) refer proofs
- deivatives of U is PD(E,U) - since we are propagating the erooro from the current state to the previous state `δnext = σ(ht)Uδout V σ'(ht)`
- δout is the loss for each units in teh output layer
- The error for the entire duration of T for all the vocabulary is the sum of all the erros across the layers - E(θ)---(11)
- This term is also known as perplexity Lower the value of 2^(E(θ)) better is the confidence of the network in predictinf the next word
- Preplexity - nth root of product of 1/(P(wt|wt-1) where n is the window size
## Exploding and vanishing gradient
- `yt = f(U,h)` and we want to propagate the error through backpropagation
- RNN is a good network and It could able to solve many problems that a normal neural network could not solve
- We have some problems - exploring value and it became an Nan and vanishing is when the value when the gradient reduced to very close value to the zero.
- In the calculation the h value depends upong the previous value
- we have to find the derivative of the all of them in the chain rule manner when we calculate the error in back propagation
- while calculating the error in back propagation then we are calculating the the error based the h. We can understand that each calculation is the diagonal matrix creation - jacobian (Jacobian matrix of a vector-valued function in several variables is the matrix of all its first-order partial derivatives.)
- But while the error calculation the diagonal matrix is multiplied with the U matrix which is the history
- If we have many history then the matrix gonna smaller and can't do any updation
- The decay of the gradient value is proportional to the depth of the network. The deeper the net network , the chance of getting a smaller value of the gradient towards the fag end of the back propagation
- **Gradient Clipping** : The gradient is either very large(larger than 1) or very small. This can cause the optimizer to converge
- To speed up training clip the gradient at certain values
- Clip the gradient if it exceeds a threshold 
## Truncated BPTT
- For applications with long sequence the input is truncated into managable fixed- sized segments. This approach is called Truncated Backpropagation through time 
- Using RNN it is possible to create some sequence of character that really makes sense

## Gated recurrent unit (GTU
If the reset gate value --> 0, previous memory states are faded and new information is stored. If the zt is close to 1, the information is copied and retained thereby adjusting the gradient to be alive for the next time step, thereby long-term dependency is stored. BPTT decides the learning of the reset and update gate

