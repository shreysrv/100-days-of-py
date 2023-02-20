import art

print(art.logo)
end_condition = "yes"
user_bids = []


def add_bid():
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    user_bid = {"name": name, "bid": bid}
    user_bids.append(user_bid)


def top_bid():
    max_bid = 0
    winner = ""
    for user_bid in user_bids:
        bid = user_bid["bid"]
        if bid > max_bid:
            max_bid = user_bid["bid"]
            winner = user_bid["name"]
    return {"name": winner, "bid": max_bid}


while end_condition != "no":
    add_bid()
    end_condition = input("Are there any other bidders? Type 'yes' or 'no'.\n")
winner_bid = top_bid()
print(f"The winner is {winner_bid['name']} with a bid of ${winner_bid['bid']}")
