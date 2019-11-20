## Advantages of attention
- Ability to focus on significant part of the sentence
- Ability to peek into source sentence
- Reduce the problem of vanishing problem
- Alignments are found automatically - no need to train 
- Improve NMT performance for alignment
## Types of NMT
- 1 encoder 1 decoder
- multi encoder 1 shared decoder
- shared encoder multiple decoder

## NMT from google - zero shot translation
- Moved away from maintaining seq2seq model for every pair of language
- A single system that translates between any two languages even in the absence of the training  corpus for these two language
- Assume that only example of Japanese- English and Korean- English translation are available google found that the multilingual NMT system trained on this data could acually generate reasonable Japanese- Korean translation
-  Is it trained create the interlingua?

