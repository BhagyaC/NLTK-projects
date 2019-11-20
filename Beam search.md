# Beam search
- It is a heuristic search algorithm that selects a few candidate hypothesis from |v|. It reduce memory requirement by using only a M <|V| candidate using a score
- Maintain K candidates / hypothesis at each time step - Ct = (x11...xt1)....(x1m...xtm)
- compute ct+1 by expanding ct and keeping the best M candidate 
- C = U ct-1
- Typical beam width of size 5-10 used in NMT. The BLUE scores computed using Beam search using B= 5-10 are comparable
- If the beam width is 3 then at a time 3 words are considered (most frequent 3) from all the derivatives
- When the end of sentence come we will back track to the initial word and create the entire sentence
- Use al possible partial translation exhaustive search 
- beam size , b=1 greedy search -words are predicted util the <EOS> is found 
- b>1 several hypothesis
- Each hypothesis will have a translation
- The length of all hypothesis my not the same
- We could use different termination conditions fixed time step , compute until <EOS> is reached for hypothesis
- Use either log probability or product of conditional probability to find the scores for each hypothesis that maximizes 
# Varients of gradient descend
- stochastic gradient - present one sentence and start learning process then calculate the j(theta) using BPTT that is for every sentence
- batch - instead of every sentence we are using a batch of sentences
- mini- batch - the batch consider all the pairs where mini batch is the subset of the batch
