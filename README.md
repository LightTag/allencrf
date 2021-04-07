#AllenCRF
A full features CRF for PyTorch extracted from the [AllenNLP Framework](https://github.com/allenai/allennlp)

## Docs
See the AllenNLP [documentation about CRF](https://docs.allennlp.org/main/api/modules/conditional_random_field/)
for full API docs.
 
## Why
The CRF implementation in the AllenNLP framework is very good and easy to use. It notably has a convenient API
for specifying allowed (and thus forbidden) transitions. 

We extracted the CRF implementation from the framework, so that we can use it without the other dependencies 
that AllenNLP includes.

 ## Credits
 The [original implementation](https://github.com/allenai/allennlp/pull/343) was written by [Joel Grus](https://github.com/joelgrus)
 with ongoing work from the good folks at AllenNLP. 
 
 