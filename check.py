import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



# Add Data
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]


data = list(zip(x,y))

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x,y, c=kmeans.labels_)
plt.show()

print(data)


# In order to find the best value for K, 
# we need to run K-means across our data for a range of possible values. 
# We only have 10 data points, so the maximum number of clusters is 10. 
# So for each value K in range(1,11), we train a K-means model and plot the intertia at that number of clusters

inertias = []
# this depends on the total data you have, in this case we have 10 data. that means we use (1,11)

# THIS IS JUST FOR CHECKING WHAT IS THE BEST 'K' VALUE WE SHOULD USE
# for i in range(1,11):
    # kmeans = KMeans(n_clusters=i)
    # kmeans.fit(data)
    # inertias.append(kmeans.inertia_)
# THIS IS JUST FOR CHECKING WHAT IS THE BEST 'K' VALUE WE SHOULD USE



# plt.plot(range(1,11), inertias, marker='o')
# plt.title('Elbow method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()

