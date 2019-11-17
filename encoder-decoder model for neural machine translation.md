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
