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

| Wordvec and hidden size | Score                                                 |
| ----------------------- | ----------------------------------------------------- |
| 256                     | Max BLEU score at checkpoint 3000: 46.3655821896654   |
| 512                     | Max BLEU score at checkpoint 4000: 46.925377943549236 |
| 1024                    | Max BLEU score at checkpoint 3000: 48.54754192671245  |

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
| Source          | Max BLEU score at checkpoint 2400: 46.37989905439381  |
| Target          | Max BLEU score at checkpoint 3000: 47.29576855897429  |
| Both            | Max BLEU score at checkpoint 3000: 45.60755607560462  |

### Model with optimal values found

Max BLEU score at checkpoint 2800: 48.565728711401825

## Data Augmentation

### Combined General Tatoeba

Max BLEU score at checkpoint 3800: 35.40834735121386
Max METEOR score at checkpoint 5000: 50.24867201589785

Max BLEU score at checkpoint 5000: 31.7002538153255
Max METEOR score at checkpoint 7600: 53.25140228551314

### Combined LSC Tatoeba

Max BLEU score at checkpoint 4400: 34.48675623737426
Max METEOR score at checkpoint 3000: 45.6154847897087

Max BLEU score at checkpoint 8800: 29.130937085528917
Max METEOR score at checkpoint 9200: 52.78091073430101

### Combined General AnCora

Max BLEU score at checkpoint 4800: 34.28713992236381
Max METEOR score at checkpoint 2800: 56.723110230413674

Max BLEU score at checkpoint 6400: 36.39769329471602
Max METEOR score at checkpoint 7200: 54.5368140068245

### Combined LSC AnCora

Max BLEU score at checkpoint 4600: 36.393473162000085
Max METEOR score at checkpoint 3200: 54.96719736589475

Max BLEU score at checkpoint 5000: 31.288790287839014
Max METEOR score at checkpoint 5000: 46.2307591478902

### Augmented General Tatoeba

Max BLEU score at checkpoint 1800: 0.4617550903124908
Max METEOR score at checkpoint 4000: 8.515734172174723

Max BLEU score at checkpoint 7600: 18.411436117989492
Max METEOR score at checkpoint 7600: 36.42204997366822

### Augmented LSC Tatoeba

Max BLEU score at checkpoint 2800: 0.27910732188996507
Max METEOR score at checkpoint 1800: 5.1866770992410745

Max BLEU score at checkpoint 9200: 12.140508302324003
Max METEOR score at checkpoint 7600: 27.981138712322736

### Augmented General AnCora

Max BLEU score at checkpoint 1000: 0.27723336220052597
Max METEOR score at checkpoint 1000: 9.015460581825426

Max BLEU score at checkpoint 7600: 1.0518626531351667
Max METEOR score at checkpoint 7200: 14.47017057815886

### Augmented LSC AnCora

Max BLEU score at checkpoint 4400: 0.5226484377143764
Max METEOR score at checkpoint 3000: 9.39164133993008

Max BLEU score at checkpoint 5800: 8.979469579415404
Max METEOR score at checkpoint 8600: 18.171952718038693

### Combined General Meteocat

Max BLEU score at checkpoint 3000: 51.55816238834341
Max METEOR score at checkpoint 3400: 68.22063207830485

Max BLEU score at checkpoint 5000: 40.48869773306925
Max METEOR score at checkpoint 5600: 61.84606490007909

### Combined LSC Meteocat

Max BLEU score at checkpoint 3400: 46.124726460745244
Max METEOR score at checkpoint 3800: 66.12778365834951

Max BLEU score at checkpoint 5000: 39.59497600928088
Max METEOR score at checkpoint 5000: 62.13005806355427

### Augmented LSC Meteocat

Max BLEU score at checkpoint 1400: 3.194377726864911
Max METEOR score at checkpoint 2000: 14.182740306837768

Max BLEU score at checkpoint 7600: 0.5572956004641145
Max METEOR score at checkpoint 7600: 9.416899021171032

### Augmented General Meteocat

Max BLEU score at checkpoint 2400: 1.8136487334291023
Max METEOR score at checkpoint 2000: 17.47729939792037

Max BLEU score at checkpoint 6000: 0.7216144348302048
Max METEOR score at checkpoint 6000: 8.746019275122233
