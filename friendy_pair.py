# numers to check
num1 = int(input("Please enter a first number: "))
num2 = int(input("Please enter a second number: "))

def isFriendlyPair(num1,num2):
    """This function checks whether two numbers are friendly pairs or not. It returns a boolean value. The numbers must be distinct."""

    ab1 = 0
    ab2 = 0

    if num1 == num2:
        return "Invalid"
    elif type(num1) != int or type(num2) != int:
        return "Invalid"
    else:
        ab1 = chegga(num1,0)
        ab2 = chegga(num2,0)


    # If num1 and num2 are friendly pairs return True. 
    if ab1 == ab2:
        return True
    else:
        return False


def chegga(num,total):
    for i in range(1,num+1):
        if num % i == 0:
            total += i
            i += 1
        else:
            i += 1
    resultat = total / num
 
    return resultat


#This line prints your method's return so that you can check your output.
print(isFriendlyPair(num1,num2))
