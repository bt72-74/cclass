import networkx as nx


def build_product_graph(pairs):
    G = nx.Graph()
    for (p1, p2), weight in pairs.items():
        G.add_edge(p1, p2, weight=weight)
    return G


def get_related_products(G, product_id, top_n=5):
    if product_id not in G:
        return []

    neighbors = G[product_id]
    sorted_neighbors = sorted(neighbors.items(), key=lambda x: x[1]["weight"], reverse=True)
    return [n[0] for n in sorted_neighbors[:top_n]]
