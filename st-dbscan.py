import math
from datetime import timedelta
from geopy.distance import great_circle
"""
input : 
    {d1,d2,d3.....dn} : data points in the database
    eps1 : minimum threshold for spatial data
    eps2 : minimum threshold for non-spatial data
    min_neighbours : minimum no of neighbours for a data point
    delta_e : threshold value to be included in the cluster
output : 
    cluster labels : {c1,c2,c3...cn}
"""

from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):

    R = 6372.8 # this is in miles.  For Earth radius in kilometers use 6372.8 km and for miles 3959.87433

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c
def retrieve_neighbours(cluster_index, df, eps1, eps2):
    neighbourhood = []
    center_point = df.loc[cluster_index]
    #filter by time
    min_time  = center_point['Date'] - timedelta(minutes=eps2)
    max_time = center_point['Date'] + timedelta(minutes=eps2)
    df = df[(df['Date']>=min_time) & (df['Date']<=max_time)]

    #filter now by distance
    for index, point in df.iterrows():
        if index!=cluster_index:
            distance = haversine(center_point['Latitude'], center_point['Longitude'], point['Latitude'], point['Longitude'])
            if distance <= eps1:
                neighbourhood.append(index)
    return neighbourhood

def st_dbscan(df, eps1, eps2, min_neighbours, delta_e):
    cluster_label = 0
    noise = -1
    UNMARKED = -2
    stack = []
    
    df['cluster'] = UNMARKED
    for index, point in df.iterrows():
        if df.iloc[index]['cluster'] == UNMARKED:
            X = retrieve_neighbours(index, df, eps1, eps2)
            if len(X) <= min_neighbours:
                df.at[index,'cluster'] = noise
            else : 
                cluster_label = cluster_label + 1
                df.at[index,'cluster'] = cluster_label
                for x in X:
                    df.at[x,'cluster'] = cluster_label
                    stack.append(x)
                while(len(stack)>0):
                    current_index_point = stack.pop()
                    new_neighbour = retrieve_neighbours(current_index_point, df, eps1, eps2)
                    if len(new_neighbour)>=min_neighbours:
                        for n in new_neighbour:
                            neigh_cluster = df.loc[n]['cluster']
                            # cluster_avg = (df[df['cluster']==cluster_label]['Date']).mean()
                            if (neigh_cluster != noise or neigh_cluster != UNMARKED):
                                df.at[n, 'cluster'] = cluster_label
                                stack.append(n)
    
    return df            


            