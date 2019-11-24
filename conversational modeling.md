# Conversational modeling
### Types of conversation
- Threaded - twitter , facebook
- Task oriented - google assistant , siri
- short - text - google help desk
- chit- chat or open conversation
- question answering
## Introductin
- Modeling conversation is one of the active research problem in AI
- Natural language conversation involves language understanding reasoning and the utilization of common sense knowledge 
- The goal is to build a conversational model that generates the respones automatically and these responses are liguistically indistiguishable from human responses thereby passing the turing test
- Understanding what NOT said
- Analysis of the language beyond the sentence 
- Identification of the relationship between the context across the sentence
- Two part - representation and condition (KB)
- and also relationship
## Few examples in conversational modeling
### ELIZA - earlier one 
- It's perl code
-  It is written using regular expression and deletion insertion codes
- It does not consider the context of the dataset
## Ideas to implement - CM
- Retrieval based method - Pick suitabl response based on how many times a particular response was selected for similar question, or using the matching feature of the question and the response
- Statistical machine translation approach - This approach treats this as a translation problem inwhich the model is trained on  the parallel corpus of question and response pairs

### IR based conversation 
- IR based mostly used in the short-text conversation 
- The corpus containsts different pairs of post-comments or question answers
- given a question  and the ser of documents the task is to find the answers from the span if text  from extracted paragraphs
- For every given query  q there could be zero or more post-comment pairs (p,r) The best response to the query q is picked up based on the ranks of the retrieved.
- pairs using r = argmax.score(q,(p,r)) whre score() is the sum or all score of the features 
- score(q,(p,r)) = ΣwiΦi(q,r)
- where Φ() and wi are the core and weight of the ith feature and Ω  is the total number of features respectively . Here the features could be TF*IDF of the word found in {q,(p,r)}

## Question answering
- An application of short post- response is question answering system, such as IBM watson (Jeopardy)
- In this case most of the candidate responses are answers factoid questions
- Open domain question answering has become important research are in natural language processing
- Tougher than common search engine tasks
- Finding accurate and consise answers to questions rather than a set of relevant document
- Simple term based retrieval won't be enough
- Type of the sought after answer should be known to retrieve accurate answers
In the qustion answering model the question along with the paragraph which is retrieved based on the similarity are encoded then in the word embeddings
- The exact question word matched and token features like POS, NER are noted
- Alignment of the qustion embedding also considered(attention)
- Then RelU is used to extract the exact match
- In a qa system we have a question and answer module -question module encodes the questionand the answer module will encode the paragraph and using the attension and the question embedding predict the span of answer

