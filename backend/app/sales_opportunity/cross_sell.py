def cross_sell_suggestions(product_id):
    mapping = {
        1: [2, 3],
        4: [5],
        10: [11, 12]
    }
    return mapping.get(product_id, [])
