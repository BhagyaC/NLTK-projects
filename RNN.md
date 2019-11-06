# ANN as a LM limitations
-  We can use the ANN to predict a next word like we used it before
- It will have a weight embedding and weight context and it will get updated and the highest probable value will get when the error is reduced
- Now we can add the word and continue the event but now we have to improve all the weight 
-  The main limitation is that the input layer size is fixed and static
- the embedding are learned on the small local window surrounded by it if the small local window contains opposite words like good and bad it may not perform well
- It did not address polysemy
- It does not consider the frequency of the words form the vocabulary
- can't understand phrases
- can we encode a sentence as a distributed vector
- can't consider the paragraph
- memory is less and we don't consider where the word and context come from
-  It can't handle variable text length
- The sequence of data is important like time series

## Sequence learning and its application
- It is a study of machine learning algorithms designed for application that need sequential data or temporal data
- applications are NER, Paraphrase detection, Language generation, Machine translation, speech recognition, spell checking, predictive typing, chatbot/dialog understanding, generate or correct the handwritten text

- Sequential learning is considered as a key problem in machine learning and artifical intelligence
- Then likelyhood of any sentence is can be determined from everyday use of language, The earlier use of words is improtant to predict the next word and sentence in the  paragraph or chapter
- If a word occurs twice in a sentence but could not be accompanied in the slicing window then the word will be learned twice
- An architecture that doesnot impose a fixed-length limit on the prior context
- states are really important in learning  excercise
- The previous state definetly affect the next states
- In order to use the previous state we need to store it or remember it
- Traditional Neural networks were not designed as a state machine as anything outside the context window had no impact on the decision being made
- Traditional Neural network do not accept arbitary input length
- Inherent ability to model sequential input 
- It uses own output as input
- RNN encode not only the attributional similarity between the words also between pairs of words item analogy chennai - tamil etc
- The change is the loop in the hidden layer
- The weights from the hidden layer are stored - that is when a new stated comes from the hidden layer the previous state Ht-1 will be also send it along with it.
-  The state of the previous state that is Ht-1 is connected to the Ht with another set of weights called U
- from the start of the sentence with no imposition of the window  size
- The hidden weights U from the previous time stamp ht-1 is the significant addition to RNN
- The past weights from the previous time stamp determines memory of the network
-              ``` |-------yt------|
                      |         |
                      |    V    |
                      |         |    
                   |-------ht------|\     \
                      |         |     \  U  \
                      |    W    |     |------ht-1-----|
                      |         |
                   |------xt-------|
                   ```
 - `ht = f(Uht-1 + Wxt)`
 -  we can use softmax or hierarchial softmax for optimization
 ## Multiple neural network classification
 - One to one - classification
 - one to many - image captioning and image description
 - many to one - Sentiment analysis
 - many to many - machine translation
 - many to many synced sequence input and output frame by frame labeling
 - There are many method and variation that can be applied to the RNN
 
## Urolled RNN
- for x0 there will be h0 and y0
- for xi there will be h1 and input from h0 and y1 and so on upto hn 
- we can unroll the rnn through time along with the previous value stored

## RNN based language model
- 
