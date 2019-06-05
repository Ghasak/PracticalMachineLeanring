# Deep Learning with Neural Networks and TensorFlow
## Neural Network Model p.46

## Output of current file
To run this file use

```
python ~/3_PracticalMachineLearning/Projectfiles/P46_XXX.py
```
## - My Note
We will start with our first Neural Network Model.
The logic in any Neural Network is almost can be summarized as:

```c
Input > weight
> hidden layer 1 (activation function)
> weights
> hidden layer 2 (activation function)
> weights
> output layer

compare output to intended output > cost function (cross entropy)

optimization function (optimizer) > minimize cost(AdamOptimizer .., SGD, AdaGrad)

backpropagation (modifying the weights)

fee forward + backpropagation = epoch // epoch is a one cycle, can be 1 times, 15 times, up to lowering the cost function

```

# CODE PROGRESS

```py
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/",one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100 # Batching a 100 images to check

# height x width
x = tf.placeholder('float',[None,784]) # The matrix is 28 by 28 values, you can remove this [None, 784]
y = tf.placeholder('float')


def neural_network_model(data):

    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                    'biases':tf.Variable(tf.random_normal([n_classes]))}

    # (Input_data * weights) + biases
    l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']

    return output
```

![](./output_images/P45-1.png)
## Acknowledgments
* Based on sentdex Lectures, modified to serve the purpose that I need in my academic research.

## Inspiration

https://pythonprogramming.net/tensorflow-introduction-machine-learning-tutorial/

## Template elements:
<kbd>Ctrl</kbd>
## Adding more features:
## Requirements
python 0.x <br />
Packages: see **requirements.txt** <br />
## Instructions
1. Install all required packages
2. Modify parameters if desired
3. Run **folder/script.R**
