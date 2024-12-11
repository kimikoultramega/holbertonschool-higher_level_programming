#!/usr/bin/python3

# def a():
#     for i in range(ord('z'), ord('a') -1, -1):
#         char = chr(i)
#         if i % 2 == 0:
#             print(f"{char.lower()}", end="")
            
#         elif i % 2 == 1:
#             print(f"{char.upper()}", end="")
            
def b():
    for i in range(ord('z'), ord('a') -1, -1):
        char = chr(i)
        print(f"{char.lower() if i % 2 == 0 else char.upper()}", end="")

b()