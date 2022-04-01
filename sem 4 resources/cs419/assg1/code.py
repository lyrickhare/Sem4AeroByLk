import numpy as np
import pandas as pd
import matplotlib

""" 
You are allowed to change the names of function "arguments" as per your convenience, 
but it should be meaningful.

E.g. y, y_train, y_test, output_var, target, output_label, ... are acceptable
but abc, a, b, etc. are not.
"""

def get_labeled_features(file_path):
    """Read data from train.csv and split into train and dev sets. Do any
       preprocessing/augmentation steps here and return final features.
    diamonds_df = pd.read_csv("train.csv")
    Args:
        file_path (str): path to train.csv

    Returns:
        phi_train, y_train, phi_dev, y_dev
    """
    
    return phi_train, y_train, phi_dev, y_dev5

def get_test_features(file_path):
    """Read test data, perform required preproccessing / augmentation
       and return final feature matrix.

    Args:
        file_path (str): path to test.csv

    Returns:
        phi_test: matrix of size (m,n) where m is number of test instances
                  and n is the dimension of the feature space.
    """
    
    return phi_test

def compute_RMSE(phi, w , y) :
   """Return root mean squared error given features phi, and true labels y."""
   
   return error

def generate_output(phi_test, w):
   """writes a file (output.csv) containing target variables in required format for Submission."""

   pass
    
   
def closed_soln(phi, y):
    """Function returns the solution w for Xw = y."""
    return np.linalg.pinv(phi).dot(y)
   
def gradient_descent(phi, y, phi_dev, y_dev) :
   # Implement gradient_descent using Mean Squared Error Loss
   # You may choose to use the dev set to determine point of convergence

   return w

def sgd(phi, y, phi_dev, y_dev) :
   # Implement stochastic gradient_descent using Mean Squared Error Loss
   # You may choose to use the dev set to determine point of convergence

   return w


def pnorm(phi, y, phi_dev, y_dev, p) :
   # Implement gradient_descent with p-norm regularization using Mean Squared Error Loss
   # You may choose to use the dev set to determine point of convergence

    return w   


def main():
    """ 
    The following steps will be run in sequence by the autograder.
    """
    ######## Task 2 #########
    phi, y, phi_dev, y_dev = get_labeled_features('train.csv')
    w1 = closed_soln(phi, y)
    w2 = gradient_descent(phi, y, phi_dev, y_dev)
    r1 = compute_RMSE(phi_dev, w1, y_dev)
    r2 = compute_RMSE(phi_dev, w2, y_dev)
    print('1a: ')
    print(abs(r1-r2))
    w3 = sgd(phi, y, phi_dev, y_dev)
    r3 = compute_RMSE(phi_dev, w3, y_dev)
    print('1c: ')
    print(abs(r2-r3))

    ######## Task 3 #########
    w_p2 = pnorm(phi, y, phi_dev, y_dev, 2)  
    w_p4 = pnorm(phi, y, phi_dev, y_dev, 4)  
    r_p2 = compute_RMSE(phi_dev, w_p2, y_dev)
    r_p4 = compute_RMSE(phi_dev, w_p4, y_dev)
    print('2: pnorm2')
    print(r_p2)
    print('2: pnorm4')
    print(r_p4)

    ######## Task 6 #########
    
    # Add code to run your selected method here
    # print RMSE on dev set with this method

main()