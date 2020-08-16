#For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here
flower_dict = {}
def create_flower_dict():
    
    with open ('flowers.txt', 'r') as file:
        for lines in file:
            flower_key = lines.split(':')[0]
            flower_value = lines.split(':')[1].strip('\n')
            flower_dict[flower_key] = flower_value
    
# HINT: create a dictionary from flowers.txt


# HINT: create a function
def match_flower_name(input_dict):
    
    username = input('Enter your First [space] Last name only: ')
    first_letter = username.title().split()[0][0]#
    for key , value in input_dict.items():
        if first_letter == key:
            print('Unique flower name with the first letter:' + input_dict[key])

    
    
create_flower_dict()  
match_flower_name(flower_dict)   
    
    
    

#