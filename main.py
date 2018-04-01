from spy_details import spy
from datetime import datetime

print f
from steganography.steganography import Steganography
print 'Hello Buddy!'
print 'Let\'s get Started'

STATUS_MESSAGE = ['Galti badi galti engineering','Attachemnts are good for email only','Sleeping']
friends = [{'name':'sushant','age':23,'rating':3.6,'is_online':True,'chats':[]},{'name':'Himanshu','age':23,'rating':3.6,'is_online':True,'chats':[]}]

def add_status(c_status):
    if c_status != None:
        print "Your current status is " + c_status
    else:
        print "you dont have any status currently"
    existing_status = raw_input("You want to select from old status? Y/N ")
    if existing_status.upper()=="N":
        new_status= raw_input("Enter your status: ")
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)
    elif existing_status.upper()=="Y":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice = input("enter your choice: ")
        new_status = STATUS_MESSAGE[user_choice-1]
    updated_status = new_status
    return updated_status

def add_friend():
    frnd ={
        'name':'',
        'age':0,
        'rating':0.0,
        'is_online':True,
        'chats':[]
    }
    frnd['name'] = raw_input("What is your name? ")
    frnd['age'] = input("What is your age? ")
    frnd['rating'] = input("What is your rating? ")
    if len(frnd['name'])>2 and 12<frnd['age']<50 and frnd['rating']>spy['rating']:
        friends.append(frnd)
    else:
        print "Friend cannot be added"
    return len(friends)

def select_frnd():
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " +frnd['name']
        serial_no = serial_no+1
    user_selected_frnd = input("Enter your choice: ")
    user_selected_frnd_index = user_selected_frnd -1
    return user_selected_frnd_index

def send_message():
    selected_frnd = select_frnd()
    original_image = raw_input("What is the name of orginal image? ")
    secret_text = raw_input("What is your secret text? ")
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,secret_text)
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[selected_frnd]['chats'].append(new_chat)
    print "Your secret message is ready!"

def read_message():
    selected_frnd = select_frnd()
    output_path = raw_input("Which image you want to decode? ")
    secret_text = Steganography.decode(output_path)
    print "Secret text is " + secret_text
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[selected_frnd]['chats'].append(new_chat)
    print "Your secret message has been saved!"


def start_chat(spy_name,spy_age,spy_rating):
    print "Here are you options "+ spy_name
    current_status = None
    show_menu = True
    while show_menu:
        choice = input("What do you want to do? \n 1. Add a status \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 0. Exit")
        if choice == 1:
            current_status = add_status(current_status)
            print "Updated status is " + current_status
        elif choice == 2:
            no_of_frnds = add_friend()
            print "You have " + str(no_of_frnds) + " friends"
        elif choice==3:
            send_message()
        elif choice==4:
            read_message()
        elif choice == 0:
            show_menu = False
        else:
            print "Invalid Input"



spy_exist = raw_input("Are you a new user? Y/N ")

if spy_exist.upper()=="N":
    print "Welcome back " +spy['name'] + " age : "+str(spy['age']) +" having rating of " +str(spy['rating'])
    start_chat(spy['name'],spy['age'],spy['rating'])

elif spy_exist.upper()=="Y":
    spy ={
        'name':'',
        'age':0,
        'rating':0.0
    }
    spy['name'] = raw_input('What is your spy name? ')
    if len(spy['name'])>2:
        print 'Welcome ' + spy['name'] + '. Glad to have you back with us.'
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        if spy_salutation=="Mr." or spy_salutation=="Ms.":
            spy['name'] = spy_salutation + " " + spy['name']
            print "Alright " + spy['name'] + ". I would like to know a little  \
                                          bit more about you. How are you?"
            spy_age = input("What is your age? ")
            if 50>spy_age>12:
                print "Your age is correct"
                spy_rating = input("What is your rating? ")
                if spy_rating>5.0:
                    print "Great Spy"
                elif 3.5<spy_rating<=5.0:
                    print "Average spy"
                elif 2.5<spy_rating<=3.5:
                    print "Bad spy"
                else:
                    print "Who hired you?"
                spy_is_online = True
                print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
                start_chat(spy_name,spy_age,spy_rating)
            else:
                print "You are not eligible to be a spy"
        else:
            print "Invalid salutation"
    else:
        print "OOopss Please enter a valid name"
else:
    print "Invalid entry"