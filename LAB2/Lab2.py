import json

# Read the data from the file into a single string.
with open('Lab02.json','r') as f:
   
# Convert the string into a JSON object.
   data_dict = json.load(f)

# Convert the username and password components of the JSON object into two lists.
usernames = data_dict['username']
passwords = data_dict['password']

# Print the resulting lists
print(usernames)
print()
print(passwords)

# Get the valuse from user.
user_name = input('Enter your name: ' + '\x1B[1;4m')
user_password = input('\x1B[0m' 'Enter your password: ' + '\x1B[1;4m')

#  Decide the user if at present the lists.
if user_name in usernames and passwords[usernames.index(user_name)] == user_password:
    print('\x1B[0m' "You are authenticated!")
else:
    print('\x1B[0m' "You are not authorized to use the system..")


