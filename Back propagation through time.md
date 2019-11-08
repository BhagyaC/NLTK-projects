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
