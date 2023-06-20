katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f' {i + 1}. {katz_deli[i]}'
        print(message)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. ' +\
        f'You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]


# adding the katz_deli as an  empty array, 
# def line and if the line is empty to print "the line is currenrly empty", 
# def take_a_number passing katz_deli, new_customer, and append
# def now_serving and passing katz_deli through  
# 
# clear load error and the first failed test
# Module deli_counter.py says the line is empty . 

# katz_deli = []

# def line(katz_deli):
#     if not katz_deli:
#         print("The line is currently empty.")


# def take_a_number(katz_deli, new_customer):
#     katz_deli.append(new_customer)

# def now_serving(katz_deli):
#     pass

# *****************************************************************************************


# Adding the print and else  to take and now will clear 6 errors 

# Module deli_counter.py says the line is empty .                                                                                                                                                               
# Module deli_counter.py adds a person to an empty line .                                                                                                                                                             
# Module deli_counter.py adds a person to the end of the line .                                                                                                                                                   
# Module deli_counter.py correctly builds the line .                                                                                                                                                      
# Module deli_counter.py says that the line is empty .                                                                                                                                                            
# Module deli_counter.py serves the first person in line and removes them from the queue .   

# def take_a_number(katz_deli, new_customer):
#     katz_deli.append(new_customer)
#     print(f'Welcome, {new_customer}. ' +\
#         f'You are number {len(katz_deli)} in line.')   
   

# def now_serving(katz_deli):
#     if not katz_deli:
#         print("There is nobody waiting to be served!")
#     else:
#         print(f'Currently serving {katz_deli[0]}.')
#         del katz_deli[0]
                                                                                                           
# ***************************************************************************************************

# adding this else amd print to the def line will clear final error:
# Module deli_counter.py displays the current line .   

#    else:
#         message = "The line is currently:"
#         for i in range(len(katz_deli)):
#             message += f' {i + 1}. {katz_deli[i]}'
#         print(message)

# **********************************************************

# Notes for me: 

# This code is simulating a deli where people line up to be served. It has three functions:

# The line function checks if there are any customers in the katz_deli list. 
# If the list is empty, it prints "The line is currently empty." 
# Otherwise, it creates a message to display the current line by iterating over each customer in the katz_deli list and 
# adding their position and name to the message. Finally, it prints the message.

# The take_a_number function adds a new customer to the katz_deli list. 
# It takes two parameters: katz_deli (the list of customers) and new_customer (the name of the new customer). 
# It appends the new_customer to the katz_deli list and prints a welcome message along with the customer's position in line 
# (which is the length of the katz_deli list).

# The now_serving function checks if there are any customers in the katz_deli list. 
# If the list is empty, it prints "There is nobody waiting to be served!" 
# Otherwise, it prints the name of the customer at the beginning of the katz_deli list (the customer being served) 
# and removes that customer from the list.

# In simple terms, this code allows you to see who is in line, add new customers to the line, and serve customers one by one.