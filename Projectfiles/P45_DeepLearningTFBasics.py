import tensorflow as tf


x1 = tf.constant(5)
x2 = tf.constant(6)

results = tf.multiply(x1,x2) # mul() multiplication, or matmul() which is with array

#print(results)

# sess = tf.Session()
# print(sess.run(results))

# This will close once its done which is much better than the pervious way
with tf.Session() as sess:
    output = sess.run(results)
    print(output)

# You can referencing to python variables once you declare the variable
print(output)

