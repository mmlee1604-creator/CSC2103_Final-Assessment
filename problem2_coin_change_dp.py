# ============================================================
# Problem 2: Optimise Cash Change Distribution Using
# Dynamic Programming Based on the Coin Change Problem
# ============================================================

# Returns the minimum number of coins required & selected coins combination
def coin_change(coins, amount):
    # Assign an infinite value to represent an unreachable solution
    INF = float('inf')

    # DP table:
    # dp[i] = minimum number of coins required to make amount i
    dp = [INF] * (amount + 1)

    # Used to record last selected coin for each amount
    selected_coin = [-1] * (amount + 1)

    # Base case: 0 coins are required to make amount 0
    dp[0] = 0

    # ==Dynamic Programming calculation==
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                # If using this coin gives a better solution, update the DP table and record the coin used
                if dp[current_amount - coin] + 1 < dp[current_amount]:
                    dp[current_amount] = dp[current_amount - coin] + 1
                    selected_coin[current_amount] = coin

    # No solution exists
    if dp[amount] == INF:
        return None, None

    # ==Reconstruct selected coins==
    result_coins = []
    current = amount

    while current > 0:
        coin = selected_coin[current]

        if coin == -1:
            return None, None

        result_coins.append(coin)
        current -= coin

    return dp[amount], result_coins

def display_result(amount, coins, minimum_coins, selected_coins):
    print("\n============= Cash Change Result =============")
    print(f"Target Change Amount: RM{amount}")
    print(f"Available Coin Denominations: {coins}")

    if minimum_coins is None:
        print("No possible combination can form this amount.")

    else:
        print(f"\nMinimum Number of Coins: {minimum_coins}")
        print("Coins Used:")
        print(" + ".join(
            [f"RM{coin}" for coin in selected_coins]
        ))

    print("==============================================")

def main():
    while True:
        print("==============================================")
        print(" Cash Change Distribution System ")
        print(" Dynamic Programming - Coin Change Problem")
        print("==============================================")

        # ==User Input Section==
        coins_input = input("Enter available coin denominations (separated by space): ")

        coins = []

        try:
            for value in coins_input.split():
                coin = int(value)

                if coin <= 0:
                    print("Coin denominations must be positive.")
                    print()
                    continue

                coins.append(coin)

            if len(coins) == 0:
                print("No valid coin denominations entered.")
                print()
                continue

        except ValueError:
            print("Invalid coin input.")
            print()
            continue

        try:
            amount = int(input("Enter required change amount: "))

            if amount <= 0:
                print("Amount must be positive.")
                print()
                continue

        except ValueError:
            print("Invalid amount.")
            print()
            continue

        # Run Dynamic Programming Algorithm
        minimum_coins, selected_coins = coin_change(coins, amount)
        # Display Output
        display_result(amount, coins, minimum_coins, selected_coins)

        run_again = input("Do you want to run the program again? (y/n): ")

        if run_again.lower() != 'y':
            print("Thank you for using the Cash Change Distribution System. Goodbye!")
            break

        print()

# Program execution
if __name__ == "__main__":
    main()