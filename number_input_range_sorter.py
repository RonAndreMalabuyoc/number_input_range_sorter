user_input = []

while True:
    try:
        numbers = int(input("Please input a number from 1-50, if not there will be consequences: "))

        if 1 <= numbers <= 50:
            user_input.append(numbers)
        else:
            print("Out of range there buddy")
    except:
        print("Whoops, wrong")

    try:
        repeat = input("Will you input another number in? (yes/no): ")
        if repeat == "no":
            break
    except:
        print("welp")

row_10 = []
row_20 = []
row_30 = []
row_40 = []
row_50 = []

for number in user_input:
    if number <= 10:
        row_10.append(numbers)
    elif number <= 20:
        row_20.append(numbers)
    elif number <= 30:
        row_30.append(numbers)
    elif number <= 40:
        row_40.append(numbers)
    elif number <= 50:
        row_50.append(numbers)

print("Row 1-10:", len(row_10))
print("Row 11-20:", len(row_20))
print("Row 21-30:", len(row_30))
print("Row 31-40:", len(row_40))
print("Row 41-50:", len(row_50))