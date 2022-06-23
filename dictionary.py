dictionary = {
    'dog': {
        'description': 'A domestic animal with four legs.',   
    },
    'bark': {
        'description': 'The sound create when dog shouts',
    }
}
filename = 'dictionary.txt'

dictionary_string = str(dictionary)

print("................................welcome to your to do list....................................................\n\n\n here you can do the following task....")

Instructions = "\n1: enter 1 to add a new word.\n2: enter 2 to update the description.\n3: enter 3 to delete word.\n4: enter 4 to show all the words.\n5: enter 5 to search word by keyword\n6: enter 6 to store all data in a txt file\n7: enter 7 to quit this app"

print(Instructions)

input_user = input("\n\nEnter your input...")

def add():
    size = int(input("enter how many words you want to add: "))

    for i in range(size):
        dict_name = input("Enter the keyword: ")

        dictionary[dict_name] = {}
        description = input("Enter description: ")
        dictionary[dict_name]['description'] = description

def update():
    size = int(input("enter how many words you want to update: "))

    for i in range(size):
        dict_name = input("Enter the keyword: ")

        dictionary[dict_name] = {}
        description = input("Enter description: ")
        dictionary[dict_name]['description'] = description


    

for x in range(100):
    #........................................ add new word ............................................................
    if (input_user == '1'):
        add()

        print(dictionary)
        print(Instructions)
        input_user = input("\n\nEnter your input...")

#........................................ update dictionary ..................................................................
    elif (input_user == '2'):
        update()

        print(dictionary)
        print(Instructions)
        input_user = input("\n\nEnter your input...")

#.......................................... delete list ..................................................................
    elif (input_user == '3'):
        size = int(input("enter how many words you want to delete: "))
    
        for i in range(size):
            dict_name = input("Enter the word: ")
            del dictionary[dict_name]

            print(dictionary)
            print(Instructions)
            input_user = input("\n\nEnter your input...")

#......................................... display list ...................................................................
    elif (input_user == '4'):
        print(dictionary)
        print(Instructions)
        input_user = input("\n\nEnter your input...")

#...................................... search .......................................................................
    elif(input_user == '5'):
        dict_name = input("Enter the keyword: ")
        try:
            dictionary[dict_name]
            search = dictionary[dict_name]
    
            print(search)
        except KeyError:
            print("not found")
        except:
            print("not found")

        print(Instructions)
        input_user = input("\n\nEnter your input...")

    elif(input_user == '6'):
        input_store = input("Are you sure you want to store all the data in data file?? Press 1 for yes, press 2 for no.....")
        if(input_store == '1'):
            with open(filename, 'w') as f:
                f.write(dictionary_string)
                print("dictionary stored successfully!!")
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

