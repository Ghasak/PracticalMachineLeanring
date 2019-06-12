
# Deep Learning with Neural Networks and TensorFlow
# - Processing our own Data p.48 - Part 5
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
python ~/3_PracticalMachineLearning/Projectfiles/P48_XXX.py
```
## - My Note
We will work with both negative and positive sentiment data set. We will come up with a dictionary for words we know and convert to a vector form to get the results.

## NOTE
We will need a package called **nltk** short for **Natural Language tool-Kit** and after you get to install the tool first using

```py
pip install nltk
```
Later you can go the next step, which is to show the following, in the terminal specifically.This will open either a GUI, or stay headless. Go ahead and just download all. If you are in GUI form, just choose download all. If you are in the text version, type d, then all. Once that's done, you're ready to progress. If you're lost or confused, check out the first NLTK tutorial for installing NLTK.

```py
import nltk
nltk.download()
then pick the option -all
```
Here is how you install them all together see

![](./output_images/P48-1.png)

Then you will get the results as,

![](./output_images/P48-2.png)

## Hint
Read more about Natural language processing in our different project file that we worked on. Starting with stemming then lemmatizing.

# What we will need
We need the following packages

```py
import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import random
import pickle
from collections import Counter
from nltk.stem import WordNetLemmatizer
```
For example the word_tokenize is a tool used to separate a sentence into a words in a list similar to **string.split()** method. These are just some necessary imports. NLTK has been explained, numpy is a given, random will be used to shuffle the data, Counter will be used for sorting most common lemmas, and pickle to save the process so that we dont need to do it every time. We define the lemmatizer, and then we set the hm_lines value. 100,000 will do all of the lines, there are just over 10,000 lines. If you want to test something new, or shrink the total data size for a smaller computer/processor, you can set a smaller number here. I mostly used this for quickly testing new functions..etc. No reason to run through the entire set to just quickly test a different method.



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
