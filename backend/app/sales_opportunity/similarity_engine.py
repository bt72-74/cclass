import numpy as np


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def find_similar_customers(target_vec, all_vectors, top_n=5):
    sims = []
    for cid, vec in all_vectors.items():
        sims.append((cid, cosine_similarity(target_vec, vec)))

    sims.sort(key=lambda x: x[1], reverse=True)
    return sims[:top_n]
