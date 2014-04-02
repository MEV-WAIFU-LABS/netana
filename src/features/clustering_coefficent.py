import networkx as nx


def clust(network):
    net = network.to_undirected()
    c = nx.average_clustering(net)
    return round(c, 3)
