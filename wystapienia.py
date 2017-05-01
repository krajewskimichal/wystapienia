# Program tworzy tablice 100 losowych cyrf i wypisuję ilość wystąpień każdej z nich

import random

a = []

n = 100
while n > 0:
    a.append(random.randint(0, 9))
    n -= 1

b = dict([(x, a.count(x)) for x in a])

print ("Program tworzy tablice stu losowych cyfr i wypisuje ilość wystąpień kazdej z nich\n")
print ("Tablica stu losowych cyfr:\n", a, "\n")
print ("Ilośc wystąpień każdej cyfry:\n", b, "\n")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
