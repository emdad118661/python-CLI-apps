todo_list = {
    'list1': {
        'description': 'rifat weeding party',
        'date': '29 june',
        'place': 'dhanmondi'
    },
    'list2': {
        'description': 'conferance',
        'date': '25 june',
        'place': 'mirpur-2'
    }
}

filename = 'to_do data.txt'

to_do_string = str(todo_list)

#......................... add functionality ..........................................
def add():
    size = int(input("enter how many list you want to add: "))

    for i in range(size):
        dict_name = input("Enter the name of list: ")

        todo_list[dict_name] = {}
        description = input("Enter description: ")
        date = input("Enter date: ")
        place = input("Enter place: ")
        todo_list[dict_name]['description'] = description
        todo_list[dict_name]['date'] = date
        todo_list[dict_name]['place'] = place

#........................... update functionality ..........................................
def update():
    size = int(input("enter how many list you want to update: "))

    for i in range(size):
        dict_name = input("Enter the name of list: ")

        todo_list[dict_name] = {}
        description = input("Enter description: ")
        date = input("Enter date: ")
        place = input("Enter place: ")
        todo_list[dict_name]['description'] = description
        todo_list[dict_name]['date'] = date
        todo_list[dict_name]['place'] = place
    

print("................................welcome to your to do list....................................................\n\n\n here you can do the following task....")

Instructions = "\n1: enter 1 to add a new to-do list.\n2: enter 2 to update the existing lists.\n3: enter 3 to delete the existing lists.\n4: enter 4 to show the upcomming lists.\n5: enter 5 to store all the lists in a txt file\n6: enter 6 to quit this app"

print(Instructions)

input_user = input("\n\nEnter your input...")

for x in range(100):
    #........................................ add new list ............................................................
    if (input_user == '1'):
        add()

        print(todo_list)
        print(Instructions)
        input_user = input("\n\nEnter your input...")
    

    #........................................ update list ..................................................................
    elif (input_user == '2'):
        update()

        print(todo_list)
        print(Instructions)
        input_user = input("\n\nEnter your input...")
    

#.......................................... delete list ..................................................................
    elif (input_user == '3'):
        size = int(input("enter how many list you want to delete: "))
    
        for i in range(size):
            dict_name = input("Enter the name of list: ")
            del todo_list[dict_name]
            

        print(todo_list)
        print(Instructions)
        input_user = input("\n\nEnter your input...")

#......................................... display list ...................................................................
    elif (input_user == '4'):
        print(todo_list)
        print(Instructions)
        input_user = input("\n\nEnter your input...")

#......................................... store data .........................................................
    elif (input_user == '5'):
        input_store = input("Are you sure you want to store all the data in data file?? Press 1 for yes, press 2 for no.....")
        if(input_store == '1'):
            with open(filename, 'w') as f:
                f.write(to_do_string)
                print("list stored successfully!!")
            
        elif(input_store == '2'):
            print("ok,, thank you!!")
        else:
            print("wrong input!! try again....")
   

        print(Instructions)
        input_user = input("\n\nEnter your input...")

    elif (input_user == '6'):
        print("the app is shutting down, thank you!!")
        break

    
#.......................................... else ..........................................................................
    else:
        print("sorry!! try again.......")
        print(Instructions)
        input_user = input("\n\nEnter your input...")
    

