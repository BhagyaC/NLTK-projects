
# Blooming taxonomy
- creative - machine translation
- analysis - The predition at Lm for next word
- application/apply - word embedding
- understanding - conceptual understanding - stemming
- Remember - search

# Attention based machine translation
## RNN with alignment
- The objective of attention is to capture the information from the passage token that relevent to the content of translation - Other than passing the long entire sentence which will create a gradient problem we should spit them to parts and then feed to the network
- Different parts of an input have different levels of significance
- Different parts of the output may even consider different parts of the input as important
- The purpose of the attention mechanism is to let the decoder peek at the relevant information encapsualting the passage and the question as it generates the answer
- Attention mechanism provides the decoder network with the entire input sequence at every decoding step, the decoder can then decide what input words are important at any point in time
- The attention based model learns to assign significance to different parts of the input for each step of the output
- In the context of translation, attention can be thought og as alignment
- Bahdanau et al argue that the attention scores αij at decoding step i signify the words in the source sentence that align with words i in the target word
- We can use attention score to build an alignment table. It is a table mapping of words in the source to corresponding words in the target sentence - based on learned encoder and decoder from our seq2seq NMT system

# Research Paper - Neural machine translation by jointly learning to align and translate
## BAHDANAU ET AL NMT MODEL
- Input is a sequence of words x1,x2 ...xn target sentence is again a sequence of words y1,y2...ym
- Let (h1,...hn) be the hidden vector representing the input sentence. These vectors are the output of bi-LSTM /bi-GRU for instance and capture contextual representation of each word in the sentence
## Decoder 
- The hidden states si of the decoder are computed using a recursive formula of the form si = f(si-1,yi-1,ci) where si-1 is the previous hidden vecotr yi-1 is the generated word at the previous step and ci is a context vector that capture the context from the original sentence that is relevant to the time step i of the decoder
- The bi LSTM is nothing but a a two later lstm inter connected where one layer will learn from left to right and one will learn from right to left
- The resultant will output from the layer and then the weighted value with the result from the decoder is selected and given to the s state
### NMT with attention 
- Conditional probability for each output neuron 
- P(yi|y1,y2...,x) = g(yi-1,si,ci)
- Where si if the RNN hidden neuron at time i and si = f(si-1,yi-1,ci)
- The context vector ci depends on the sequence of annotation (h1,h2,...htx). Each hi contains information about every word with a strong focus on context words surrounding the ith word of the input sequence.
- The context vector ci is computed as the weighted sum of these annotation hi
- ci = Σ αijhj - the weighted sum of the alpha and the values from the hidden state
- αij of each annotation hj is computed by 
- αij - exp(eij)/ Σ exp(eik) - the soft max of all values from eij (which is a dot product of e vector and state form the previous hidden layer)
- Where eij = a(si-1,hi) - previous decoder value and current hidden state value
- The encoder is trying to figure out which word is align to next one at a particular time slot
- During the training we will get the alignment matrix in the right form
- For each word we will predict the next word and the and will feed the the word as the next word and for each word the j(θ) and the error calculated and will be reduced while training
- the eij = a (si-1,hj)
- It is the alignment model this learn how well the inputs surrounding position j and the output at position i match
- The alignment is explicitly computed and not latent
- This alignment model is also trained along with the translation model
- αij is the probability that the target word yi is aligned to the source xj 
- ci is the expcted annotation over all possible annotations αij 
- αij or eij reflects the importance of the annotation hj wrt to the previous hidden sate si-1 of the target. This enables the next state si to generate yi
- The decoder decides which part of the input is important to generate yi 
- The decoder decides which part of the input is important to generate a respective translation rather than depending on the encoded vector of the entire sentence
- Decoder has control over the input sequence and selectively learns to align words/phrases automatically
### Translation with local attension
- consider a small part of the input at a given time slot
