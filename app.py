import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from distance import mathDistance # Own Function

C1 = [3,4,4,5,5,6,7,8,7,9]
C2 = [2,1,3,1,4,5,6,4,2,1]
CATEGORY = ['GOOD','GOOD','GOOD', 'GOOD', 'GOOD', 'BAD', 'BAD', 'BAD', 'BAD', 'BAD']
data = list(zip(C1,C2))
dataCategory = list(zip(C1,C2,CATEGORY))

r = (6,3)

distance = []
print('\nDISTANCE')
for x in data:
    result = mathDistance(x,r)
    distance.append(float(result))
    print(result)
print('DISTANCE\n')

# Sort the data by distance, K = 7. Take 7 distance
print("SORT DISTANCE")
K = 7
num = 0
distance.sort()
for x in distance:
    print(x)
    num += 1
    if num == K:
        break
print("SORT DISTANCE")








# K (n_clusters=3)

inertia = []

data = list(zip(C1,C2))

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(C1,C2, c=kmeans.labels_)
plt.show()


