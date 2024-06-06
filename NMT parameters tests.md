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

# Starting Moryossef config

Max BLEU score at checkpoint 4000: 46.925377943549236

## Hyperparameters that will be examined

| Parameters examined | Standard value |
| ------------------- | -------------- |
| Layers              | 2              |
| RNN size            | 512            |
| word_vec size       | 512            |
| hidden size         | 512            |
| learning rate       | 0.5            |
| transformer_ff      | 2048           |

### Layers

| Layers | Score                                                 |
| ------ | ----------------------------------------------------- |
| 1      | Max BLEU score at checkpoint 4000: 46.227239136800755 |
| 2      | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| 3      | Max BLEU score at checkpoint 3600: 47.71098576695772  |

### RNN size

| RNN size | Score                                                 |
| -------- | ----------------------------------------------------- |
| 256      | Max BLEU score at checkpoint 3800: 48.51555813877618  |
| 512      | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| 1024     | Max BLEU score at checkpoint 3000: 45.8691732240156   |

### Wordvec size and hidden size

| Wordvec size | Score                                                 |
| ------------ | ----------------------------------------------------- |
| 256          | Max BLEU score at checkpoint 3000: 46.3655821896654   |
| 512          | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| 1024         | Max BLEU score at checkpoint 3000: 48.54754192671245  |

### Learning rate

| Learning rate | Score                                                 |
| ------------- | ----------------------------------------------------- |
| 0.1           | Max BLEU score at checkpoint 3400: 45.60678699845643  |
| 0.5           | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| 0.7           | Max BLEU score at checkpoint 2000: 47.38314049153926  |

### Transformer_ff

| Transformer_ff | Score                                                 |
| -------------- | ----------------------------------------------------- |
| 1024           | Max BLEU score at checkpoint 3200: 46.925094671833754 |
| 2048           | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| 4096           | Max BLEU score at checkpoint 1800: 47.19788279291931  |

### Pretrained embeddings

| Used embeddings | Score                                                 |
| --------------- | ----------------------------------------------------- |
| None            | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| Source          |                                                       |
| Target          | Max BLEU score at checkpoint 3000: 47.29576855897429  |
| Both            |                                                       |
