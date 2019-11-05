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
- applications - NER, Paraphrase detection, Language generation, Machine translation, speech recognition, spell checking, predictive typing, chatbot/dialog understanding, generate or correct the handwritten text
