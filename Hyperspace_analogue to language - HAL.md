# Hyperspacd analogue to language - HAL
### Summary of word2vec
- Uses skip-gram and CBOW models to build distributed word vectors
- Optimizes computations using sub-sampling negative sampling and Hierarchical softmax at the output   layer
- Uses co-occurance words, but ignore the frequency of co-occurance words
- context is within the chosen widow size
- the model like LSA, HAL, COALS, and GLOVE consider the co-occurance frequency as well
### Constructing sematice models
- Semantic space are constructed by selecting an axis Use human judgment to place words in each axis.
- To place a set of desirable words, one must choose the axis and find a ser of words that must be confined to the chosen axis
- In a size axis placing ant and mountain 
- can we use lexical co-occurance to construct semantic spaces
- Is it possible to construct high dimensional distributed semantics spaces automatically 
## Hyperspace analouge to language - HAL
- A window size n. representing a span of words is used words within the window(or ramped window) are recorded 
- The strength of co-occurance is computed using a inverse relationship with respect to the word in question wi
-  Cs proportional 1/N where Cs is the co-occurance strength and N is the number of words separating them
- A word wj immediately occuring next  to wi will have a higher value than the word wj seperated by a distance of n from it
- The co-occurance word strength are distance and direction sensitive
- A term - term matrix is constructed with every cell representing summed co-occurance counts for a single word pair
- If the word have similar values in the same dimensions, they will be closer together in the space meaning they share similar context
- The word vectors closest to a given word are considered its neighbors
- The matrix of the sentence is created such as the rows - count from right to left
- columns - count from left to right
- Pick up a test that contains conversational text , variety of topics to cover all type of co-occurance
- 160 million words from usenet news groups window size = 20
- A word appearing with a frequency of 50 or more is considered as a vocabulary item
- 20 target words selected at random from middle frequency words using zipf's law to eliminate most common and rare words
- for each target word, a normalized euclidean distance was computed from the word to each vocabulary item
- The neighbors with the smallest distance is shown in Table 
- These relationships appear to be both semantic and associative
- The high dimensional neighbourhood surrounding each word is simialr to a semantic field
- read paper - Lund, K & Burgees C producing high dimensional semantic spaces from lexical co-occurance Behaviour Research Methods , Instruments & Computers
- HAL capture information about the word meaning throught the unsupervised analysis of the text
- This produces word vectors that are more semantic (similar words) than associative in nature
- HAL acquires word meaning as a function of keeping track of how words are used in context
- The term- term co-occurance matrix carries the history of the contextual experience by using a moving window and weighting of co-occurance words based on the distance
- HAL exploints the regularities of language such that conceptual generalization can be captured in a data matrix
