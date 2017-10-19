#!/usr/bin/env python3
import sys
try:
    a = int(sys.argv[1])
except ValueError:
    print("Parameter Error")
b = a - 3500
if b <= 0:
    print(format(0 , ".2f"))
if 0 < b <= 1500:
    print(format(b * 0.03 - 0 , ".2f"))
if 1500 < b <= 4500:
    print(format(b * 0.1 - 105 , ".2f"))
if 4500 < b <= 9000:
    print(format(b * 0.2 - 555 , ".2f"))
if 9000 < b <= 35000:
    print(format(b * 0.25 - 1005 , ".2f"))
if 3500 < b <= 55000:
    print(format(b * 0.3 - 2755 , ".2f"))
if 55000 < b <= 80000:
    print(format(b * 0.35 - 5505 , ".2f"))
if b > 80000:
    print(format(b * 0.45 - 13505 , ".2f"))

