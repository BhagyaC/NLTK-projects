# NLTK-projects
basics projects on NLTK

OS:MAC

install nltk
http://www.nltk.org/install.html

if facing any issue in installing

pip install --upgrade setuptools --user python


# Probability in NLP
1.It provide  a method to select the next word in the sequece of sample data.
2.If there is an uncertainity in the data it helps to make a informed decision.
3.It gives  a quantitative description on the chances and likely hood between the data.
4. Probability of the sentence - whether the sentence in the corpus or not
5.Probability of next word in the sentence.

## Vector space models

How to do the mathematical operations on the text?
Let us assume that the text in the corpus is cinsidered as the linearly independent vectors .If a corpus consist on N number of words which are linearly independent, then every word represent an axis in the contineous vector space R.

Each word takes an independent axis which is orthagonal to other words
But we need to reduce the number of axes so that the number of variable must be reduced so that we have less number of variables to deal with.
We have to create the sematically connected vectors (model that discovers and uncovers the semantic relation between words)

### Why dense vectors
Sparse matrix are too long and not convinient for machine learning concepts.
Dense matrix are capable of capturing the synonyms of the neighbouring words.

### Word embeddings
The words will have a numeric representation which reflect the sematic and syntatic similarity.

**word is known by company it keeps -John Rupert Firth**
