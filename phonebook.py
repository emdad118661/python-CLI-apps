phonebook = {
    'contact1': {
        'name': 'John',
        'address': '29',
        'email': 'Programmer',
        'phone_no': '01961458608'
    },
    'contact2': {
        'name': 'Steve',
        'address': '45',
        'email': 'HR',
        'phone_no' : '01876423228'
    }
}
filename = 'phonebook.txt'

phonebook_string = str(phonebook)

print("................................welcome to your phonebook....................................................\n\n\n here you can do the following task....")

Instructions = "\n1: enter 1 to add new contacts.\n2: enter 2 to update the existing contacts.\n3: enter 3 to delete the existing contacts.\n4: enter 4 to show all contacts.\n5: enter 5 to search contact\n6: enter 6 to store data in a txt file\n7:enter 7 to quit this app"

print(Instructions)

input_user = input("\n\nEnter your input...")

def add():
    size = int(input("enter how many contacts you want to add: "))

    for i in range(size):
        dict_name = input("Enter the name of contact: ")

        phonebook[dict_name] = {}
        name = input("Enter name: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone_no = input("Enter phone number: ")
        phonebook[dict_name]['name'] = name
        phonebook[dict_name]['address'] = address
        phonebook[dict_name]['email'] = email
        phonebook[dict_name]['phone_no'] = phone_no

def update():
    size = int(input("enter how many contacts you want to update: "))

    for i in range(size):
        dict_name = input("Enter the name of contact: ")

        phonebook[dict_name] = {}
        name = input("Enter name: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone_no = input("Enter phone number: ")
        phonebook[dict_name]['name'] = name
        phonebook[dict_name]['address'] = address
        phonebook[dict_name]['email'] = email
        phonebook[dict_name]['phone_no'] = phone_no


    

for x in range(100):
    #........................................ add new list ............................................................
    if (input_user == '1'):
        add()

        print(phonebook)
        print(Instructions)
        input_user = input("\n\nEnter your input...")
    

#........................................ update list ..................................................................
    elif (input_user == '2'):
        update()

        print(phonebook)
        print(Instructions)
        input_user = input("\n\nEnter your input...")
    

#.......................................... delete list ..................................................................
    elif (input_user == '3'):
        size = int(input("enter how many contacts you want to delete: "))
    
        for i in range(size):
            dict_name = input("Enter the name of contact: ")
            del phonebook[dict_name]

            print(phonebook)
            print(Instructions)
            input_user = input("\n\nEnter your input...")

#......................................... display list ...................................................................
    elif (input_user == '4'):
        print(phonebook)
        print(Instructions)
        input_user = input("\n\nEnter your input...")

    elif (input_user == '5'):
        dict_name = input("Enter the contact you want to search: ")
        try:
            phonebook[dict_name]
            search = phonebook[dict_name]
    
            print(search)
        except KeyError:
            print("not found")
        except:
            print("not found")

        print(Instructions)
        input_user = input("\n\nEnter your input...")

    elif(input_user == '6'):
        input_store = input("Are you sure you want to store all the data in data file?? Press 1 for yes, press 2 for no")
        if(input_store == '1'):
            with open(filename, 'w') as f:
                f.write(phonebook_string)
                print("contacts stored successfully!!")
        elif(input_store == '2'):
            print("ok,, thank you!!")
        else:
            print("wrong input!! try again....")

        print(Instructions)
        input_user = input("\n\nEnter your input...")
    
    elif (input_user == '7'):
        print("the app is shutting down, thank you!!")
        break
#.......................................... else ..........................................................................
    else:
        print("sorry!! try again.......")
        print(Instructions)
        input_user = input("\n\nEnter your input...")

