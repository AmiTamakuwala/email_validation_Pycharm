"""
# making code for e-mail id validation in python.
# for that we will make code using "if" and "else" conditions:-
"""

"""
# here, I am using many conditions...which are as follow....

condition-1 : e-mail id length should have more then 6 letters (# ">=6") 
                # will use "len()" function.
condition-2 : id must have alphabets on the place.(where we will use ".isalpha()" function).
condition-3 : in id we must have "@" sign which have two condition which both should be fulfilled. (# "and" operator.)
                # also using "and" -- another condition: there must be only 1 "@" sign in the id.
condition-4 : for ".com" or ".in" we need to specify the "." sign place...
                # must be from the last 4th or from the last 3rd place.  (# will use "^" operator)
"""

'''
# after this conditions we also have other conditions like..
 in e-mail id we must not have upper case also there must not be any space in between the mail id.
 
# but for that we  will use "for" loop. 
# so, for loop can check every condition letter by letter.

condition-5 : there should be not even single space in Id also there should be no "uppercase" .
            there should be no "#", ":" , "_" , etc. signs
                (".isspace()" function, ".upper()" function)
condition-6 : digit condition. there should be digit in id.      
            (".isdigit()" function)
condition-7 : there should be "#", ":", ">", "<", etc. signs in id.
'''
email = input("Enter your e-mail Id: ")      # g@g.in , # iscube@gmail.com
k, j, d = 0, 0, 0

'''
    # k is for 1st 4 conditions.
    # j is for after 4th conditions which is applied after "for" loop, so it will check 1 by 1 character.
    # d is for if we have others signs in id like >, < etc. sign. so if d=1 then condition should be wrong.
'''

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():         # condition-5, # ("isspace()": for having space in id)
                        k=1                      # (means if space will be there it can count)
                    elif i.isalpha():            # 1st letter is alphabet or not
                        if i == i.upper():       # condition-5     # so, first letter is upper or not
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:                       # condition-5
                        d=1

                if k==1 or j==1 or d==1:
                    ''' # (if there is any 1 space condition should be wrong)'''
                    print("wrong Id: condition-5")
                else:
                    print("Right e-mail Id.")
            else:
                print("wrong Id: condition-4")

        else:
            print("wrong Id: condition-3")

    else:
        print("wrong Id: condition-2")
else:
    print("wrong Id: condition-1.")


