def print_big(name):
    # This dictionary is used to contain the patterns required in order to form the letters in the alphabet that the program is instructed to print
    # For an expanded version of this python program, the dictionary below would have all the patterns needed to print the entire alphabet
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*  * ',9:'*    ',10:'* * *',11:' ****',12:'    *',13:'**  *',14:'*  **'}
    # For an expanded version of this python program, you would have the complete alphabet in the dictionary below so that it is able to print whatever word it is given.
    alphabet = {'M':[3,2,10,3,3],'A':[1,2,4,3,3],'D':[5,3,3,3,5],'I':[1,1,1,1,1],'S':[4,9,11,12,4],'O':[4,3,3,3,4],'N':[3,13,14,3,3]}
    for pattern in alphabet[name.upper()]:
        print(patterns[pattern])

print_big('m')
print_big('a')
print_big('d')
print_big('i')
print_big('s')
print_big('o')
print_big('n')

