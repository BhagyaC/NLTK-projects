### Out of vocabulary

- In a closed vocabulary language model , there is no unknown words or out of vocabulary words
- In an open vocabulary system you may find new words that are not present in the trained model
- pick some words which are below frequency and replace them as OOV
- Treat  OOV as a regular word
- During testing the new words would be treated as OOV and the corresponding frequency will used for computation 
- This will eliminate the zero probability for the sentences cotaining OOV
