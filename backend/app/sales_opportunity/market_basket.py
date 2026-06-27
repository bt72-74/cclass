from collections import defaultdict


def market_basket_analysis(transactions):
    pairs = defaultdict(int)

    for basket in transactions:
        products = list(set(basket))
        for i in range(len(products)):
            for j in range(i + 1, len(products)):
                pairs[(products[i], products[j])] += 1

    return dict(pairs)
