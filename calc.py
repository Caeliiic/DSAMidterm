import math
import time

print('C A L C U L A T O R')
print('')

while True:
    print('')
    time.sleep(1)
    print("OPTIONS:")
    print('')
    print("Addition [ + ]")
    print("Division [ / ]")
    print("Subtraction [ - ]")
    print("Multiplication [ * ] \nRemainder [ r ] \nSquare Root [ sqr ]")
    
    print('')
    time.sleep(0.5)
    chooseopt =input("Choose Option [ ? ]: ")
    
    def plus():
        no1 = int(input("First number: "))
        no2 = int(input("Second number: "))
        print("calculating...")
        time.sleep(2)
        print("Answer:", no1 + no2)
        
    def divide():
        no1 = int(input("First number: "))
        no2 = int(input("Second number: "))
        print("calculating...")
        time.sleep(2)
        print("Answer:", no1 / no2)
        
    def subtract():
       no1 = int(input("First number: "))
       no2 = int(input("Second number: "))
       print("calculating...")
       time.sleep(2)
       print("Answer:", no1 - no2)
    
    def multiply():
        no1 = int(input("First number: "))
        no2 = int(input("Second number: "))
        print("calculating...")
        time.sleep(2)
        print("Answer:", no1 * no2)
    
    def remainder():
        no1 = int(input("First number: "))
        no2 = int(input("Second number: "))
        print("calculating...")
        time.sleep(2)
        print(f"Answer: {no1} / {no2} there remainder is", no1 % no2)
        
    def square_root():
        no1 = int(input("First number: "))
        print("calculating...")
        time.sleep(2)
        print(f"The square root of {no1} is", no1 ** 0.5)
    
    if chooseopt == "+":
        plus()
            
    elif chooseopt == "/":
        divide()
    
    elif chooseopt == "-":
        subtract()
    
    elif chooseopt == "*":
        multiply()
    
    elif chooseopt == "r":
        remainder()
        
    elif chooseopt == "sqr":
        square_root()
    
    else:
        print("invalid input")
       
    print('')
    input1 = input("try again? (Yes/No): ").capitalize()
    if input1 == "No":
          break
    elif input1 == "Yes":
          print("")
    else:
           print("""Please enter "Yes"or "No" """)
           input1 = input("try again? (Yes/No): ").capitalize()
           if input1 == "No":
               break
           elif input1 == "Yes":
               print("")
           else:
                 print("Warning, program will finished afterwards.")
                 input1 = input("try again? (Yes/No): ").capitalize()
                 if input1 == "No":
                      break
                 elif input1 == "Yes":
                      print("")
                 else:
                        break
                        
    time.sleep(1)