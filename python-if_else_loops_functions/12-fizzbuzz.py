#!/usr/bin/python3

# def fizzbuzz():

#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("{}".format("FizzBuzz"), end=" ")
#         elif i % 3 == 0:
#             print("{}".format("Fizz"), end=" ")
#         elif i % 5 == 0:
#             print("{}".format("Buzz"), end=" ")
#         else:
#             print("{}".format(i), end=" " if i != 100 else "")


def fizzbuzz():

    for i in range(1, 101):
        str = i
        if i % 3 == 0 and i % 5 == 0:
            str = "FizzBuzz"
        elif i % 3 == 0:
            str = "Fizz"
        elif i % 5 == 0:
            str = "Buzz"

        print(str, end=" " if i != 100 else "")

def fizzbuzz():
    d = {3: "Fizz", 5: "Buzz", 7: "Fuzz", 9: "Bizz", 15: "FizzBuzz"}

    for i in range(1, 101):
        str = i
        for k, v in d.items(): # [[3, "fizz"], [5, "buzz"], [15, "fizzbuzz"]]
            if i % k == 0:
                str = v
    
        print(str, end=" " if i != 100 else "")