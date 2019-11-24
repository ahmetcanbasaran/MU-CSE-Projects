#############################################
#                                           #
#   CSE4088 - Intro. to Machine Learning    #
#               Homework #2                 #
#       Oguzhan BOLUKBAS - 150114022        #
#                                           #
#############################################





#############################################
#                                           #
#           Generalization Error            #
#                                           #
#############################################

import math

# Question #2
e = 0.05
M = 10
print("\nQuestion #2 - For the case M = 10, the result is: ",
      math.ceil(-1 / (2 * e**2) * math.log(0.03 / (2 * M))),
      " and the least number of examples N is [c]1500")



# Question #3
e = 0.05
M = 100
print("\nQuestion #3 - For the case M = 100, the result is: ",
      math.ceil(-1 / (2 * e**2) * math.log(0.03 / (2 * M))),
      " and the least number of examples N is [d]2000")





#############################################
#                                           #
#     The Perceptron Learning Algorithm     #
#                                           #
#############################################

import numpy as np
import matplotlib.pyplot as plt


# To generate uniformly points in X = [-1,1]x[-1,1]
def random(n): 
    return np.random.uniform(-1, 1, n)

# Scalar multiplication vectors and to take sign of result
def out_perceptron(X, weights):
    total = np.dot(X, weights)
    return np.sign(total)

# To generate N datapoints and take transpose of the generated matrix
def generate_datapoints(N):
    return (np.array([np.ones(N), random(N), random(N)])).T

# Repeat the experiment for 1000 times
ITERATION = 1000
"""
def PLA(N, Question_10):

    iterations_total = 0
    ratio_misclassification_total = 0

    global iterations_avg
    global ratio_misclassification_avg

    for i in range(ITERATION):

      # To choose two random points (uniformly in X = [-1,1]x[-1,1])
      A = np.random.uniform(-1, 1, 2)
      B = np.random.uniform(-1, 1, 2)

      # To find variables used in line formula: y = m*x + b 
      m = (B[1] - A[1]) / (B[0] - A[0])       # Slope of the line
      b = A[1] - m * A[0]                     # Bias of the line
      
      # To generate a weight vector with -1 bias value
      weight_func = np.array([b, m, -1])      
      
      # To generate N data points 
      X = generate_datapoints(N)
      
      # To calculate result of mult. of input and weight of nodes
      out_func = out_perceptron(X, weight_func)

      # It is added for Question 10
      if (Question_10 == True):
            weight_pla = weight_lin_reg
      else:
            weight_pla = np.zeros(3)    # To initialize weight vector as zeros
      
      counter = 0     # To count number of iterations in PLA
      
      while True:
      
            # To return output value of PLA's hypothesis
            out_pla = out_perceptron(X, weight_pla)     
            
            # It compares classification with outputs of f and h and returns boolean
            equivalent = out_func != out_pla            
            
            # Returns indices array where wrong classification by hypothesis h
            misclassification = np.where(equivalent)[0]             

            if misclassification.size == 0: 
                  break
            
            # To pick a random misclassified point from "equivalent" indices array
            random_choice = np.random.choice(misclassification)            

            # To update weight vector as real output calculated with f and X:
            weight_pla += out_func[random_choice] * X[random_choice].T
            counter += 1

            iterations_total += counter
            
            # To generate data "outside" of training data to calculate error
            N_outside = 1000

            # To generate new data array with size 1000x3
            X = generate_datapoints(N_outside)

            # To calculate output of perceptron with new dataset X
            output_f = out_perceptron(X, weight_func)
            output_g = out_perceptron(X, weight_pla)
            
            # To calculate misclassification ratio
            ratio_misclassification = ((output_f != output_g).sum()) / N_outside
            ratio_misclassification_total += ratio_misclassification

      iterations_avg = iterations_total / ITERATION

      ratio_misclassification_avg = ratio_misclassification_total / ITERATION

N = 10
PLA(N, False)
print("\nQuestion #4 - It takes ", iterations_avg, " iterations for N = ", N, " and ",
"the closest value for iterations taken on average is [b]15")

print("\nQuestion #5 - P(f(x)!=h(x)) for N = ", N, " is ", "%.2f" % ratio_misclassification_avg, " and ",
"the closest value for disagreement is [c]0.1")

N = 100
PLA(N, False)

print("\nQuestion #6 - It takes ", iterations_avg, " iterations for N = ", N, " and ",
"the closest value for iterations taken on average is [b]100")

print("\nQuestion #7 - P(f(x)!=h(x)) for N = ", N, " is ", "%.2f" % ratio_misclassification_avg, " and ",
"the closest value for disagreement is [c]0.01")





#############################################
#                                           #
#             Linear Regression             #
#                                           #
#############################################

# NOTE: Same functions used above does not explained again



# Question 8:

N_sample = 100
E_in_total = 0

for linear_regression in range(ITERATION):
    
    A = random(2)
    B = random(2)

    m = (B[1] - A[1]) / (B[0] - A[0])
    b = A[1] - m * A[0]  
    weight_func = np.array([b, m, -1])

    X = generate_datapoints(N_sample)           
    output_func = out_perceptron(X, weight_func)
        
    # To take pseudo-inverse of X
    X_pseudo_inverse = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    
    # To calculate weight
    weight_lin_reg = np.dot(X_pseudo_inverse, output_func)
    
    # To calculate output of the perceptron
    output_lin_reg = out_perceptron(X, weight_lin_reg)
        
    # To calculate E_in
    E_in = sum(output_lin_reg != output_func) / N_sample
    E_in_total += E_in

E_in_avg = E_in_total / ITERATION   # Average of E_in over 1000 iterations
print("\nQuestion #8 - Average of E_in over ", ITERATION, " iterations: ", "%.2f" % E_in_avg, 
      " and the closest value to the average E_in is [c]0.01")



# Question 9:

N_fresh = 1000
E_out_total = 0

for i in range(ITERATION):
    
    # To generate fresh datapoints
    X_test = generate_datapoints(N_fresh)

    # To calculate output of the function
    output_func_test = out_perceptron(X_test, weight_func)

    # To calculate output of the hypothesis
    output_lin_reg_test = out_perceptron(X_test, weight_lin_reg)
    
    E_out = sum(output_lin_reg_test != output_func_test) / N_fresh
    E_out_total += E_out

E_out_avg = E_out_total / ITERATION     # Average of E_out over 1000 iterations
print("\nQuestion #9 - Average of E_out over ", ITERATION, " iterations: ", "%.2f" % E_out_avg, 
      "and the closest value to the average E_out is [c]0.01")



# Question 10:
N = 10
PLA(N, True)
print("\nQuestion #10 - It takes ", iterations_avg, " iterations for N = ", N, " and ",
      "the closest value for iterations taken on average is [a]1")




"""
#############################################
#                                           #
#          Nonlinear Transformation         #
#                                           #
#############################################

# Question 11:

import matplotlib.pyplot as plt

N = 1000
E_in_total = 0

for run in range(ITERATION):
    
    # To generate a dataset
    X = generate_datapoints(N)
    
    # NOTE: [:,1] returns second column of the matrix
    output_func = np.sign(X[:,1] * X[:,1] + X[:,2] * X[:,2] - 0.6)

    # To pick a subset (10% of N)
    subset = list(range(N))               # To list values drom 1 to N which is 1000
    np.random.shuffle(subset)             # To shuffle the subset
    random_subset = subset[:(N // 10)]    # // used in order to get integer result

    # To flip sign of the output of the subset
    for i in random_subset:
        output_func[i] = output_func[i] * -1

    # Calculation of linear regression
    pseudo_inverse_X = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    weight_lin_reg = np.dot(pseudo_inverse_X, output_func)

    # To calculate E_in
    output_lin_reg = out_perceptron(X, weight_lin_reg)
    E_in = sum((output_lin_reg != output_func)) / N
    E_in_total += E_in
    
E_in_avg = E_in_total / ITERATION

print("\nQuestion #11 - Average of E_in over ", ITERATION, " iterations: ", "%.2f" % E_in_avg, 
      " and the closest value to the average E_in is [d]0.5")

# Create a plot of the classified points
plt.plot(X[:,1][output_func == 1], X[:,2][output_func == 1], 'ro')
plt.plot(X[:,1][output_func == -1], X[:,2][output_func == -1], 'bo')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()





# Question #12:

# To generate new nonlinear feature vector
X_new = np.array([np.ones(N), X[:,1], X[:,2],
                  X[:,1]*X[:,2], X[:,1]*X[:,1], X[:,2]*X[:,2]]).T

# Calculation of linear regression on the new feature matrix
pseudo_inverse_X = np.dot(np.linalg.inv(np.dot(X_new.T, X_new)), X_new.T)
weight_lin_reg = np.dot(pseudo_inverse_X, output_func)
print "\n\n\n", weight_lin_reg, "\n\n\n"
print type(weight_lin_reg)


# try the different hypotheses that are given
weight_g1 = np.array([-1, -0.05, 0.08, 0.13, 1.5, 1.5])
weight_g2 = np.array([-1, -0.05, 0.08, 0.13, 1.5, 15])
weight_g3 = np.array([-1, -0.05, 0.08, 0.13, 15, 1.5])
weight_g4 = np.array([-1, -1.5, 0.08, 0.13, 0.05, 0.05])
weight_g5 = np.array([-1, -0.05, 0.08, 1.5, 0.15, 0.15])

# compute classifications made by each hypothesis
output_lin_reg = out_perceptron(X_new, weight_lin_reg)

output_g1 = out_perceptron(X_new, weight_g1)
output_g2 = out_perceptron(X_new, weight_g2)
output_g3 = out_perceptron(X_new, weight_g3)
output_g4 = out_perceptron(X_new, weight_g4)
output_g5 = out_perceptron(X_new, weight_g5)

mismatch_1 = sum(output_g1 != output_lin_reg) / N
mismatch_2 = sum(output_g2 != output_lin_reg) / N
mismatch_3 = sum(output_g3 != output_lin_reg) / N
mismatch_4 = sum(output_g4 != output_lin_reg) / N
mismatch_5 = sum(output_g5 != output_lin_reg) / N

print("\nQuestion #12 - The closest hypothesis to the my found is [a]")

# To print only two digit after decimal for numpy arrays
np.set_printoptions(precision = 2)

print("My hypothesis is: ", weight_lin_reg)
print("The closest hypothesis [a] is: [-1 -0.05 +0.08 +0.13 +1.5 +1.5]")

# Create a plot of the classified points
plt.plot(X_new[:,1][output_func == 1], X_new[:,2][output_func == 1], 'ro')
plt.plot(X_new[:,1][output_func == -1], X_new[:,2][output_func == -1], 'bo')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()


# Question #13

N = 1000
E_out_total = 0

for run in range(ITERATION):
    
    # To generate a dataset
    X = generate_datapoints(N)

    # NOTE: [:,1] returns second column of the matrix
    output_func = np.sign(X[:,1] * X[:,1] + X[:,2] * X[:,2] - 0.6)

    # To pick a subset (10% of N)
    subset = list(range(N))               # To list values drom 1 to N which is 1000
    np.random.shuffle(subset)             # To shuffle the subset
    random_subset = subset[:(N // 10)]    # // used in order to get integer result

    # To flip sign of the output of the subset
    for i in random_subset:
        output_func[i] = output_func[i] * -1

    # To generate a new transformed feature matrix
    X_new = np.array([np.ones(N), X[:,1], X[:,2], X[:,1]*X[:,2], X[:,1]*X[:,1], X[:,2]*X[:,2]]).T
    
    # To compute classification made by my hypothesis from Problem 12
    output_lin_reg = out_perceptron(X_new, weight_lin_reg)
    
    # Compute disagreement between hypothesis and target function
    E_out = sum(output_lin_reg != output_func) / N
    E_out_total += E_out
    
E_out_avg = E_out_total / ITERATION

# Create a plot of the classified points
plt.plot(X[:,1][output_func == 1], X[:,2][output_func == 1], 'ro')
plt.plot(X[:,1][output_func == -1], X[:,2][output_func == -1], 'bo')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()

print("\nQuestion #13 - Average of E_out over ", ITERATION, " iterations: ", "%.2f" % E_out_avg, 
      " and the closest value to the average E_out is [b]0.1")