user_input = {}

while True:
    try:
        numbers = int(input("Please input a number from 1-50, if not there will be consequences"))

        Invalid = numbers < 50 in user_input
    except:
        print