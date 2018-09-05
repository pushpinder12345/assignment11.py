import re as r

# Question 1: validate email
# Answer 1:

email = input("enter the email to be verified: ")
matcher = r.finditer('^[a-z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)', email)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('email verified')
else:
    print('wrong input')


# question 2: validate indian phone number
# answer 2:

number = str(input('enter the phone number'))
matcher = r.finditer('^[+][9][1][6-9][\d]{9}', number)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('phone number validated')
else:
    print('wrong phone number')
