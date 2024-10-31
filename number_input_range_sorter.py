user_input = []

while True:
    try:
        numbers = int(input("Please input a number from 1-50, if not there will be consequences: "))

        if numbers > 51:
            break
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

for numbers in user_input:
    if user_input <= 10:
        row_10.append(numbers)
    elif user_input <= 20:
        row_20.append(numbers)
    elif user_input <= 30:
        row_30.append(numbers)
    elif user_input <= 40:
        row_40.append(numbers)
    elif user_input <= 50:
        row_50.append(numbers)

print(row_10, row_20, row_30, row_40, row_50)