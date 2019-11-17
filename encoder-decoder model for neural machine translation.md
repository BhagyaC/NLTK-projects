# Neural machine translation
- Neural machine translation is the mechanism of modeling the machine translation process using artificial neural network
- We could consider translation as a sequence with the source and the destination sentences appearing in a time series.
- The words within E,F appear in different time (t11,t12,t13 ...t1n) and (t21,t22,t23...t2m) respectively
- Unlike the phrase based SMT models, NMT attempts to build and train a single , large neural network that reads a sentence and outputs a correct translation
## Encoder-Decoder model
- encoder and decoder is RNN models
- The encoder will encode the source sentence
- All sentences of varying length are encoded into fixed sized vectors
- Uses fraction of the memory needed by traditional SMT model
- Performance of this model decreases as the length of a source sentence increases
- Uses RNN for both encoding and decoding 
- Encoder maps the variable length sentence into a fixed length vector
- Decoder translates the vector representation back to a variable length target sequence
- Two network are trained jointly to maximize the conditional probability of the target sentence , given the source sentence
- This model learns a continuous space representation of a phrase that preserves both the sematics and syntatic structure of the phrase
- the encoded vector is called context vector
# RNN based machine translation
- Input units - variable length source sequence x= (x1, x2 , x3 ..xt)
- Output units - variable lenght target output y = (y1,y2,y3 ...yt)
- Hidden units for each input state ht = f(ht-1 .x) where f is a simple non - linear activation function(sigmoid or tanh) or a complex LSTM and GRU cell
- RNN is trained to predict the next word in the sequence or RNN learn a probability distribution over a sequence 
- The output at each time step t = p(xt|xt-1....x1)
- The output distribution softmaz layer size is equal to the size of the vocabulary  V at every input
- Then p(x) =  Π p(xt|xt-q...x1)
### Encoder
- RNN learns to map an input sentence of variable length into a fixed dimentional vector representation
- It learn to decode a fixed length vector representation back into a variable length sequence
- This model learns to predict a sequence given a sequence p(y1,y2,...yt|x1,x2...xt)
- Encoder reads every in x sequentially 
- C is the summary of the hidden state at time T and had encoded all the symbols in the  sequence
### Decoder
- This is another RNN
- This is trained to predict the next symbol yt and generate the output sequence given the previous state ht
- yt and ht are conditioned on the summary from the encoder , C and its previos hidden state 
- Decoder 's hidden state is given by  ht = f(ht-1,yt-1,C)
- Conditional distribution for the next symbol is P(yt|yt-1,yt-2 .. y1,C) = g(ht-1,yt-1,C)
### Estimating model parameters
- Both encoder and decoder are jointly trained to maximize the conditional likelihood 
- J(θ) = max 1/n log pθ (yn|xn)
- where θ is the set of model parameters (all weights) that will be learned during BPTT and (xn,yn) is the source sentence sequence and target sequence pair
- go throught the BPTT derivation
- inorder to avoid the exploding the gradient problem we can use clipping to avoid the vanishig gradient problem we have to use some other method like GRU there is a new hidden acivation cell where there is a reset and forget gate which will indicate that the word have to retained and the new hidden state value is calculated as the result of both update gate and reset gate
- If the r is apporx 0 then the hidden state value is reset with current input 
- Update gate controls how much information from the previous hidden state will carry over to the current hidden state 
- Units that learn to capture short-term dependencies will tend to have reset gates that are frequently active
- Those units that capture long term dependencies will have update gates active most of the time
