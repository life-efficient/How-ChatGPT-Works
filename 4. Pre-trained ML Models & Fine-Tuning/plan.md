## intro to huggingface

- show pre-trained models

## using a pre-trained image classification model

- previous mistake I've made, not specifying pretrained = True!

## Fine-tuning

- much of what models have learnt can be re-used
- the end-layers of the network contain high level representations useful to your task

- we might call these _embeddings_

- you want to take these high level representations as inputs, hopefully to a smaller model

- it's critical to throw away the last layer, instead of building on top of it

## TODO image

- the last layer has learnt to throw away any information not relevant to the task it was originally trained on
- if you want to build a plane classifier built on resnet, then every output of resnet will be the same - high probability on the plane category, but no information about other features

## TODO image

### Weight freezing

### Disriminative learning rates

## Where are we on the map of our journey to ChatGPT?
