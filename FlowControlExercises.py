#1
def max_(x,y) :
    if x > y :
        print(x)
    else:
        print(y)
max_(5,4)


#2
def max_of_three (x, y,z):
    if x > y:
        if x > z :
            print(x)
    elif y > x and y > z:
            print(y)
    else:
        print(z)
max_of_three(1,2,3)

#3
def length (arrayName):
    x = 0
    for i in arrayName:
        x = x + 1
    print("The length of given list:  ", str(x))
    return x

member = ["raina", "christy", "joce", "bently", "jason"]
length(member)

#4
def characters (x):
    vowels = ("a", "i","u","e","o")
    for i in vowels:
        if i == x:
            return True
    return False
print(characters("r"))

#5
def reverse(string):
    #reversed_text:str = ""
    #for i in range (len(text)-1,-1,-1):
    #   reversed_text + = text [i]
    return string [::-1]
print(reverse("I am testing"))

#6
def is_palindrome(string):
    x = string [::-1]
    if string == x:
        return True
    return " "
print(is_palindrome("radar"))

#7
def palindrome(word):
    x = word.replace(" ","")
    if (x[::-1] == x[::1]) :
        return True
    return " "
print(palindrome ("step on no pets"))


#8
def generate_n_chars(a:int, n:str ):
    print(a*n)
generate_n_chars(5, "x")


#9
def score (x : float):
    if 1.0 >= x >= 0.9:
        print("A")
    elif 0.9 >= x >= 0.8:
        print("B")
    elif 0.8 >= x >= 0.7:
        print("C")
    elif 0.7 >= x >= 0.6:
        print("D")
    elif 0.0 <= x < 0.6:
        print("F")
    else:
        x < 0.0 and x > 1.0
        print("error")
score(0.8)
score(2.0)


#10
def count_pay():
    x = float(input("Enter Hours: "))
    y = float(input("Rate: "))

    if x <= 40:
        pay = x*y
        print("Pay: ", str(pay))
        return
    else:
        pay = 40*y + (x-40)*1.5*y
        print("Pay: ", str(pay))
        return
count_pay()

#11
def distance_from_zero(something):
    if isinstance(something, int):
        print(abs(something))
    elif isinstance(something, float):
        print(abs(something))
    else:
        print("Nope")
distance_from_zero(-5.6)
distance_from_zero("What?")
distance_from_zero(7)



#12
def pig_Latin():
    word = str(input("Enter word: "))
    if len(word) > 0:
        if word.isalpha() is True:
            piglatin = word[1:] + word[0] + "ay"
            print(word, "in PigLatin is: ", piglatin.lower())
        else:
            print(" ")

pig_Latin()
