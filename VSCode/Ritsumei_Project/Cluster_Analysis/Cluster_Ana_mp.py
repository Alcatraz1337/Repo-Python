import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist, squareform
import pandas as pd
from sklearn.decomposition import PCA
import seaborn as sns

df = pd.read_csv('data_ca2.csv', index_col=0)
print(df.head())

#1
# relative_pic = sns.pairplot(df, vars = ['A','B','C','D','E','F','G','H','I','J'])
# plt.show()

pca = PCA(n_components=2)
pca.fit(df)
df_pca = pd.DataFrame(pca.transform(df), columns = ['PCA%i' % i for i in range(2)], index = df.index)

fig, ax = plt.subplots()
df_pca.plot.scatter(x = 'PCA0', y = 'PCA1', marker = 'D', ax = ax)
plt.show()

#2
Z = linkage(df, 'centroid', 'euclidean')

plt.figure(figsize = (10, 4))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data')
plt.ylabel('Distance')
dendrogram(Z, p = 3, truncate_mode = 'lastp', labels = df.index.get_values(), leaf_font_size = 12)
plt.show()

#3
fig, ax = plt.subplots()
k = 3
clusters = fcluster(Z, k, criterion = 'maxclust')
print(clusters)

#4
df_pca.plot.scatter(x = 'PCA0', y = 'PCA1', c = clusters, cmap = 'Set1', marker = 'D', ax = ax)
plt.show()