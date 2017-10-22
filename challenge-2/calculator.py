#!/usr/bin/env python3
def f(salary): 
    a = salary * 0.165             #Social_insurance 
    b = salary - a - 3500          #Taxable_income 
    c = salary - 3500              #Tax_threshold 
    if 0 >= c:
        return salary - a          #result:After_tax_salary
    elif 0 < c <= 1500:
        return salary - a - b * 0.03 - 0    
    elif 1500 < c <= 4500:
        return salary - a - (b * 0.1 - 105)
    elif 4500 < c <= 9000:
        return salary - a - (b * 0.2 - 555)
    elif 9000 < c <= 35000:
        return salary - a - (b * 0.25 - 1005)
    elif 35000 < c <= 55000:
        return salary - a - (b * 0.3 - 2755)
    elif 55000 < c <= 80000:
        return salary - a - (b * 0.35 - 5505)
    else:
        return salary - a - (b * 0.45 - 13505)

if __name__ == '__main__': 

    import sys
    try:
        list = sys.argv[1:]     
        for str in list:
            a = str 
            b = a.split(':')
            [x,y] = b
            salary = int(y)
            print(x+':'+format(f(salary),'.2f'))
    except:
        print("Parameter Error")
