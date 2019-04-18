# average numbers

def average(nums):
    print(f"computing the average for your numbers: {nums}")
    return (sum(int(i) for i in nums) / len(nums))

nums = []
while True:
    number = input("Enter a number, or 'done' : ").strip().lower()
    if number.isdigit():
        number = int(number)
        nums.append(number)
        continue
    elif number == "done":
        break
    else:
        print("Make sure you're typing a number, or 'done'")

print(f"The average is: {average(nums)}")
