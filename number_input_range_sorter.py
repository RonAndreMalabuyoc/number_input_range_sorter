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
        user_input.append(row_10)
    elif user_input <= 20:
        user_input.append(row_20)
    elif user_input <= 30:
        user_input.append(row_30)
    elif user_input <= 40:
        user_input.append(row_40)
    elif user_input <= 50:
        user_input.append(row_50)

print(row_10, row_20, row_30, row_40, row_50)