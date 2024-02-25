import numpy as np

class SecondPriceAuction:
    def __init__(self, bids):
        self.bids = bids

    def find_winner_and_price(self):
        sorted_indices = np.argsort(self.bids)
        winner_index = sorted_indices[-1]
        second_highest_bid_index = sorted_indices[-2]
        winning_bid = self.bids[second_highest_bid_index]
        winner = winner_index
        return winner, winning_bid

# Example usage
bids = np.array([10, 20, 15, 5])  # Bids from different bidders
auction = SecondPriceAuction(bids)
winner, winning_price = auction.find_winner_and_price()

print("Winner:", winner)
print("Winning Price:", winning_price)
