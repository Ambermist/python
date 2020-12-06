def readint(prompt, min, max):
    try:
        prompt=int(input("Enter a number from -10 to 10: "))
        if prompt<-10 or prompt>10:
            raise ArithmeticError
    except ArithmeticError:
        print ('Error: the value is not within permitted range (-10..10)')
        prompt=readint(prompt, min, max)
    except ValueError:
        print ('Error: wrong input')
        prompt=readint(prompt, min, max)
    return prompt
        
            


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
