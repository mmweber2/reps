# Hackerrank's Bon Appetit challenge.

def owed_amount(not_eaten, prices, amt_charged):
    """Print the amount owed to Anna, or Bon Appetit if nothing is owed.

    If amt_charged exceeds what Anna actually owes for her half of the bill,
    considering that she did not eat one item, prints the difference.
    Otherwise, prints "Bon Appetit".

    Args:
        not_eaten: integer, the 0-based index of the single food item,
            listed in prices, that Anna did not eat. 

        prices: list of integers, the list of prices for the foods in the meal.

        amt_charged: integer, the amount Anna paid for her share of the bill.
    """
    owed = (sum(prices) - prices[not_eaten]) / 2
    if owed == amt_charged:
        print "Bon Appetit"
        return
    print amt_charged - owed
