# practice 1 combine dictionary

def combine(a, b):
    # combined = {}
    # for i in range(len(a)):
    #     combined[a[i]] = b[i]
    # return combined

    return dict(zip(a, b))

    # return {a[i]:b[i] for i in range(len(a))}

fruit_list = ['apples', 'banana', 'orange']
price_list = [1.2, 3.3, 2.1]


combined = combine(fruit_list, price_list)
print(combined)

# practice 2 caclulate average price

def average(price):
    return round(sum(price.values()) / len(price), 1)

print(f"Average price of fruits {combined} = {average(combined)}")
