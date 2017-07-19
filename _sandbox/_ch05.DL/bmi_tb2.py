import pandas as pd # to read csv
import numpy as np
import tensorflow as tf

# data read

csv = pd.read_csv("../_mainText_srcs/ch5/bmi.csv")

# data normalizing

csv["height"] /= 200
csv["weight"] /= 100

# label to array

bmi_class = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x: np.array(bmi_class[x]))

# test set

test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

# making DFG

#1. declaring placeholder

x = tf.placeholder(tf.float32, [None,2], name="x")   # height, weight
y = tf.placeholder(tf.float32, [None,3], name="y")   # pattern

#2. declaring variables

with tf.name_scope('interface') as scope:
    W = tf.Variable(tf.zeros([2,3]), name="W") # weight
    b = tf.Variable(tf.zeros([3]), name="b") # bias

#3. defining softmax regression
    with tf.name_scope('softmax') as scope:
        y_hat = tf.nn.softmax(tf.matmul(x,W)+b)



# model learning
with tf.name_scope('loss') as scope:
    cross_entropy = -tf.reduce_sum(y*tf.log(y_hat))

with tf.name_scope('training') as scope:
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(cross_entropy)

# calculating prediction success rate

predict = tf.equal(tf.argmax(y_hat,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))


# start session

sess = tf.Session()
sess.run(tf.global_variables_initializer()) # initialization


# run learning

for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1+i : 1+i+100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y: y_ans}
    sess.run(train, feed_dict = fd)
    if step%500 == 0:
        cre = sess.run(cross_entropy, feed_dict = fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
        print ("step=",step, "cre=",cre, "acc=",acc)
        
        
# final accuracy

acc = sess.run(accuracy, feed_dict = {x: test_pat, y: test_ans})
print ("accuracy=",acc)

tw = tf.summary.FileWriter("_log_dir_tb", graph=sess.graph)
