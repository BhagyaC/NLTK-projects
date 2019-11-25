# The GLOVE model
- The globel vector models the word vectors with the computed statistics of the co-occurance count
- The authors of this model introduce the idea that the **co-occurance ration** between two words im a context are strongly connected to the meaning
- Let X represent the counts of the co-occurance matrix . Every element of Xij represent the number of times the word j occurs in the context of word i
- Let Xi = Σ  Xik be the number of times any word appears in the context of word i
- Let Pij = P(j|i) = Xij/Xi be the probability that word j appear in the context of word i 
- The skip gram model captures the co-occurance patterns one window at a time while the glove captures it using the statistics of the co-occurance or how oftem the pattern occur together
- Since the ratio Pik/Pjk depends of i,j,k. It can be modeled by F(wi,wj,wk) There could be several possible way to encode the ratio. We would like to estimate the parameters of this model given the ration
- Using factorial approach similar to LSA the new weighted least square regression model is proposed that minimizes th cost function
- There is a J(θ) which has to be reduced/ minimize it over time - a cost function
- corpus is selected
- initial learning rate - 0.5
- context word to left and right is 10 each
- Generates two words vectors W and W' the final word vector is W+W'

# Evaluation of word vectors
## Evaluation of word embeddings
- There are two type of evaluation
- Intrinsic Evaluation - word embeddings are compared with human judgements on words relations
- Extrinsic evaluation - traditionally judged by its utility in downstream NLP tasks. The performance of the word embedding is measured indereclty by the performance of the down stream applicaiton
### Intrinsic evaluation
- Evaluate word vector representation quality by judging the similarity of representations assigned to similar words by humans
- The most popular evaluation sets at present consist of words parirs with similarity rating produced by human annotators . Use a correlation method to compare word vectors using common words
- If the correlation score is higher then the word vector quality is good
- N be the number of common words in the word embedding
- Let X Ε  R d*n {word vector dimension }be the word vector matrix and let xj Ε R 1*n be the word vector. D denoted the word vector dimension
- Let S Ε  R p*n be the linguistic property matrix. Let sj Ε R 1*N be the liguistic property vector for a word . P denotes liguistic properties obtained from a manually annotated liguistic resources
- Let A Ε {0,1}d*p be the matrix of alignments such that aij = 1 iff xi is aligned to sj, otherwise aij = 0. If r(xi,sj) is the pearson's corelationbeween vectors xi and sj then our quality of word vector is defined as
- Q = max ΣΣr(XI,SJ)*aij
