## Vector space model 

### 2D vector space

- 2D vector space is defined as a sert of linearly independent basis vectors with 2 axes each axis correspond to a dimension in the vector-space
- normal x/y axis
### 3D vector space model 

- 3 axis will be there 

- Let us assume that the words in a corpus are considered as linearly independent basis vectors
- If a corpus contain v they are linearly independent
- every words in R will have a position in space
- emma corpus 7079 axis in that

- If terms are represented as axises 
- Vector space models are used to represent words in a continuous vector space R
- Then how to represent the document
- Combination of term represent the document vector in the vector space
- It will create the very high dimensional space

### Document similarity

-  If we have a TF-IDF table given then we have to find out which of the documents are similar in nature
- **Wieghted TF-IDF** is defined as 1+ log(tf) where tf>0 else 0 

**Query modeling**
-if someone ask for some terms in the document then the query is generated as a vector then find the document which is similar to the query model
- The relevancy ranking of the document is depends on the distance of the document with respect to the query
- The proximity of the query with every document is computed using distance measure

- If we are using a binary incident matrix then the query is returend a set of document whether the query keywords were found in documents or absent 
- It did not give any ranking for the retrieved document.
- A similarity measure is a real- valued function that quantifies the similarity between two objects
- The examples are
- Euclidean distance
- Cosine simialarity 
- Cluster similarity 
- Jaccard similarity
- The length of the vector is too much and we are using the distance then it will not give a good result
- The cosine distance is normalized correlation coefficient
- And the proximity score is listed in the descending order and the documents within a predefines proximity score(angle) will be considered as relevent and retrieved
 
 
-  Inverted index with a posting which will indicate the all document which is the term is present so that it reduce the computation to find the term in the document
- 
