# Phrase based model
- Instead of one word we are considering more than one word at a time
- Still the long term dependencies are still difficult in phrase based systems
- we use a noisy- channel model
- Use phrases (contiguous subsequence of sentence or a span of tokens) as the atomic unit - not to be confused with the lingustics phrases
- Four stages 1. Use IBM model to align 2.Phrase to Phrase align words, 3. Extraction of  phrases 4.Construction phrase probability
### Definitions
- Let e be the target language and f be the foreign language. Let ei be the ith word and fj be the jth word for e,f respectively
- ê = argmaxP(e)t(f|e)
- argmax is a search operation to predict the english sentence with the highest probability
- Many to many translation possible can handle non compositional phrases and idioms
- Use of local context - using nearest neighbours
- The number words in the phrase may dictate the correct word order
- If the learned phrases are longer , the whole sentence is translated
### Heurisitics for growing alignments
- To insert new alignment point , search for the alignment points in P(e|f)UP(f|e) alignments
- If not available in (1), do not fill alignment points
- Check for the points that are not aligned already 
- Start filing the diagonal neighbors and adjacent points
- from the alignment model with union and intersectin the phrases can be listed out and we have to find which among them should be calculated or not
