#############################################
#                                           #
#   CSE4088 - Intro. to Machine Learning    #
#               Homework #3                 #
#       Oguzhan BOLUKBAS - 150114022        #
#                                           #
#############################################
#############################################
#                                           #
#             Gradient Descent              #
#                                           #
#############################################

print "\n\n-_-_-_-_- Gradient Descent -_-_-_-_-"

#Question 4
import math
import numpy as np
import sympy as sp

u, v = sp.symbols('u v', real=True)
E = ((u*sp.exp(v) - 2*v*sp.exp(-u)) ** 2)

print "\nQuestion 4: [e] Partial derivative of E(u,v) with respect to u is", sp.diff(E, u)

def E(u, v):
   return (u * np.exp(v) - 2 * v * np.exp(-u)) ** 2

def dE_du(u, v):
   return 2 * (u * np.exp(v) - 2 * v * np.exp(-u)) * (np.exp(v) + 2 * v * np.exp(-u))

def dE_dv(u, v):
   return 2 * (u * np.exp(v) - 2 * v * np.exp(-u)) * (u * np.exp(v) - 2 * np.exp(-u))

# Question 5 & 6
iteration = 0
error = 0
eta = 0.1           # Learning rate
u, v = 1, 1         # Start point

while True:
   du, dv = dE_du(u, v), dE_dv(u, v)

   u -= eta * du
   v -= eta * dv

   error = E(u, v)

   iteration += 1

   if error < 1e-14:
      break

# Question 5
print "\nQuestion 5: [d] It takes", iteration, "iterations"

# Question 6
print "\nQuestion 6: [e] The closest values among the following choices to the final (u,v) is (%.3f, %.3f)" % (u, v)

# Question 7
u, v = 1, 1
for _ in range(15):
   u -= eta * dE_du(u, v)
   v -= eta * dE_dv(u, v)

# Question 7
print "\nQuestion 7: [a] The error E(u,v) be closest after 15 full iterations is %.3f" % E(u, v)

#############################################
#                                           #
#           Logistic Regression             #
#                                           #
#############################################

print "\n\n-_-_-_-_- Logistic Regression -_-_-_-_-"

import random
import matplotlib.pyplot as plt

d = 2
N = 100

# To generate uniformly points in X = [-1,1]x[-1,1]
def rnd(n): 
    return np.random.uniform(-1, 1, n)

# To generate random points for a dataset X
def create_dataset(N):
    return rnd((N,d))

def create_targets(plotting):
    line_coords = rnd((2,d))

    # Least squares polynomial fit. It returns polynomial coefficients, highest power first.
    slope, intercept = np.polyfit(line_coords[:,0],line_coords[:,1],1)

    X = create_dataset(N)
    y = calc_target((slope,intercept),X)
    
    if plotting:
        x_coords = np.array([-1,1])
        y_coords = x_coords*slope + intercept
        plt.plot(x_coords,y_coords) 
        plt.scatter( X[y > 0][:, 0], X[y > 0][:, 1], color = "red" )
        plt.scatter( X[y < 0][:, 0], X[y < 0][:, 1], color = "blue" )
        
        plt.xlim([-1,1])
        plt.ylim([-1,1])
        plt.show()

    return (slope,intercept), (X,y)    

# To generate outputs of dataset according to polynomial func.
def calc_target(line, X):
    slope = line[0]
    intercept = line[1]
    
    x0 = X[:,0]
    y0 = X[:,1]
    
    y_out = np.zeros(x0.shape[0])
    y_out[x0*slope + intercept > y0] = 1
    y_out[x0*slope + intercept < y0] = -1

    return y_out

# Stack arrays in sequence horizontally (column wise)
def add_bias(X):
    return np.hstack((np.ones((X.shape[0],1)), X))
    
# To calculate result of the output node
def sigmoid(x):
    return 1/(1+np.e**-x)

# Main function
class LogisticRegression():
    def __init__(self):
        self.w = np.zeros(d+1)      # Weights are initially 0
        self.eta = 0.01             # Learning rate
        self.threshold = 0.01
    
    # To fit the data into the target polynomial func. 
    def fit(self,data,target):
        X = add_bias(data)
        data = list(zip(X,target))
        
        for i in range(1,10001):    
            random.shuffle(data)
            w1 = self.w.copy()

            for x_i, y_i in data:
                dE = -(y_i * x_i) / (1 + np.e**(y_i*self.w.dot(x_i)))
                self.w -= self.eta*dE

            w_score = np.sqrt(sum((w1 - self.w)**2))    
            
            if w_score < self.threshold:
                return i
        
        return -1
    
    # To predict the result
    def predict(self,data):
        X = add_bias(data)
        return sigmoid(self.w.dot(X.T))

    # To calculate cross entrophy of the data and the outputs
    def calc_cross_entropy(self,data,y):
        X = add_bias(data)
        return np.log(1 + np.e**(-y * self.w.dot(X.T))).mean()

num_epochs = []
errors = []
num_iter = 10

for i in range(1,num_iter+1):

    # Turn False to True in order to see plots
    target_function, target_data = create_targets(False)
    
    lr = LogisticRegression()
    num_epoch = lr.fit(target_data[0],target_data[1])
    
    # Generate new datasets
    new_X = create_dataset(100)
    new_y = calc_target(target_function, new_X)
    error = lr.calc_cross_entropy(new_X,new_y)
    
    num_epochs.append(num_epoch)
    errors.append(error)

print "\nQuestion 8: [d] The closest to E_out for N=100 is: %.3f" % np.mean(errors)
print "\nQuestion 9: [a] It takes", np.mean(num_epochs), "epochs on average"

#############################################
#                                           #
#             Regularization with           #
#                Weight Decay               #
#                                           #
#############################################

print "\n\n-_-_-_-_- Regularization with Weight Decay -_-_-_-_-"

def read_data(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        m = len(lines)
        if m == 0:
            return None
        n = len(lines[0].split())
        mat = np.empty((m, n))
        for i, line in enumerate(lines):
            for j, number in enumerate(line.split()):
                mat[i][j] = float(number)
        return mat
    return None

def transform(point):
    a = [1, point[0], point[1], point[0]**2, point[1]**2, point[0]* point[1],
        abs(point[0] - point[1]), abs(point[0] + point[1]), point[2]]

    return a

def transformPoints(X):
    X_transformed = []
    for point in X:
        X_transformed.append(transform(point))
    return X_transformed

# To calculate weights
def lr_weights(X_transformed):
    X, y = [], []
    y_location = len(X_transformed[0]) -1 # y's location is assumed to be the last element in the list

    # Construct X space and split y values out
    for point in X_transformed:
        X.append(np.array(point[:y_location]))
        y.append(point[y_location])

    X = np.array(X)
    y = np.array(y)
    X_inverse = np.linalg.pinv(X)

    return np.dot(X_inverse, y)

def linRegWithRegularization(X_transformed, l):
    X, y = [], []
    y_location = len(X_transformed[0]) -1 # y's location is assumed to be the last element in the list

    for point in X_transformed:
        X.append(np.array(point[:y_location]))
        y.append(point[y_location])

    weights = lr_weights(X_transformed)
    X = np.array(X)
    X_inverse = np.linalg.pinv(X + np.array(l / len(X_transformed) * np.dot(weights, weights)))
    return np.dot(X_inverse, y)

def E(weights, X_transformed):
    errorCount = 0
    y_location = len(X_transformed[0]) - 1

    for point in X_transformed:
        if np.sign(np.dot(weights,point[:y_location])) != point[y_location]:
            errorCount += 1

    return errorCount/float(len(X_transformed))

X = read_data("in.dta")
X_test = read_data("out.dta")

# Assumes X_transformed is a list of lists, and the last element in given list is the y value
X_transformed = transformPoints(X)
X_test_transformed = transformPoints(X_test)

# Question 2
weights = lr_weights(X_transformed)
E_in = E(weights, X_transformed)
E_out = E(weights, X_test_transformed)
print "\nQuestion 2: [a] The closest values among the following choices to the final (u,v) is (%.2f, %.2f)" % (E_in,E_out)

# Question 3
l = 10**-3
weights = linRegWithRegularization(X_transformed, l)
E_in = E(weights, X_transformed)
E_out = E(weights, X_test_transformed)
print "\nQuestion 3: [d] The closest values among the following choices to the final (u,v) is (%.2f, %.2f)" % (E_in,E_out)

# Question 4
l = 10**3
weights = linRegWithRegularization(X_transformed, l)
E_in = E(weights, X_transformed)
E_out = E(weights, X_test_transformed)
print "\nQuestion 4: [e] The closest values among the following choices to the final (u,v) is (%.2f, %.2f)" % (E_in,E_out)

# Question 5
e_out_min = float("inf")
i_min = float("inf")
for i in range(-2, 2+1):
    e_out = E(linRegWithRegularization(X_transformed, 10**i), X_test_transformed)
    if(e_out < e_out_min):
        e_out_min = e_out
        i_min = i
print "\nQuestion 5: [d] The value of k achieves the smallest out-of-sample classification error is:", i_min

# Question 6
e_out_min = float("inf")
i_min = float("inf")
for i in range(-20, 20+1):
    e_out = E(linRegWithRegularization(X_transformed, 10**i), X_test_transformed)
    if(e_out < e_out_min):
        e_out_min = e_out
        i_min = i
print "\nQuestion 6: [b] The closest value to the minimum out-of-sample classification error is %.2f" % e_out_min

#############################################
#                                           #
#              Neural Networks              #
#                                           #
#############################################

print "\n\n-_-_-_-_- Neural Networks -_-_-_-_-"

# Question 8
d0 = 5
d1 = 3
d2 = 1

forward_cal = d0*d1 + d1*d2
backward_calc = d2*d1 + d1*d0
updating_weights = d2 + d1 + d0

operation_counter = forward_cal + backward_calc + updating_weights

print "\nQuestion 8: [d] Total number of operations required in a single iteration of backpropagation is", operation_counter

# Question 9
print "\nQuestion 9: [a] Minimum possible number of weights that such a network can have", 10*1 + (36/2)*2

# Question 10
layer_num_2 = zip( range(1,36), map(lambda(x): 10*(x-1) + (x)*(36-x-1) + (36-x), range(1,36)))

max_num_weights = -1

for i in range(35):
    if (layer_num_2[i][1] > max_num_weights):
        max_num_weights = layer_num_2[i][1]

print "\nQuestion 10: [e] Maximum possible number of weights that such a network can have is", max_num_weights, "\n"