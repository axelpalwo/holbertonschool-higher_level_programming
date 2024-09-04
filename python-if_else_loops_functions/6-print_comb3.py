#!/usr/bin/python3
for i in range(100):
    for v in range(1):
        if (i % 10 == i / 10 or i % 10 > i / 10) and i != 0:
            if i < 80:
                print("{:02}".format(i), end=", ")
            else:
                print("{:02}".format(i))
