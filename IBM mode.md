# IBM Model 1
- IBM models are statistical machine translation models. They learn the model parameter by using bilingual corpus. The were part of many SMT system for more than 20 years
- Lexical translation model (word2word)
- Alignemnt decision are independent - they doesnot give any importance to the context - that is any words before and after is not confirmed
- All alignments are equally likely
- The length of source language sentence is fixed,m
- More than one surce language word f can be aligned to a single target langauge word
- we are using phrase base model now

## IBM model translation probability
- english sentence - e1,e2,e3..
- French sentence - f1,f2,f3
- a = {a1,a2,a3..}
- alignment indacates that from which english word each french word originated from each alignment
- Estimate the traslation probability P(f,a|e,m) = P(a|e,m) * P(f|a,e,m)
- where P(a|e,m) is the probability distribution of possible alignments
- P(f|e,m) = Σ P(f,a|e,m) = Σ P(a|e,m) * P(f|a,e,m)
- Find teh alignment - P(a|e,m) = 1/(1+n)^m
- Find the french word alignment probability given the alignment variable, English word and fixed length of french sentence 
- Find the most probable alignment variable for every pair of e and f the above equation

## IBM model training
- If the alignments are known then it is possible to estimate the translation probabilities by counting the aligned words
- If the translation probabilities are known then it is possible to esimate the alignments
- We do not know both - Incomplete data
- Hence iterative approach with refinement of these values over time is used 
- If we had complete data would could estimate model
- If we had the model we could fill in the missing information
- To solve this incomplete problem we use expectation maximization algorithm 
- Initialize model parameters equally likely
- Assign probabilities to the missing data
- Estimate model parameters from completed data
- Iterate steps 2-3 until convergence
- Alignments are equally likely means the word in english and words in french are connected to all words in the french
- As we moves along with the iterations we can understand that some connection are only valid
- At the end we will have a decorder with the probability of the e and f|e it will decode everything
# IBM model 2
- The conditional probability P(f,a|e,m) will be taken for redefinition
- IBM model 2 = IBM model q + distortion parameter
- A new parameter distortion parameter q(j|i,n,m) is introduced in the computation of P(a|e,m)
- `q(j|i,n,m)` is the probability of alignment variable ai taking the value j conditioned on the length n and m and length n and m of the english and french sentence respectively
and iΕ(1,m) j Ε {0,m}
- The two parameters of the alignment model are defined as 
- The conditional probability of generating a french word fj given the english word ej - t(fj|ej) where n and m are the lengths of the English and french sentence respectively
- q(j|i,n,m) is the probability of alignment variable ai, taking the value j conditioned on the length n and m of the english and french sentences resepectively
- Check the proof and then we can understand that it will index the all sentences decoded and then pick up the one with the maximum probability
- If we know the parameters q and t it is easy to find the most probable alignment sequence a for any pair of french and english sentence
- we calculate the argmax of product of distortion parameter and transition function
- There are many model available
- There other models that improve that improve the translation probability. These model are no longer used but they are used in state of the art of NMT models
- To estimate the lexical probability t(f|e)
- To derive alignments
## Statistical machine translation
- The translation model represents the probable word translation. The language model encode the generative model that compute the sentence confidence in terms of probability.
- The decorder searches for the most likely target word sequence form a large amount of hypotheses using these two models

### Phrase based translation system
- A phrase based translation system can consider inputs and outputs in terms of sequence of phrase and can handle more complex syntaxes than word- based systems. However long-term dependencies are still difficult to capture in phrase based systems
- Till early 2000 IBM models were used and after that upto 2014 we used the early neural network and then the advanced concepts are used
