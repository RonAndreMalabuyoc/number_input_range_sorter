user_input = {}

while True:
    try:
        numbers = int(input("Please input a number from 1-50, if not there will be consequences: "))

        if numbers > 51:
            break
    except:
        print("Whoops, wrong")