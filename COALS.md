# Correlated Occurance Analouge to Lexical semantics - COALS
- Rhode et al "An improved model of semantic similarity based on lexical co -occurance" - 2006
- Gather co-occurance counts typically ignoring closed class neighbors and using a ramped size 4 window
- Discard all but the m columns reflectinf the most common open-class words
- Convert counts to word pair correlations - Instead of using the raw frequency score correlation score is used to analyze the relationship  between pair of words 
- Set negative values to 0 and take square roots of positive ones.
- The semantic similarity between two words is given by the correlation of their vectors. The correlation coefficient values with this normalization will be in the range of [-1,1]
- The matrix constructed using this correlation would be semantic space in HAL high frequency neighbours have undue influence on the scores. COALD method employs a normalization strategy thath largely factors our lexical frequency. Columns representing low frequency word are removed
- It is one direction while considering the matrix - then take the correlation of the values
- The majority of the correlations are negative
- word with negative correlations do not contribute well to finding the similarity thatn the ones with positive correlation
- Closed class words convey syntactic information than semantic - could be removed from the correlation table
- More complex than HAL
- The major diff with CBOw and skip gram is that they are supervised and LSI HAL COALS are unsupervised with cooccurance where the word2vec model never considered the cooccurance

