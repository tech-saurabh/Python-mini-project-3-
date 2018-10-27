email=input("enter the email address: ").strip() #using strip to cut off any extra spaces in input

user_name = email[:email.index("@")] #take out the user name upto @

domain_name = email[email.index("@") + 1:] 

output = "your user name is {} and your domain name is {}".format(user_name,domain_name)
print(output) #string formating is used here
