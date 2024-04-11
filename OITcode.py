#OIT Code Challenge 4/10/2024
#Create a program that converts Roman Numerials into a decimal value
#Time spent - approximatley 45 minutes

#first I will define all the RNs with their values.
def value(x):
    if (x == 'I'):
        return 1
    if (x == 'V'):
        return 5
    if (x == 'X'):
        return 10
    if (x == 'L'):
        return 50
    if (x == 'C'):
        return 100
    if (x == 'D'):
        return 500
    if (x == 'M'):
        return 1000
    return -1

#I realized after finishing the romanCalculator function that I need to satisfy #4 in the challenge
def canSubtract(x, y):
    #I just made a list of pairs that meet the #4 requirements
    #I hope that they are all correct, I'm not confident that I interpreted the explanation correctly
    valid_pairs = [('I', 'V'), ('I', 'X'), ('X', 'L'), ('X', 'C'), ('C', 'D'), ('C', 'M')]
    return (x, y) in valid_pairs

#Now i'll make the main function
def romanCalculator(RN): #I assume the user/tests will not input any invalid inputs for the sake of simplicty
    #initializing iterator and rolling output value
    i = 0
    output = 0

    #I was initialy planning on using a for loop here, however, I think RN will be easier to maninupulate
    #using a while loop and an interator for the cases where we are reading two symbols to make one number
    while (i < len(RN)):

        #setting x to value of first number
        x = value(RN[i])

        #setting y to value of second number if it is not the end of the RN
        if (i + 1 < len(RN)):
            y = value(RN[i + 1])

            #check x and y to see which case we will use
            if (x >= y):
                #case where second number is smaller and only adding x
                output += x
                i += 1
            else:
                #2. Roman numerals also involve subtractive notation.
                #If symbol A is less than the symbol immediately following it (B), A is subtracted from B and AB is treated as a
                #unit to add to the total. Thus, IV = 4, XL = 40, XC = 90.

                if canSubtract(RN[i], RN[i + 1]): #check to satisfy subtract rule
                    output = output + y - x
                    i += 2

                else:
                    #I decided to just add x if the subtraction was invalid
                    #the prompt didn't explain the prefered way to handle this case
                    #so I know not to subract but I don't want to throw an error so add is my last option
                    output += x
                    i += 1

        #end of RN case, no second number to check
        else:
            output += x
            i += 1

    return output

print(romanCalculator("IC"))