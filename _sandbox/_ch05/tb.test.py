import tensorflow as tf

a = tf.constant(20, name="a")
b = tf.constant(30, name="b")

mul_op = a*b

sess = tf.Session()

tw=tf.summary.FileWriter(logdir="_log_dir_tb", graph=sess.graph)

print(sess.run(mul_op))

