import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist, squareform
import pandas as pd
from sklearn.decomposition import PCA

np.set_printoptions(precision = 1, suppress = True)
df = pd.read_csv('data_ca.csv', index_col = 0)

fig, ax = plt.subplots(figsize = (4,9))
for i in range(len(df)):
    ax.annotate(df.iloc[i].name, df.iloc[i].values,
    xytext = (5,-10), textcoords = 'offset points', size = 12, color = 'dimgrey')
df.plot.scatter(x='Infection Rate', y = 'Media Coverage Rate', ax = ax)
# plt.show()

df2 = pd.DataFrame(squareform(pdist(df)) ** 2, index = df.index, columns = df.index)
# print(df2)

# plt.figure(figsize = (5,2))
# plt.title('Hierarchical Clustering Dendrogram')
# plt.xlabel('Country')
# plt.ylabel('Distance')
# dendrogram(Z, p = 10, truncate_mode = 'lastp', labels = df.index.get_values(), leaf_font_size = 12)
# # plt.show()

Z = linkage(df, 'centroid', 'euclidean')
max_d = 10
clusters = fcluster(Z, max_d, criterion='distance')
print(clusters)

fig, ax = plt.subplots(figsize = (4,9))
for i in range(len(df)):
    ax.annotate(df.iloc[i].name, df.iloc[i].values,
    xytext = (5, -10), textcoords = 'offset points', size = 12, color = 'dimgrey')
df.plot.scatter(x = 'Infection Rate', y = 'Media Coverage Rate',
c = clusters, cmap = 'Set1', marker = 'D', ax = ax)
# plt.show()

k = 3
clusters = fcluster(Z, k, criterion = 'maxclust')
fig, ax = plt.subplots(figsize = (4,9))
for i in range(len(df)):
    ax.annotate(df.iloc[i].name, df.iloc[i].value,
    xytext = (5, -10), textcoords = 'offset points', size = 12, color = 'dimgrey')
df.plot.scatter(x = 'Infection Rate', y = 'Media Coverage Rate',
c = clusters, cmap = 'Set1', marker = 'D', ax = ax)
# plt.show()