'''
    Deep Learning With Python
    Develop Deep Learning Models On Theano And TensorFlow Using Keras: Jason Brownlee
'''
messagex = "Deep Learning With Python"

import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates  as mdates
from functools import reduce # This one for the reduce function.
# Loading my tools that I created:
print(os.getcwd())
#sys.path.append('/Users/ghasak/Desktop/My_DATA_MP/Learning/04_PythonforFinance/')
sys.path.append(os.getcwd()+"/")
#/Users/ghasak/Desktop/My_DATA_MP/Learning/04_PythonforFinance/GTools/NiceOutPutClass.py
from GTools.NiceOutPutClass import session_info



class Chapter1():
    session_info("Chapter - 1 - Background").add_line()

    def SimpleTheanoExample():
        # Example of Theano library
        session_info("Simple Theano Example").add_line()
        import theano
        from theano import tensor
        # declare two symbolic floating-point scalars
        a = tensor.dscalar()
        b = tensor.dscalar()





def main():
    output1 = session_info(messagex)
    output1.Initial_run()
    Chapter1.SimpleTheanoExample()






    output1.Finishing_run()


if __name__ == "__main__":
    main()

