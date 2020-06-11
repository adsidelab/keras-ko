# Using pre-trained word embeddings

**Author:** [fchollet](https://twitter.com/fchollet)<br>
**Date created:** 2020/05/05<br>
**Last modified:** 2020/05/05<br>
**Description:** Text classification on the Newsgroup20 dataset using pre-trained GloVe word embeddings.


<img class="k-inline-icon" src="https://colab.research.google.com/img/colab_favicon.ico"/> [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/pretrained_word_embeddings.ipynb)  <span class="k-dot">•</span><img class="k-inline-icon" src="https://github.com/favicon.ico"/> [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/pretrained_word_embeddings.py)



---
## Setup


```python
import numpy as np
import tensorflow as tf
from tensorflow import keras

```

---
## Introduction

In this example, we show how to train a text classification model that uses pre-trained
word embeddings.

We'll work with the Newsgroup20 dataset, a set of 20,000 message board messages
belonging to 20 different topic categories.

For the pre-trained word embeddings, we'll use
[GloVe embeddings](http://nlp.stanford.edu/projects/glove/).

---
## Download the Newsgroup20 data


```python
data_path = keras.utils.get_file(
    "news20.tar.gz",
    "http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-20/www/data/news20.tar.gz",
    untar=True,
)

```

---
## Let's take a look at the data


```python
import os
import pathlib

os.listdir(pathlib.Path(data_path).parent)

data_dir = pathlib.Path(data_path).parent / "20_newsgroup"
dirnames = os.listdir(data_dir)
print("Number of directories:", len(dirnames))
print("Directory names:", dirnames)

fnames = os.listdir(data_dir / "comp.graphics")
print("Number of files in comp.graphics:", len(fnames))
print("Some example filenames:", fnames[:5])

```

<div class="k-default-codeblock">
```
Number of directories: 20
Directory names: ['talk.politics.mideast', 'rec.autos', 'comp.sys.mac.hardware', 'alt.atheism', 'rec.sport.baseball', 'comp.os.ms-windows.misc', 'rec.sport.hockey', 'sci.crypt', 'sci.med', 'talk.politics.misc', 'rec.motorcycles', 'comp.windows.x', 'comp.graphics', 'comp.sys.ibm.pc.hardware', 'sci.electronics', 'talk.politics.guns', 'sci.space', 'soc.religion.christian', 'misc.forsale', 'talk.religion.misc']
Number of files in comp.graphics: 1000
Some example filenames: ['38254', '38402', '38630', '38865', '38891']

```
</div>
Here's a example of what one file contains:


```python
print(open(data_dir / "comp.graphics" / "38987").read())

```

<div class="k-default-codeblock">
```
Newsgroups: comp.graphics
Path: cantaloupe.srv.cs.cmu.edu!das-news.harvard.edu!noc.near.net!howland.reston.ans.net!agate!dog.ee.lbl.gov!network.ucsd.edu!usc!rpi!nason110.its.rpi.edu!mabusj
From: mabusj@nason110.its.rpi.edu (Jasen M. Mabus)
Subject: Looking for Brain in CAD
Message-ID: <c285m+p@rpi.edu>
Nntp-Posting-Host: nason110.its.rpi.edu
Reply-To: mabusj@rpi.edu
Organization: Rensselaer Polytechnic Institute, Troy, NY.
Date: Thu, 29 Apr 1993 23:27:20 GMT
Lines: 7
```
</div>
    
<div class="k-default-codeblock">
```
Jasen Mabus
RPI student
```
</div>
    
<div class="k-default-codeblock">
```
	I am looking for a hman brain in any CAD (.dxf,.cad,.iges,.cgm,etc.) or picture (.gif,.jpg,.ras,etc.) format for an animation demonstration. If any has or knows of a location please reply by e-mail to mabusj@rpi.edu.
```
</div>
    
<div class="k-default-codeblock">
```
Thank you in advance,
Jasen Mabus  
```
</div>
    


As you can see, there are header lines that are leaking the file's category, either
explicitly (the first line is literally the category name), or implicitly, e.g. via the
`Organization` filed. Let's get rid of the headers:


```python
samples = []
labels = []
class_names = []
class_index = 0
for dirname in sorted(os.listdir(data_dir)):
    class_names.append(dirname)
    dirpath = data_dir / dirname
    fnames = os.listdir(dirpath)
    print("Processing %s, %d files found" % (dirname, len(fnames)))
    for fname in fnames:
        fpath = dirpath / fname
        f = open(fpath, encoding="latin-1")
        content = f.read()
        lines = content.split("\n")
        lines = lines[10:]
        content = "\n".join(lines)
        samples.append(content)
        labels.append(class_index)
    class_index += 1

print("Classes:", class_names)
print("Number of samples:", len(samples))

```

<div class="k-default-codeblock">
```
Processing alt.atheism, 1000 files found
Processing comp.graphics, 1000 files found
Processing comp.os.ms-windows.misc, 1000 files found
Processing comp.sys.ibm.pc.hardware, 1000 files found
Processing comp.sys.mac.hardware, 1000 files found
Processing comp.windows.x, 1000 files found
Processing misc.forsale, 1000 files found
Processing rec.autos, 1000 files found
Processing rec.motorcycles, 1000 files found
Processing rec.sport.baseball, 1000 files found
Processing rec.sport.hockey, 1000 files found
Processing sci.crypt, 1000 files found
Processing sci.electronics, 1000 files found
Processing sci.med, 1000 files found
Processing sci.space, 1000 files found
Processing soc.religion.christian, 997 files found
Processing talk.politics.guns, 1000 files found
Processing talk.politics.mideast, 1000 files found
Processing talk.politics.misc, 1000 files found
Processing talk.religion.misc, 1000 files found
Classes: ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
Number of samples: 19997

```
</div>
There's actually one category that doesn't have the expected number of files, but the
difference is small enough that the problem remains a balanced classification problem.

---
## Shuffle and split the data into training & validation sets


```python
# Shuffle the data
seed = 1337
rng = np.random.RandomState(seed)
rng.shuffle(samples)
rng = np.random.RandomState(seed)
rng.shuffle(labels)

# Extract a training & validation split
validation_split = 0.2
num_validation_samples = int(validation_split * len(samples))
train_samples = samples[:-num_validation_samples]
val_samples = samples[-num_validation_samples:]
train_labels = labels[:-num_validation_samples]
val_labels = labels[-num_validation_samples:]

```

---
## Create a vocabulary index

Let's use the `TextVectorization` to index the vocabulary found in the dataset.
Later, we'll use the same layer instance to vectorize the samples.

Our layer will only consider the top 20,000 words, and will truncate or pad sequences to
be actually 200 tokens long.


```python
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

vectorizer = TextVectorization(max_tokens=20000, output_sequence_length=200)
text_ds = tf.data.Dataset.from_tensor_slices(train_samples).batch(128)
vectorizer.adapt(text_ds)

```

You can retrieve the computed vocabulary used via `vectorizer.get_vocabulary()`. Let's
print the top 5 words:


```python
vectorizer.get_vocabulary()[:5]

```




<div class="k-default-codeblock">
```
[b'the', b'to', b'of', b'a', b'and']

```
</div>
Let's vectorize a test sentence:


```python
output = vectorizer(np.array([["the cat sat on the mat"]]))
output.numpy()[0, :6]

```




<div class="k-default-codeblock">
```
array([   2, 3697, 1686,   15,    2, 5943])

```
</div>
As you can see, "the" gets represented as "2". Why not 0, given that "the" was the first
word in the vocabulary? That's because index 0 is reserved for padding and index 1 is
reserved for "out of vocabulary" tokens.

Here's a dict mapping words to their indices:


```python
voc = vectorizer.get_vocabulary()
word_index = dict(zip(voc, range(2, len(voc))))

```

As you can see, we obtain the same encoding as above for our test sentence:


```python
test = [b"the", b"cat", b"sat", b"on", b"the", b"mat"]
[word_index[w] for w in test]

```




<div class="k-default-codeblock">
```
[2, 3697, 1686, 15, 2, 5943]

```
</div>
---
## Load pre-trained word embeddings

Let's download pre-trained GloVe embeddings (a 822M zip file).

You'll need to run the following commands:

```
!wget http://nlp.stanford.edu/data/glove.6B.zip
!unzip -q glove.6B.zip
```

The archive contains text-encoded vectors of various sizes: 50-dimensional,
100-dimensional, 200-dimensional, 300-dimensional. We'll use the 100D ones.

Let's make a dict mapping words (strings) to their NumPy vector representation:


```python
path_to_glove_file = os.path.join(
    os.path.expanduser("~"), ".keras/datasets/glove.6B.100d.txt"
)

embeddings_index = {}
with open(path_to_glove_file) as f:
    for line in f:
        word, coefs = line.split(maxsplit=1)
        coefs = np.fromstring(coefs, "f", sep=" ")
        embeddings_index[word] = coefs

print("Found %s word vectors." % len(embeddings_index))

```

<div class="k-default-codeblock">
```
Found 400000 word vectors.

```
</div>
Now, let's prepare a corresponding embedding matrix that we can use in a Keras
`Embedding` layer. It's a simple NumPy matrix where entry at index `i` is the pre-trained
vector for the word of index `i` in our `vectorizer`'s vocabulary.

**Note:** the `TextVectorization` layer stores tokens as bytes, not `str` types.
This means that you need to decode them to `utf-8` before doing string comparisons, like
the below: `embeddings_index.get(word.decode('utf-8'))`


```python
num_tokens = len(voc) + 2
embedding_dim = 100
hits = 0
misses = 0

# Prepare embedding matrix
embedding_matrix = np.zeros((num_tokens, embedding_dim))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word.decode("utf-8"))
    if embedding_vector is not None:
        # Words not found in embedding index will be all-zeros.
        # This includes the representation for "padding" and "OOV"
        embedding_matrix[i] = embedding_vector
        hits += 1
    else:
        misses += 1
print("Converted %d words (%d misses)" % (hits, misses))


```

<div class="k-default-codeblock">
```
Converted 17998 words (1999 misses)

```
</div>
Next, we load the pre-trained word embeddings matrix into an `Embedding` layer.

Note that we set `trainable=False` so as to keep the embeddings fixed (we don't want to
update them during training).


```python
from tensorflow.keras.layers import Embedding

embedding_layer = Embedding(
    num_tokens,
    embedding_dim,
    embeddings_initializer=keras.initializers.Constant(embedding_matrix),
    trainable=False,
)

```

---
## Build the model

A simple 1D convnet with global max pooling and a classifier at the end.


```python
from tensorflow.keras import layers

int_sequences_input = keras.Input(shape=(None,), dtype="int64")
embedded_sequences = embedding_layer(int_sequences_input)
x = layers.Conv1D(128, 5, activation="relu")(embedded_sequences)
x = layers.MaxPooling1D(5)(x)
x = layers.Conv1D(128, 5, activation="relu")(x)
x = layers.MaxPooling1D(5)(x)
x = layers.Conv1D(128, 5, activation="relu")(x)
x = layers.GlobalMaxPooling1D()(x)
x = layers.Dense(128, activation="relu")(x)
x = layers.Dropout(0.5)(x)
preds = layers.Dense(len(class_names), activation="softmax")(x)
model = keras.Model(int_sequences_input, preds)
model.summary()

```

<div class="k-default-codeblock">
```
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, None)]            0         
_________________________________________________________________
embedding (Embedding)        (None, None, 100)         2000100   
_________________________________________________________________
conv1d (Conv1D)              (None, None, 128)         64128     
_________________________________________________________________
max_pooling1d (MaxPooling1D) (None, None, 128)         0         
_________________________________________________________________
conv1d_1 (Conv1D)            (None, None, 128)         82048     
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, None, 128)         0         
_________________________________________________________________
conv1d_2 (Conv1D)            (None, None, 128)         82048     
_________________________________________________________________
global_max_pooling1d (Global (None, 128)               0         
_________________________________________________________________
dense (Dense)                (None, 128)               16512     
_________________________________________________________________
dropout (Dropout)            (None, 128)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 20)                2580      
=================================================================
Total params: 2,247,416
Trainable params: 247,316
Non-trainable params: 2,000,100
_________________________________________________________________

```
</div>
---
## Train the model

First, convert our list-of-strings data to NumPy arrays of integer indices. The arrays
are right-padded.


```python
x_train = vectorizer(np.array([[s] for s in train_samples])).numpy()
x_val = vectorizer(np.array([[s] for s in val_samples])).numpy()

y_train = np.array(train_labels)
y_val = np.array(val_labels)

```

We use categorical crossentropy as our loss since we're doing softmax classification.
Moreover, we use `sparse_categorical_crossentropy` since our labels are integers.


```python
model.compile(
    loss="sparse_categorical_crossentropy", optimizer="rmsprop", metrics=["acc"]
)
model.fit(x_train, y_train, batch_size=128, epochs=20, validation_data=(x_val, y_val))

```

<div class="k-default-codeblock">
```
Epoch 1/20
125/125 [==============================] - 8s 64ms/step - loss: 2.6467 - acc: 0.1403 - val_loss: 2.0737 - val_acc: 0.2796
Epoch 2/20
125/125 [==============================] - 8s 65ms/step - loss: 1.9139 - acc: 0.3422 - val_loss: 1.5841 - val_acc: 0.4689
Epoch 3/20
125/125 [==============================] - 8s 65ms/step - loss: 1.4909 - acc: 0.4915 - val_loss: 1.3311 - val_acc: 0.5649
Epoch 4/20
125/125 [==============================] - 8s 67ms/step - loss: 1.2629 - acc: 0.5631 - val_loss: 1.3060 - val_acc: 0.5571
Epoch 5/20
125/125 [==============================] - 9s 69ms/step - loss: 1.1007 - acc: 0.6231 - val_loss: 1.0992 - val_acc: 0.6302
Epoch 6/20
125/125 [==============================] - 8s 68ms/step - loss: 0.9657 - acc: 0.6690 - val_loss: 1.2182 - val_acc: 0.6062
Epoch 7/20
125/125 [==============================] - 9s 73ms/step - loss: 0.8474 - acc: 0.7097 - val_loss: 1.1390 - val_acc: 0.6297
Epoch 8/20
125/125 [==============================] - 10s 79ms/step - loss: 0.7485 - acc: 0.7388 - val_loss: 0.9862 - val_acc: 0.6784
Epoch 9/20
125/125 [==============================] - 10s 77ms/step - loss: 0.6623 - acc: 0.7714 - val_loss: 1.0549 - val_acc: 0.6562
Epoch 10/20
125/125 [==============================] - 10s 78ms/step - loss: 0.5723 - acc: 0.7983 - val_loss: 1.3427 - val_acc: 0.6164
Epoch 11/20
125/125 [==============================] - 9s 75ms/step - loss: 0.5030 - acc: 0.8283 - val_loss: 1.1039 - val_acc: 0.6739
Epoch 12/20
125/125 [==============================] - 10s 83ms/step - loss: 0.4420 - acc: 0.8483 - val_loss: 1.1172 - val_acc: 0.6899
Epoch 13/20
125/125 [==============================] - 10s 81ms/step - loss: 0.3761 - acc: 0.8697 - val_loss: 1.3080 - val_acc: 0.6612
Epoch 14/20
125/125 [==============================] - 9s 75ms/step - loss: 0.3404 - acc: 0.8852 - val_loss: 1.5581 - val_acc: 0.6192
Epoch 15/20
125/125 [==============================] - 10s 77ms/step - loss: 0.2835 - acc: 0.9042 - val_loss: 1.2626 - val_acc: 0.7079
Epoch 16/20
125/125 [==============================] - 10s 77ms/step - loss: 0.2653 - acc: 0.9099 - val_loss: 1.3099 - val_acc: 0.7052
Epoch 17/20
125/125 [==============================] - 10s 81ms/step - loss: 0.2528 - acc: 0.9176 - val_loss: 1.2101 - val_acc: 0.7047
Epoch 18/20
125/125 [==============================] - 10s 76ms/step - loss: 0.2156 - acc: 0.9299 - val_loss: 1.4729 - val_acc: 0.6844
Epoch 19/20
125/125 [==============================] - 10s 79ms/step - loss: 0.2010 - acc: 0.9343 - val_loss: 1.4224 - val_acc: 0.6969
Epoch 20/20
 37/125 [=======>......................] - ETA: 5s - loss: 0.2082 - acc: 0.9335

```
</div>
---
## Export an end-to-end model

Now, we may want to export a `Model` object that takes as input a string of arbitrary
length, rather than a sequence of indices. It would make the model much more portable,
since you wouldn't have to worry about the input preprocessing pipeline.

Our `vectorizer` is actually a Keras layer, so it's simple:


```python
string_input = keras.Input(shape=(1,), dtype="string")
x = vectorizer(string_input)
preds = model(x)
end_to_end_model = keras.Model(string_input, preds)

probabilities = end_to_end_model.predict(
    [["this message is about computer graphics and 3D modeling"]]
)

class_names[np.argmax(probabilities[0])]

```




<div class="k-default-codeblock">
```
'comp.graphics'

```
</div>