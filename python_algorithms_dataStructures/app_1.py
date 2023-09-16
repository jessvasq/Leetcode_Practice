'''PRACTICE'''
'''A user forgot the password of his linkedin account. But he knows the ASCII values of his password in reverse order. Help the user to find the password.
Given the string, decode the password'''

#Loop 
#Reverse the string  
#convert from ASCI values to strings or integers 
#return the answer in a string (.join method)
#does the password have alphabets only? or does it include blank spaces? or numbers? 

password1="101109971110"

def find_pw(str):
    #reverse the string '' by using the slicing notation used with strings 
    reverse_str = str[::-1] #first empty part indicates you want to start slicing at the beginning of the string, the second empty part indicates we want to end at the beginning of the string. The -1 means that we want to move through the string in reverse order, from the end towards the beginning
    print(reverse_str)
    
    #initial value
    i = 0
    #result = empty string
    result = ''
    
    while i < len(str)-1:
        ascii_value = str[i] + str[i+1]
        if ascii_value == '32':
            result = result + ''
        elif int(ascii_value) in range(65, 91) or int(ascii_value) in range(97, 100):
            result = result + chr(int(ascii_value))
        elif i+2<len(str):
            ascii_value = ascii_value + str[i+2]
            result = result + chr(int(ascii_value))
            i+=1
        i+=2
    return result

print(find_pw(password1))

'''There is a group of people which also includes two monsters in this group and they split these groups among the people to kill them. When monsters come into the group of people, then at that time people leave their group.
After that, the breaking of the group will continue due to the monster's entry. And at last, the group with the minimum length will be killed by the monsters. Two types of monsters are present there namely '@' and '$'. People are presented as a string 'P'. Now you have to find out the minimum length of the group which will be killed by monsters '''

#find the min

def find_min(str): 
    #splits the string using the @ character as the delimiter
    groups = str.split('$')
    #This line initializes a variable min_length to positive infinity (float('inf')). This initial value is used to ensure that the first minimum length found in the subsequent loop will be smaller than this initial value.
    min_length= float('inf')
    
    for group in groups: 
        #further splits each group using the @ character as the delimiter
        subgroups = group.split('@')
        #creates a list called lengths using a list comprehension. It calculates the length of each substring in the subgroups list and stores these lengths in the lengths list.
        lenghts = [len(subgroup) for subgroup in subgroups]
        #compare the min length found within the current group (min(lengths)) with the current minimum length stored in the min_length variable. 
        min_length = min(min_length, min(lenghts))
    
    return min_length

test1= 'PPPPPP@PPP@PP$PP'
#test 
print(find_min(test1))