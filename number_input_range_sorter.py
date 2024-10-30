#set an array to store the input values to be checked later
#setup a input system for the numbers being input
#Check the input numbers if it goes over the range
#Check how many of the numbers goes into a set in a range of 10s


#main variable
user_input = {}
#loop
while True:
    try:
#input numbers
        numbers = int(input("Please input a number from 1-50, if not there will be consequences"))
    #if it isn't an integer, or number goes over 50, print invalid
        Invalid = numbers < 50 in user_input
    except:
#end loop

#find the values inputted and sort them in ranges of 10s