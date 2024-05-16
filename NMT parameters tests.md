| Train steps | Embeddings? | Enc-dec layers | Enc-dec types | Wordvec size | Optim | Learning rate |     | **BLEU**                  |
| ----------- | ----------- | -------------- | ------------- | ------------ | ----- | ------------- | --- | ------------------------- |
| 5000        | No          | 4              | Seq2seq       | 512          | SGD   | 1             |     | 21                        |
| 5000        | No          | 2              | Seq2seq       | 512          | SGD   | 1             |     | 25.096556862119098        |
| 5000        | No          | 2              | Seq2seq       | 100          | SGD   | 1             |     | 27.70303931529561 (retry) |
| 5000        | No          | 2              | Seq2seq       | 100          | Adam  | 0.001         |     | 27.127219600063004        |
| 5000        | No          | 2              | Seq2seq       | 100          | Adam  | 0.0001        |     | **29.12208860911118**     |
| 7000        | No          | 2              | Seq2seq       | 100          | Adam  | 0.0001        |     | 24.39660783311091         |
| 5000        | No          | 2              | Transformer   | 100          | Adam  | 0.0001        |     | 32.77601479338147         |

With embeddings: ~39!!!
Moryossef config:
