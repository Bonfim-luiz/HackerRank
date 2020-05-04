# Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

entrada = input()

if entrada[8:] == "PM" and entrada[0:2] != '12':
    print(str(int(entrada[0:2])+12) + entrada[2:8])
elif entrada[8:] == "AM" and entrada[0:2] == '12':
    print('00'+ entrada[2:8])
else:
    print(entrada[:8])
