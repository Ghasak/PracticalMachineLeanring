
# Deep Learning with Neural Networks and TensorFlow
# - Using More Data p.50 - Part 8
We are using the following version of TensorFlow

```py
python -c "import tensorflow; print('Tensorflow library version is =',tensorflow.__version__)"
```
which is:

```py
Tensorflow library version is = 1.13.1
```

## Output of current file
To run this file use

```
python ~/3_PracticalMachineLearning/Projectfiles/P50_XXX.py
```
## - My Note

Starting from previous file we have to include the following. We will add more data for our model, we will use the exact deep neural network that we have developed.We will use the **sentiment140 dataset**

# Step -1- Searching for the data:
We will use the **sentiment140 dataset**, See here: http://help.sentiment140.com/for-students
and I read more about available dataset for training machine learning here:
https://blog.cambridgespark.com/50-free-machine-learning-datasets-sentiment-analysis-b9388f79c124. We will ignore the **neutral** repsonse by the twitter. and we will follow the run a new code for the new dataset.

Now, at the moment, this dataset isn't likely too large for you to fit into memory, but, once we convert it to the bag of words model from before, it definitely will be. So, this time, we have to begin considering what to do when datasets are much larger. When working with large datasets, we have a few changes:

We want to buffer that data coming in to an acceptable size. Rather than reading an entire file all at once, we can instead read it in segments of 10mb at a time with buffering.
## NOTE
We will use the CPU here in our MacPro, but also we can use the GPU, the GPU will give us the power of estimation much better with accuracy.

# Step -2- preprocessing dataset,
we will create here in P50 a preprocessing python script that will not be imported in the next **P51** rather saving the output as a csv with a buffer size around 10 MB.


![](./output_images/P50-1.png)

Or through terminal

![](./output_images/P50-2.png)






## Acknowledgments
* Based on sentdex Lectures, modified to serve the purpose that I need in my academic research.

## Inspiration
https://www.youtube.com/watch?v=7fcWfUavO7E&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=48&frags=pl%2Cwn


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
