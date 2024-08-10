from database import dbController

user = "sslinnn"
#
# usr = dbController.get_user_by_username(user)
#
# print(usr[1])

if 'sslinnn' == dbController.get_user_by_username(user)[1]:
    print('This user is on site')
else:
    print('Free to use')