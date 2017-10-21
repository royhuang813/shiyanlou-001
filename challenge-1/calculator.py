#!/usr/bin/env python3
def f(x):
    b = x - 3500
    if b <= 0:
        print(format(0,'.2f'))
    elif 0 < b <= 1500:
        print(format(b * 0.03 - 0, '.2f'))
    elif 1500 < b <= 4500:
        print(format(b * 0.1 - 105, '.2f'))
    elif 4500 < b <= 9000:
        print(format(b * 0.2 - 555, '.2f'))
    elif 9000 < b <= 35000:
        print(format(b * 0.25 - 1005, '.2f'))
    elif 35000 < b <= 55000:
        print(format(b * 0.3 - 2755, '.2f'))
    elif 55000 < b <= 80000:
        print(format(b * 0.35 - 5505, '.2f'))
    else:
        print(format(b * 0.45 - 13505, '.2f'))
if __name__ == '__main__':
    import sys
try:
    salary = int(sys.argv[1])
    f(salary)
except ValueError:
    print('Parameter Error')
