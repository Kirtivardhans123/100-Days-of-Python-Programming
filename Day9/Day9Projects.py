import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def secret_auction():
    """Handles the secret auction process."""
    print("Welcome to the Secret Auction Program!")
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        # Get bidder's name and bid amount
        name = input("Enter your name: ")
        bid = int(input("Enter your bid amount: $"))

        # Store the bid in the dictionary
        bids[name] = bid

        # Ask if there are more bidders
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == 'no':
            bidding_finished = True
        elif should_continue == 'yes':
            clear_screen()

    # Find the highest bidder
    highest_bidder = max(bids, key=bids.get)
    highest_bid = bids[highest_bidder]

    # Announce the winner
    print("\nAuction Results:")
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")

# Run the secret auction program
secret_auction()
