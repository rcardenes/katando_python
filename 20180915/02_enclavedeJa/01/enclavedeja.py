discount_factor = {
        1: 1.0,
        2: 1.0,
        3: 0.9,
        4: 0.9
        }


def get_price(seasons):
    nseasons = len(seasons)
    # Default discount: 0.8, for more than 4 seasons
    discount = discount_factor.get(nseasons, 0.8)
    return nseasons * 5 * discount
