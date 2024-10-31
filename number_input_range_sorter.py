user_input = {}

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

if numbers <= 50:
    row_50.append(numbers)
    count_50 = len(row_50)
elif numbers <= 40:
    row_40.append(numbers)
    count_40 = len(row_40)
elif numbers <= 30:
    row_30.append(numbers)
    count_30 = len(row_30)
elif numbers <= 20:
    row_20.append(numbers)
    count_20 = len(row_20)
elif numbers <= 10:
    row_10.append(numbers)
    count_10 = len(row_10)

print(row_50, row_40, row_30, row_20, row_10)