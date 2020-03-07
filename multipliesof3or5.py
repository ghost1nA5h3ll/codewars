#find all numbers which are lower than parameter and multipliers of 3 or 5
#sum them all up
def solution(number):
    summe = 0
    for j in range(number):
        
        if j % 3 == 0 or j % 5 == 0:
            summe += j
    return summe
