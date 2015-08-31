#Login Loop Template

password = "secret"
user_response = ""
message = ""

user_response = raw_input("Password:")

if (user_response == password):
    message = """
########## Access Granted ############
"""
else:
    message = """
########## Password Incorrect ##########
########## Access Denied ###############
"""
print(message)




###Complete Program
##
##password = "secret"
##user_response = ""
##message = ""
##
##while (user_response != password and user_response != "exit"):
##    user_response = raw_input("Password:")
##
##    if (user_response == password):
##        message = """
##    ########## Access Granted ############
##    """
##    elif (user_response == "exit"):
##        message = "Goodbye..."
##    else:
##        message = """
##    ########## Password Incorrect ##########
##    ########## Access Denied ###############
##
##    Please try again or type "exit"
##    """
##    print(message)
##

    
