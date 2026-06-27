def up_sell_suggestions(product_id):
    mapping = {
        1: [100],   # نسخه Pro
        4: [40],    # نسخه Premium
        10: [50]    # نسخه Advanced
    }
    return mapping.get(product_id, [])
