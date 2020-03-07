#function should return a string object in format of a telephonenumber: "(123) 456-7890" 
def create_phone_number(n):
    result_string = "("
    count = 0
    for i in n:
        if(count == 3):
            result_string += ") "
        if(count == 6):
            result_string += "-"
        result_string += str(i)
        count += 1
    return result_string

testdata = [0,1,2,3,4,5,6,7,8,9]
print(create_phone_number(testdata))