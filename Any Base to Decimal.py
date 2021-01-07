'''Objective : Converting anybase number to Decimal Number '''

def con(num_str,base,power): #function for converting any base to decimal
    num_str = num_str[::-1] #reversing the string 
    result = 0 #Initialize result
    for k in range(len(num_str)):
        dig = num_str[k] #storing single char of num_string
        if dig.isdigit():#assuming it is number only
            dig = int(dig)
        else:    #if it alphabet only
            dig = ord(dig.upper())-ord('A')+10 #ord(<character>) – Built-in function that returns the ASCII value of character
        result += dig*(base**power) #logic used :1*str[0] + base*str[1] + (base)^2*str[2] + ...
        power+=1
    print("Result",result)


def val(num_str,base): #function : for checking if entered number is valid or not according to base
    temp=num_str.upper() #changing alphabest to uppercase
    alist=['.','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#list of all allowerd characters 
    for i in temp: # if char found in list then contine if not then raise an error
        if i in alist[0:base+1] :
            continue
        else:
            print("\nPlease Enter a valid base number.\n"
                      "\n-Choose Again-\n")
        main()
    
    if num_str.count(".")>1: #couting period if it is more then one raising error if not continuing 
        print("\nPlease Enter a valid base number.\n"
                      "\n-Choose Again-\n")
        main()
    elif num_str.count(".")==1: #if period is one then we will spliting into two parts  
        temp=num_str.split(sep=".")
        power=-len(temp[1]) #storing number of character on right side of period in string
        num_str=num_str.replace('.', '') #removing period(.) from string 
        con(num_str,base,power)#calling function
    else: 
        power=0
        con(num_str,base,power)
    
    main() #restarting the program

def main():#menu
    print("\n---------------CONVERSION MENU---------------\n"
          "1. Binary to Decimal.\n"
          "2. Octal to Decimal.\n"
          "3. Hexadecimal to Decimal.\n"
          "4. Anyother base\n"
          "5. To Exit.\n")
    ch=int(input("Enter your Choice: "))#taking input in string if base is greater then 10 
    x=(input("Enter your number: "))
    if(ch==1):
        val(x,2)#calling conversion function with base 2
    elif(ch==2):
        val(x,8)#calling conversion function with base 8
    elif(ch==3):
        val(x,16)#calling conversion function with base 16
    elif(ch==4):
        r=int(input("Enter your radix: "))
        val(x,r)#calling conversion function with entered base 
    else:#for anyother number it will exit
        print("\nEnding the Program.")
        exit()
     
if __name__ == '__main__':
    main()
    
#The code is Contributed by Ankit
