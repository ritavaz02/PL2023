def main():
    
    exit = True

    counter = 0 # sum of the digits
    flag = 0 # tells the index on the words 'on' or 'off'
    stopCounting = 0 # if 0 its to count the digit, else don't count it

    while exit:

        try:
            user_input = input("Enter something: ")
            print("The string is: '" + user_input + "'")
            for c in user_input:
                if stopCounting==0 and c.isdigit()==True: # its a digit and its not after an 'off'
                    counter += int(c)
                    flag = 0 # stop counting the index on the words 'on' or 'off' 
                elif c == "=":
                    print("The sum so far is: " + str(counter)) # print the sum
                    flag = 0
                elif c.lower() == "o":
                    if flag == 0: # it's the first 'o' to appear
                        flag = 1
                    else: # there were two 'o' in a row, stop counting the index
                        flag = 0
                elif c.lower() == "f":
                    if flag == 1: # word = 'of', increment the index
                        flag = 2
                    elif flag == 2: # word = 'off', active the flag to stop counting the digits
                        flag = 0
                        stopCounting = 1
                elif c.lower() == "n":
                    if flag == 1: # word = 'on', active the flag to start counting the digits
                        stopCounting = 0
                    flag = 0
                else: # ignore
                    flag = 0
        except KeyboardInterrupt:
            # end the loop when the user types "Ctrl+D" or "Ctrl+C"
            print("\nThe final sum is: " + str(counter))
            exit = False
        except EOFError:
            print("\nThe final sum is: " + str(counter))
            exit = False

main()