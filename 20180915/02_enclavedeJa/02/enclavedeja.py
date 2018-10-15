prices = {
        0: 3.0,
        1: 3.5,
        2: 4,
        3: 4.5,
        4: 5
        }

discount_factor = {
        1: 1.0,
        2: 1.0,
        3: 0.9,
        4: 0.8
        }

def get_series(seasons):
    current_series = []
    for season in seasons:
        if (season in current_series) or (len(current_series) and season < current_series[-1]):
            yield current_series
            current_series = []
        current_series.append(season)
    else:
        if current_series:
            yield current_series

def get_price(seasons):
    total = 0.0

    for series in get_series(seasons):
        price = sum(prices[season] for season in series)
        # Default discount: 30%, for more than 4 different seasons
        discount = discount_factor.get(len(series), 0.7)
        total += price * discount

    return total
