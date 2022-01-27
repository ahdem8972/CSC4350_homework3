def question1():
    string = input("Enter a string: ")
    lower_string = string.lower()
    vcount = 0
    space = 0
    for char in lower_string:
        if char in "aeiou":
            vcount += 1
        if char in " ":
            space += 1
    length_string = ((len(lower_string) - space)/2)
    if vcount > (length_string):
        return True
    elif vcount < (length_string):
        return False
    else:
        return None


def question2(height, radius):
    volume = 3.14 * height * pow(radius, 2)
    print(volume)

def question3():
    exit =
    input_list = (input("Enter a value, type \"exit.\" when done"))
    input_list.append()
    
    print(input_list)


def question6(num1, num2):
    if num2 == 0:
        print("Error! Cannot divide by 0!")
        return
    else:
        print(num1/num2)

question6(5,2)



