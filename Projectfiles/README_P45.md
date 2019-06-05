# Deep Learning
## TensorFlow Basics p.45

After Installing TensorFlow in our current Machine, we will use this library to preform some editing.

## Output of current file
To run this file use

```
python ~/3_PracticalMachineLearning/Projectfiles/P45_XXX.py
```

![](./output_images/P45-1.png)


## - My Note
Here will try to understand some basics to and fundamental staff with TensorFlow library.
## Problem
From the tensorflow 1.0.0 release notes:

```
tf.mul, tf.sub and tf.neg are deprecated in favor of tf.multiply, tf.subtract and tf.negative.
```

So you will need a **session** and then call the tf.session() to run your it.
 ```python
import tensorflow as tf
    x1 = tf.constant(5)
    x2 = tf.constant(6)
    results = tf.multiply(x1,x2) # mul() multiplication, or matmul() which is with array
    print(results)
    sess = tf.Session()
    print(sess.run(results))
 ```

# Note
You have to a computational graph that you can modified, and it will be built in our computational graph.



#

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
