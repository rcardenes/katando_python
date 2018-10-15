prices = {
        0: 2.5,
        1: 3.0,
        2: 3.5,
        3: 4.0,
        4: 4.5,
        5: 5.0
        }

discount_factor = {
        1: 1.0,
        2: 1.0,
        3: 0.9,
        4: 0.8
        }

no_discount = { 5 }

def get_series(seasons):
    current_series = []
    for season in seasons:
        if (season in current_series) or (len(current_series) and season < current_series[-1]):
            yield set(current_series)
            current_series = []
        current_series.append(season)
    else:
        if current_series:
            yield set(current_series)

def partial_price(seasons):
    return sum(prices[season] for season in seasons)

def get_price(seasons):
    total = 0.0

    for series in get_series(seasons):
        # Default discount: 30%, for more than 4 different seasons
        discounted = series - no_discount
        not_discounted = series & no_discount
        discount = discount_factor.get(len(series), 0.7)
        print(discounted, partial_price(discounted), discount)
        print(not_discounted, partial_price(not_discounted))
        total += partial_price(discounted) * discount + partial_price(not_discounted)

    return total
