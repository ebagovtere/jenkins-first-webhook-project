print("hello world")
print("hello ebubekir")

try:
    x = int(input("Please enter a number between 1 and 3999 : "))
except ValueError :
    print("Something went wrong")
    print("Please enter a decimal number !!!")  
    x = int(input("Please enter a number between 1 and 3999 : "))
def int_to_rome(x):
    if 1 <= x <= 3999 :
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
        i = 12  
        roman_numeral = ''
        while x != 0:
            if numbers[i] <= x:    
                roman_numeral += roman[i] 
                x = x - numbers[i]
            else:
                i -= 1 # i = i - 1
    else :
        print("You can only enter a number between 1 and 3999 ")
    return roman_numeral    
print(int_to_rome(x))
print("Thanks for using our mini calculator! Come again!")