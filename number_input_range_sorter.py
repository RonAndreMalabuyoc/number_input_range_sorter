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