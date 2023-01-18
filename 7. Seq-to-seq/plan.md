
Alignment is the correspondence between particular words in the translated sentence pair
Arrows between parts of pair entences
- Some words have no counterpart
- Some go many to one
- Some go one to many
- many to many

Can we learn these alignments and decode part by part?
Alignments, a, are latent variables

the most likely translation is argmax_yP(x|y)P(y)
We cannot possibly enumerate over all possible translations 
Decoding is the process of 
you can be guided by a language model as you go along, which gives you P(y)

Neural Machine Translation (NMT) is a way to do Machine Translation witha single end-to-end network

The decoder is a language model who's output is the target sentence, conditioned on the encoder encoding

Seq-to-seq can be used for many NLP tasks
- Summarisation
- dialogue
- parsing
- code generation
- music generation

The key idea with seq to seq is a conditional language model

The entire thing is optimised end-to-end

You can also have deep seq-to-seq models

# TODO diagram

Without skip connections, LSTMs seem to work best with 2 or 3 layers

Greedy decoding vs exhaustive search decoding vs beam search decoding

BLEU
- n-gram prcision
- plus a penalty for too-short system translations


## Where are we on the map of our journey to ChatGPT?
