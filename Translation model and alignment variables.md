# Translation model (continuation from bayes model)
- p(f|e) is the chance that upon seeing e, a translator will produce f
- In simple terms translating from french to english is to identify the bag of words in english and later form syntatically correct sentence
- In this model , there is no need to use any french to English translated corpus to train the language model
## How can we translate
- we are just framing the sentence again not by a step by step method
- P(f1,f2,..|e1,e2,..)
- By fixing the size of the french sentence to m words we will assume that there is some distribution P(m|n) that model the conditional distribution of french sentence length m
- Now we can use the conditional probability of the french sentence is conditioned on the English words of length n and the french sentence of length m
- It is very difficult to estimate all the probability so we introduced a concept like allignment
## Alignment variables
- It is hard to esimate P(f|e,m) directly let us introduce the concept of alignment variables
- Consider a seed word in english that starts the traslation process
- Assume this seed word, aj as the alignment word at the position jth in the english sentence
- The alignment a is {a1,a2..am}
- The possible allignments are n+1^m
- The idea is to find the most likely alignment
- Alignment probability depends on position of the words and position relative to neighbours
- The likelyhood of an alignment depends on how many words align to a certain position
- Automatic alignment is the backborn of SMT(stastistical machine traslation)
- **Bijective alignment**
- Every word in each text is coupled to exactly one words in the other text
- No words remains uncoupled or left out
- There are another representation of alignments using matriz representation
- the alignment set length will be input langauge vocabulary
- Insertion - a null token is inserted if the target language does not have the equvalent source of language word
- One2many - A source word may translated into more than one target word
- many2one - many source words translate into one target word
- The alignment table is filled with the conditional probability other than putting zero
