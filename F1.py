import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


values = np.arange(11)
equation_values = [5*i**2+7*i+9 for i in values]

X = tf.placeholder("float")
Y = tf.placeholder("float")

a = tf.Variable(np.random.randn(), name = "a")
b = tf.Variable(np.random.randn(), name = "b")
c = tf.Variable(np.random.randn(), name = "c")



learning_rate = 0.005
no_of_epochs = 4800


deg2 = a*tf.pow(X,2) + b*X + c

mse2 = tf.reduce_sum(tf.pow(deg2-Y,2))/(2*11)
optimizer2 = tf.train.AdamOptimizer(learning_rate).minimize(mse2)


init=tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for epoch in range(no_of_epochs):
        for (x,y) in zip(values, equation_values):
            sess.run(optimizer2, feed_dict={X:x, Y:y})
        if (epoch+1)%300==0:
            cost = sess.run(mse2,feed_dict={X:values,Y:equation_values})
            print("Epoch",(epoch+1), ": Training Cost:", cost," a, b, c = ",sess.run(a),', ',sess.run(b),', ',sess.run(c),'\n')

            training_cost = sess.run(mse2,feed_dict={X:values,Y:equation_values})
            a_ = sess.run(a)
            b_ = sess.run(b)
            c_ = sess.run(c)

print(training_cost, a_,b, c)

input_x = int(input('Enter value of x: '))
print('Output of polynomial Function, F(x): ',np.round(a_*input_x**2 + b_*input_x + c_ ))

