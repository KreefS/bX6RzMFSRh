import sys
print("""

 ,-----.        ,--.              ,--.          ,--.                                                                           
'  .--./ ,--,--.|  | ,---.,--.,--.|  | ,--,--.,-'  '-. ,---. ,--.--.                                                           
|  |    ' ,-.  ||  || .--'|  ||  ||  |' ,-.  |'-.  .-'| .-. ||  .--'                                                           
'  '--'\\ '-'  ||  |\ `--.'  ''  '|  |\ '-'  |  |  |  ' '-' '|  |                                                              
 `-----' `--`--'`--' `---' `----' `--' `--`--'  `--'   `---' `--'                                                              
  ,--. ,--.                                                                                                                    
,-|  |-|  |-.,------.            ,--.  ,--.                    ,--.       ,--.  ,--.         ,--.   ,----.                     
'-|  |-|  |-'|  .--. ',--. ,--.,-'  '-.|  ,---.  ,---. ,--,--, |  | ,---. |  ,'.|  | ,---. ,-'  '-.'  .-./    ,--,--.,--. ,--. 
,-|  |-|  |-.|  '--' | \  '  / '-.  .-'|  .-.  || .-. ||      \|  |(  .-' |  |' '  || .-. |'-.  .-'|  | .---.' ,-.  | \  '  /  
'-|  |-|  |-'|  | --'   \   '    |  |  |  | |  |' '-' '|  ||  ||  |.-'  `)|  | `   |' '-' '  |  |  '  '--'  |\ '-'  |  \   '   
  `--' `--'  `--'     .-'  /     `--'  `--' `--' `---' `--''--'`--'`----' `--'  `--' `---'   `--'   `------'  `--`--'.-'  /    
                      `---'                                                                                          `---'     """)
print("Input a number")
print("\n1.+ between 2 numbers(you have to know this...)")
print("\n2.- between 2 numbers(you know this...)")
print("\n3.* between 2 numbers(multiply)")
print("\n4./ between 2 numbers(divide)")
print("\n5.** between 2 numbers(something to the power of something)")

answer = int(input())

if answer < 1:
    sys.exit()
if answer > 5:
    sys.exit()
    
if answer == 1:
    print("You chose +.")
    num1=float(input("Input the first number.\n"))
    num2=float(input("Input the second number.\n"))
    result1= num1 + num2
    print("The result is:", result1)
    end1 = input("\nPress enter to exit.")

if answer == 2:
    print("You chose -.")
    num3=float(input("Input the first number.\n"))
    num4=float(input("Input the second number.\n"))
    result2= num3 - num4
    print("The result is:", result2)
    end2 = input("\nPress enter to exit.")

if answer == 3:
    print("You chose multiply.")
    num5=float(input("Input the first number.\n"))
    num6=float(input("Input the second number.\n"))
    result3=num5 * num6
    print("The result is:", result3)
    end3 = input("\nPress enter to exit.")

if answer == 4:
    print("You chose divide.")
    num7=float(input("Input the first number.\n"))
    num8=float(input("Input the second number.\n"))
    result4=num7 / num8
    print("The result is:", result4)
    end4 = input("\nPress enter to exit.")

if answer == 5:
    print("You chose **.")
    num9 =float(input("Input the number\n"))
    num10 =float(input("Input the exponent.\n"))
    result5=num9 ** num10
    print("The result is:", result5)
    end5 = input("\nPress enter to exit.")

    

        
        
        
    


