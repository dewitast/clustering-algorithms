from clustering.agglomerative import AgglomerativeClustering

ag = AgglomerativeClustering(2, "average group")
ag.fit([[0, 0], [1, 2], [0, 2], [1, 1]])
print(ag.labels)