#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i != j:
            if i < j:
                print("{i}{j}".format(i=i,j=j), end=", " if i < 8 else "\n")
