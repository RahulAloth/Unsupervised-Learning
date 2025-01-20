
##Notes on unsupervised learning:
Clustering Algorithms: Learn how to group data into clusters.
Anomaly Detection: Understand how to identify unusual data points.
Applications: These techniques are widely used in commercial applications
### K-mean square algorithm
The K-means clustering algorithm is used to partition a dataset into clusters. Here’s a step-by-step 
example with 30 unlabeled data points:
####Initialization:
The algorithm starts by randomly selecting two points as the initial cluster centroids (red and blue crosses).
####Assignment Step: 
Each data point is assigned to the nearest cluster centroid. This is done by calculating the distance
of each point to the red and blue centroids and coloring the points accordingly (red or blue).
####Update Step: 
The centroids are recalculated by taking the average of all points assigned to each cluster. 
The red centroid moves to the average location of the red points, and the blue centroid moves to the average 
location of the blue points.
####Iteration: 
Steps 2 and 3 are repeated. Points are reassigned to the nearest centroid based on the updated positions,
and the centroids are recalculated. This process continues until the centroids no longer move significantly.
The algorithm repeatedly assigns points to the nearest centroid and updates the centroids’ positions until 
convergence. This results in the data being partitioned into clusters based on proximity to the centroids.
####Optimization objectives:
The K-means algorithm also optimizes a specific cost function, but it uses a different optimization method.
The K-means algorithm aims to find the best assignments of points to cluster centroids and the optimal locations of these centroids to minimize the squared distance between points and their assigned centroids.
#####Optimization Steps:
######Assignment Step: 
Assign each training example to the nearest cluster centroid to minimize the squared distance.
######Update Step: 
Recalculate the centroids as the mean of the points assigned to each cluster to further reduce the cost function
##### Iterative Process:
The algorithm iteratively updates the cluster assignments and centroid positions to continuously reduce the cost function until it converges to a minimum value.
During the run of K-means, the algorithm measures the distances between points and centroids, computes the squares of these distances, and averages them to get the cost function value.
The algorithm updates the cluster assignments and centroid positions to minimize this cost function, effectively reducing the average squared distance between points and their assigned centroids.
This process ensures that the points are grouped into clusters with minimal variance, making the clusters as compact and distinct as possible.

#####Initializing Cluster Centroids in K-means
Random Initialization:
The first step in the K-means algorithm is to choose random locations for the initial cluster centroids, denoted as μ1, μ2,... μn
A common method is to randomly select K training examples from the dataset and use their locations as the initial centroids.
Choosing K:
Ensure that the number of cluster centroids K is less than the number of training examples m. For example, if K=2 and m=30, you randomly pick two training examples as initial centroids.
Example:
If you randomly pick two training examples, you might initialize the red cluster centroid at one point and the blue cluster centroid at another.
This method differs from initializing centroids at random points not corresponding to training examples, which was used in earlier illustrations for clarity.
Multiple Initializations:
Different random initializations can lead to different clustering results. Some initializations might result in better clustering than others.
For instance, initializing centroids within dense groups of points might lead to suboptimal clustering, known as local optima.
To improve results, run K-means multiple times with different random initializations and choose the best clustering based on the cost function.
Local Optima:
K-means can get stuck in local minima, where the clustering is not optimal.
By trying multiple random initializations, you increase the chances of finding a better clustering solution.
This approach helps in finding a more accurate and stable clustering by mitigating the impact of poor initial centroid choices.

Deciding the number of clusters, ( k ), for the k-means algorithm can be ambiguous. Different people might see different numbers of clusters in the same dataset. Here are some key points to consider:

Ambiguity in Clustering: The right value of ( k ) can be ambiguous. Different observers might see different numbers of clusters in the same data, and both could be correct.
Elbow Method: One technique to choose ( k ) is the elbow method. Run k-means with various ( k ) values and plot the cost function ( J ) against ( k ). The “elbow” point, where the cost function decreases sharply and then levels off, suggests a good ( k ). However, this method isn’t always clear-cut.
Downstream Purpose: Often, the choice of ( k ) depends on the downstream application. For example, in t-shirt sizing, you might choose ( k ) based on practical needs (e.g., small, medium, large vs. extra small, small, medium, large, extra large).
Avoid Minimizing Cost Function: Choosing ( k ) to minimize the cost function ( J ) isn’t effective, as it tends to favor the largest possible ( k ).
