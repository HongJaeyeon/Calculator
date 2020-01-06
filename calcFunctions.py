from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        result = 1
        for i in range(1,n+1):
            result = result * i
        return result
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):

    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''

    for value,letter in romans:
        while n >= value:
            result += letter
            n -= value

    return result

def retRom(ch):

    romans = [
        (1000, 'M'),  (500, 'D'),
         (100, 'C'),   (50, 'L'),
          (10, 'X'),    (5, 'V'),
           (1, 'I')
    ]

    for value in romans:
        if value[1]  == ch:
            num = value[0]
    return num


def romanToDec(numStr):
    try:
        result = 0
        for i in range(0,len(numStr)-1):
            if retRom(numStr[i])>=retRom(numStr[i+1]):
                result+=retRom(numStr[i])
            else:
                result-=retRom(numStr[i])
        return result + retRom(numStr[len(numStr)-1])

    except:
        return 'Error!'
