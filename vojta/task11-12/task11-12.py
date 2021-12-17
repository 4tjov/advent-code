DAYS = 256

with open("input11-12.txt") as f:
    input = f.read().split(",")
    lanternfishes = [int(item) for item in input]
    days = [0] * 9
    for lant in lanternfishes:
        days[lant] += 1

    for i in range(DAYS):
        b_lant = days[0]
        days = days[1:] + days[:1]
        days[6] += b_lant

    print(sum(days))
