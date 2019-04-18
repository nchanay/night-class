import random

earnings = 0
expenses = 0

# maybe make a dictionary here
winnings = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}


def payout(winning_ticket, current_ticket):
    return winnings[len([i for i, j in zip(winning_ticket, current_ticket) if i == j])]

    # if hits == 1:
    #     return 4
    # elif hits == 2:
    #     return 7
    # elif hits == 3:
    #     return 100
    # elif hits == 4:
    #     return 50000
    # elif hits == 5:
    #     return 1000000
    # elif hits == 6:
    #     return 25000000
    # else:
    #     return 0

def pick6():
    return [random.randint(1, 99) for digit in range(6)]


# for digit in range(6):
#     pick6.append(random.randint(1,99))


winning_ticket = pick6()
print(f"The winning numbers are {winning_ticket}")

for ticket in range(100000):
    current_ticket = pick6()
    expenses += 2
    earnings += payout(winning_ticket, current_ticket)
    # for digit in range(6):
    #     current_ticket.append(random.randint(1, 99))
    # hits = 0
    # # [i == j for i, j in zip(x_list, y_list)] from stackoverflow.com
    # for i, j in zip(pick6, current_ticket):
    #     if i == j:
    #         hits += 1

ROI = round((earnings - expenses) / expenses, 2)

print(f"100,000 were tickets was purchased, the cost was ${expenses}, and your earnings were ${earnings}.\nYour Return on Investment (ROI) per ticket was about ${ROI}.")
