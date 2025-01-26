import numpy as np
import matplotlib.pyplot as plt
from utils import *

%matplotlib inline

# Load the dataset
X_train, X_val, y_val = load_data()
# Display the first five elements of X_train
print("The first 5 elements of X_train are:\n", X_train[:5])
# Display the first five elements of y_val
print("The first 5 elements of y_val are\n", y_val[:5])
# Display the first five elements of y_val
print("The first 5 elements of y_val are\n", y_val[:5])
print ('The shape of X_train is:', X_train.shape)
print ('The shape of X_val is:', X_val.shape)
print ('The shape of y_val is: ', y_val.shape)
# Visualize the data:
# Create a scatter plot of the data. To change the markers to blue "x",
# we used the 'marker' and 'c' parameters
plt.scatter(X_train[:, 0], X_train[:, 1], marker='x', c='b')

# Set the title
plt.title("The first dataset")
# Set the y-axis label
plt.ylabel('Throughput (mb/s)')
# Set the x-axis label
plt.xlabel('Latency (ms)')
# Set axis range
plt.axis([0, 30, 0, 30])
plt.show()
'''
Gaussian distribution
To perform anomaly detection, you will first need to fit a model to the data’s distribution.
Given a training set  {𝑥(1),...,𝑥(𝑚)}
  you want to estimate the Gaussian distribution for each of the features  𝑥𝑖
Recall that the Gaussian distribution is given by:
𝑝(𝑥;𝜇,𝜎2)=1/Square_root(2𝜋𝜎2) * exp−(𝑥−𝜇)2/2𝜎2

sigma square = variance.

Estimating parameters for a Gaussian distribution
Implementation:
# mu is calculated as the mean of each feature (column) in the dataset.
# var is calculated as the variance of each feature (column) in the dataset.
'''


# UNQ_C1
# GRADED FUNCTION: estimate_gaussian

def estimate_gaussian(X):
    """
    Calculates mean and variance of all features
    in the dataset

    Args:
        X (ndarray): (m, n) Data matrix

    Returns:
        mu (ndarray): (n,) Mean of all features
        var (ndarray): (n,) Variance of all features
    """

    m, n = X.shape

    ### START CODE HERE ###
    mu = np.mean(X, axis=0)
    var = np.var(X, axis=0)
    ### END CODE HERE ###

    return mu, var


# Estimate mean and variance of each feature
mu, var = estimate_gaussian(X_train)

print("Mean of each feature:", mu)
print("Variance of each feature:", var)

# UNIT TEST
from public_tests import *

estimate_gaussian_test(estimate_gaussian)

# Returns the density of the multivariate normal
# at each data point (row) of X_train
p = multivariate_gaussian(X_train, mu, var)

#Plotting code
visualize_fit(X_train, mu, var)

'''
Selecting the threshold  𝜖
Now can investigate which examples have a very high probability given this distribution and which examples have a very low probability.
The low probability examples are more likely to be the anomalies in our dataset.
One way to determine which examples are anomalies is to select a threshold based on a cross validation set.
In this section, we can complete the code in `select_threshold` to select the threshold $\varepsilon$ using the $F_1$ score on a cross validation set.
Recall that if an example  𝑥
  has a low probability  𝑝(𝑥)<𝜀
 , then it is classified as an anomaly.

Then, you can compute precision and recall by:
𝑝𝑟𝑒𝑐𝑟𝑒𝑐==𝑡𝑝𝑡𝑝+𝑓𝑝𝑡𝑝𝑡𝑝+𝑓𝑛,
The  𝐹1
  score is computed using precision ( 𝑝𝑟𝑒𝑐
 ) and recall ( 𝑟𝑒𝑐
 ) as follows:
𝐹1=2⋅𝑝𝑟𝑒𝑐⋅𝑟𝑒𝑐𝑝𝑟𝑒𝑐+𝑟𝑒𝑐
'''


# UNQ_C2
# GRADED FUNCTION: select_threshold

def select_threshold(y_val, p_val):
    """
    Finds the best threshold to use for selecting outliers
    based on the results from a validation set (p_val)
    and the ground truth (y_val)

    Args:
        y_val (ndarray): Ground truth on validation set
        p_val (ndarray): Results on validation set

    Returns:
        epsilon (float): Threshold chosen
        F1 (float):      F1 score by choosing epsilon as threshold
    """

    best_epsilon = 0
    best_F1 = 0
    F1 = 0

    step_size = (max(p_val) - min(p_val)) / 1000

    for epsilon in np.arange(min(p_val), max(p_val), step_size):

        ### START CODE HERE ###
        predictions = (p_val < epsilon).astype(int)

        tp = np.sum((predictions == 1) & (y_val == 1))
        fp = np.sum((predictions == 1) & (y_val == 0))
        fn = np.sum((predictions == 0) & (y_val == 1))

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0

        F1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        ### END CODE HERE ###

        if F1 > best_F1:
            best_F1 = F1
            best_epsilon = epsilon

    return best_epsilon, best_F1


p_val = multivariate_gaussian(X_val, mu, var)
epsilon, F1 = select_threshold(y_val, p_val)

print('Best epsilon found using cross-validation: %e' % epsilon)
print('Best F1 on Cross Validation Set: %f' % F1)

# UNIT TEST
select_threshold_test(select_threshold)


# Find the outliers in the training set
outliers = p < epsilon

# Visualize the fit
visualize_fit(X_train, mu, var)

# Draw a red circle around those outliers
plt.plot(X_train[outliers, 0], X_train[outliers, 1], 'ro',
         markersize= 10,markerfacecolor='none', markeredgewidth=2)


'''
High dimensional dataset
run the anomaly detection algorithm that you implemented on a more realistic and much harder dataset.
In this dataset, each example is described by 11 features, capturing many more properties of your compute servers.

Let's start by loading the dataset.

- The `load_data()` function shown below loads the data into variables `X_train_high`, `X_val_high` and `y_val_high`
    -  `_high` is meant to distinguish these variables from the ones used in the previous part
    - We will use `X_train_high` to fit Gaussian distribution 
    - We will use `X_val_high` and `y_val_high` as a cross validation set to select a threshold and determine anomalous vs normal examples
'''

print ('The shape of X_train_high is:', X_train_high.shape)
print ('The shape of X_val_high is:', X_val_high.shape)
print ('The shape of y_val_high is: ', y_val_high.shape)

'''
Anomaly detection
Now, let's run the anomaly detection algorithm on this new dataset.

The code below will use your code to

Estimate the Gaussian parameters ( 𝜇𝑖
  and  𝜎2𝑖
 )
Evaluate the probabilities for both the training data X_train_high from which you estimated the Gaussian parameters, 
as well as for the the cross-validation set X_val_high.
Finally, it will use select_threshold to find the best threshold  𝜀.
'''

# Apply the same steps to the larger dataset

# Estimate the Gaussian parameters
mu_high, var_high = estimate_gaussian(X_train_high)

# Evaluate the probabilites for the training set
p_high = multivariate_gaussian(X_train_high, mu_high, var_high)

# Evaluate the probabilites for the cross validation set
p_val_high = multivariate_gaussian(X_val_high, mu_high, var_high)

# Find the best threshold
epsilon_high, F1_high = select_threshold(y_val_high, p_val_high)

print('Best epsilon found using cross-validation: %e'% epsilon_high)
print('Best F1 on Cross Validation Set:  %f'% F1_high)
print('# Anomalies found: %d'% sum(p_high < epsilon_high))
