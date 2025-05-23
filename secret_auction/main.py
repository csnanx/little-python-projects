from art import gavel_art

print(gavel_art)
print("Welcome to The Secret Auction")

auction_data = {}
other_bidders = True

while other_bidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_data[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if more_bidders == "no":
        other_bidders = False
    elif more_bidders == "yes":
        print("\n" * 50)
