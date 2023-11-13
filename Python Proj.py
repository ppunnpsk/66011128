import random

bankroll = 0
while True:
    try:
        bankroll = int(input("What is your starting balance (in whole $$): "))
        if bankroll < 10:
            print("Sorry, the minimum starting balance is $10. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

total_win = 0
total_bet = 0

def spins():
    slots = {
        '00': 'green', '0': 'green', '1': 'red', '2': 'black',
        '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
        '8': 'black', '9': 'red', '10': 'black', '11': 'red',
        '12': 'black', '13': 'red', '14': 'black', '15': 'red',
        '16': 'black', '17': 'red', '18': 'black', '19': 'red',
        '20': 'black', '21': 'red', '22': 'black', '23': 'red',
        '24': 'black', '25': 'red', '26': 'black', '27': 'red',
        '28': 'black', '29': 'red', '30': 'black', '31': 'red',
        '32': 'black', '33': 'red', '34': 'black', '35': 'red',
        '36': 'black'
    }

    result = random.choice(list(slots.keys()))
    color = slots[result]
    return result, color, slots

def bet_value(bet_type):
    if bet_type == 1:
        bet_val = int(input("Is it an EVEN (1) or an ODD (2) bet?: "))
        return bet_val
    if bet_type == 2:
        bet_val = int(input("Is it a RED (1) or a BLACK (2) bet?: "))
        return bet_val
    if bet_type == 8:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        return bet_list
    if bet_type == 9:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        num3 = int(input("What is your third number?: "))
        bet_list.append(num3)
        return bet_list
    if bet_type == 10:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        num3 = int(input("What is your third number?: "))
        bet_list.append(num3)
        num4 = int(input("What is your fourth number?: "))
        bet_list.append(num4)
        return bet_list
    if bet_type == 11:
        bet_list = []
        num1 = int(input("What is your first number?: "))
        bet_list.append(num1)
        num2 = int(input("What is your second number?: "))
        bet_list.append(num2)
        num3 = int(input("What is your third number?: "))
        bet_list.append(num3)
        num4 = int(input("What is your fourth number?: "))
        bet_list.append(num4)
        num5 = int(input("What is your fifth number?: "))
        bet_list.append(num5)
        num6 = int(input("What is your sixth number?: "))
        bet_list.append(num6)
        return bet_list
    if bet_type == 12:
        bet_list = ['00', '0', '1', '2', '3']
        return bet_list
    if bet_type == 13:
        bet_val = input("What number do you want to choose 00, 0, 1-36?: ")
        return bet_val


def adjusted_bankroll(spins_result, balance, bet_val):
    result, color, slots = spins_result
    balance -= bet
    # Adjust player balance for even/odd bets.
    if (bet_type == 1) and (bet_val == 1):  # Even
        if (int(result) % 2 == 0) and (int(result) != 0):
            payout = bet
            balance += bet + payout
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if (bet_type == 1) and (bet_val == 2):  # Odd
        if int(result) % 2 == 1:
            payout = bet
            balance += bet + payout
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust player balance for red/black bets.
    if (bet_type == 2) and (bet_val == 1):  # Red
        if slots[result] == 'red':
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if (bet_type == 2) and (bet_val == 2):  # Black
        if slots[result] == 'black':
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust player balance for the set of twelves.k
    if bet_type == 3:  # First Twelve
        if (int(result) >= 1) and (int(result) <= 12):
            balance += 3 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 4:  # Second Twelve
        if (int(result) >= 13) and (int(result) <= 24):
            balance += 3 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 5:  # Third Twelve
        if (int(result) >= 25) and (int(result) <= 36):
            balance += 3 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust the player balance for the first and second set of eighteen.
    if bet_type == 6:  # First Eighteen
        if (int(result) >= 1) and (int(result) <= 18):
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 7:  # Second Eighteen
        if (int(result) >= 19) and (int(result) <= 36):
            balance += 2 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust for betting multiple numbers at the same time.
    if bet_type == 8:  # Combination of two numbers
        if int(result) in bet_val:
            balance += 18 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 9:  # Combination of three numbers
        if int(result) in bet_val:
            balance += 12 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 10:  # Combination of four numbers
        if int(result) in bet_val:
            balance += 9 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 11:  # Combination of six numbers
        if int(result) in bet_val:
            balance += 6 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    if bet_type == 12:  # Combination of 00-0-1-2-3
        if result in bet_val:
            balance += 7 * bet
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
    # Adjust player balance if bet a single number.
    if bet_type == 13:
        if result == bet_val:
            payout = 36 * bet
            balance += payout
            prompt = "Winner! You now have $%s dollars!" % balance
        else:
            prompt = "Loser! You now have $%s dollars!" % balance
            
    bankroll = balance

    return (prompt, bankroll)
global slots
keep_playing = 'yes'
while (keep_playing.lower() == 'yes') or (keep_playing.lower() == 'y'):
    try:
        bet = int(input("How much do you want to bet?: "))
        if bet < 10:
            print("Sorry, the minimum bet is $10. Please enter a valid amount.")
            continue
        total_bet += bet  # Track total bet

        bet_type = int(input("What type of bet? Choose one of the given numbers:\n"
                             "1 = Even/Odd\n"
                             "2 = Red/Black\n"
                             "3 = First Twelve (1-12)\n"
                             "4 = Second Twelve (13-24)\n"
                             "5 = Third Twelve (25-36)\n"
                             "6 = First Eighteen (1-18)\n"
                             "7 = Second Eighteen (19-36)\n"
                             "8 = Combination of Two Numbers\n"
                             "9 = Combination of Three Numbers\n"
                             "10 = Combination of Four Numbers\n"
                             "11 = Combination of Six Numbers\n"
                             "12 = Combination of 1-2-3-0-00\n"
                             "13 = One Number (Straight Up)\n"
                             "Choose number: "))
        if bet_type not in range(1, 14):
            print("Invalid bet type. Please choose a number between 1 and 13.")
            continue

        (result, color, slots) = spins()
        (prompt, balance) = adjusted_bankroll((result, color, slots), bankroll, bet_value(bet_type))

        print("\nThe winning number is: %s %s !" % (result, color))
        if bankroll < 10 or balance < 10:
            print(prompt)
            print("Sorry, the minimum bet is $10. Please deposit for more fun >_<. Game over!")
            break
        else:
            print(prompt)
            total_win += (balance - bankroll)  # Track total win
            bankroll = balance
            print("\nTotal Wins: $%s" % total_win)
            print("Total Bets: $%s" % total_bet)

        total_win += (balance - bankroll)  # Track total win
        bankroll = balance
        keep_playing = input("Would you like to keep playing? (Y/N): ")
        if keep_playing.lower() not in ['yes', 'y', 'no', 'n']:
            print("Invalid option. Please enter 'Y' or 'N'.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid whole number.")