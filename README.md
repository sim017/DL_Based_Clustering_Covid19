
# DL_Based_Clustering_Covid19

The spread of the covid cases held a devastating effects on the health of the people, mankind and economic policies of various countries. Although, various institutions and countries did keep a track of the increase in covid cases and other statistics, it just gave us a number and the most we could do to take care of the further increase in the number of the cases was to cut off the human contact completely. Here, the issue of the spread of the cluster is tackled. Various approaches to define this spatial and time series problem statement is discussed. The end result would be that we can then predict the spread of the covid clusters and to track it's movement.

For initial clustering of the covid19 data and to visualise the spread of the covid19 disease iniatially the DBSCAN algorithm is used to plot the clusters with fields  - ['latitude','longitude','date'].

This is actually a time series data with higher dimensions. The issue with the DBSCAN is as shown in the notebook "DBSCAN.ipynb" - The data points are not clustered together properly where the density varies. DBSCAN takes two parameters into consideration - epsilon (this is the minimum distance between the points so that the points can be considered as the core points, boundary points or noise) and min_points (The number of the neighbours for the point to be considered as the core points, border and noise). With these two parameters the DBSCAN algorithm is capable of clustering the datapoints according to the density but it shows inaccurate results with varying density.

In order to address the above issue a variation of DBSCAN - HDBSCAN is further used to cluster the data. The main advantage of this is that we can cluster the points belonging to the different densities as well. The parameters - epsilon can be optional. The results can be viewed in the python notebooks - "clustering for time series data." The issue with the hdbscan is that it is was clustering the data points according to the varying densities and thus smaller clusters too were formed. As a result of this the no of clusters were increased. Again a variation of this - hdbscan with dbscan is used that makes the use of epsilon. 

# Comparison between HDBSCAN and DBSCAN

While the DBSCAN and HDBSCAN have their different applications yet their performances can be compared. It also depends upon the distribution of the data. DBSCAN is able to cluster the data based upon the density and HDBSCAN can cluster the same data points although they do belong to different density and yet hold similar properties. The capability of both the processes can be combined and we can then compare the performances of the above approaches as later described in the jupyter notebook. 

# Use of the convex hull 

After clustering the data points, the convex hull can be used to draw a boundary around the separate clusters. The data points in the convex hull can then be increased or decreased depending upon the spread of the clusters. The challenge here lies in the prediction of different labels on each day. This is tackled by keeping a track of the previous labels of the data points. The newly predicted labels then can be compared and accordingly the new labels can be adjusted. The variance and the distance between the farthest points in the convex hull can give a fair idea about the spread of the covid clusters.

# Use of the DTW

For each covid cluster the centroid is found. This is essential because with each increase or decrease of the cluster the centroid points will change. The path of the centroid is then traced to find the direction of the covid clusters movement.

# The application of this approach

One of the basic applications of this approach can be used to analyse the spread of the pandemic. This will help us in concentrating our energy in one spatial area and tackle the problems over there. Moreover, the resources can be efficiently utilised at these red zones. 
