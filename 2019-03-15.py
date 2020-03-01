# PROBLEM
# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
#
# SOLUTION
# Generally, using higher valued coins makes us reach for the desired amount quicker, meaning fewer coins used.
# Starting from the highest valued coin, how many of these coins can "fit" into the amount we want to reach. If this is
# a positive valued number, subtract this total value from the current amount of cents we want to reach. If the coin
# cannot "fit" into the amount, move on to the next coin. Do this until the current amount becomes 0 (this is assumed
# to happen because the smallest in value coin should be the lowest common denominator of every possible amount of
# cents. This problem has a time complexity of O(n) where n is the amount of different coin types. The amount of cents
# we want to reach does not affect the time to solve the problem with any real significance.


coin_types = [1, 5, 10, 25]  # What type of coins exist
input_amount = 16  # The total amount of cents we want to reach

if __name__ == '__main__':
    current_amount = input_amount
    coin_using_index = len(coin_types) - 1
    needed_coins = 0
    while current_amount > 0:

        # Make sure to select a valid coin
        while current_amount < coin_types[coin_using_index]:
            coin_using_index -= 1

        # Calculate the amount of coins of the selected type can "fit" into the current_amount.
        total_fits = current_amount // coin_types[coin_using_index]

        # Remove from the current_amount the total amount these coins are amount to.
        current_amount -= total_fits * coin_types[coin_using_index]

        # Update the final answer
        needed_coins += total_fits

    print(needed_coins)
