# Create a string variable
string = "supercalifragilisticexpialidocious"

# Using a for loop, count number of char repetitions and store in a dictionary
char_dict = {}

for char in string:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

print(char_dict)
