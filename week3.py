name_and_number = {
    "Johirnadh" : 9515096362,
    "manoj" :9849592156,
    "vamsi" : 8465846874,
}
details = {
    "Johirnadh" : "friend",
    "manoj" : "friend",
    "vamsi" : "friend"
}
def Add() :
    name = input("Enter the name you want to add: ")
    number = input("Enter the number : ")
    description=input("eneter the details :")
    if name and number in name_and_number :
        print("the contact is already exist")
    else :
        name_and_number[name]=number
        details[name]=description
        print("the number is addedin you phone book")
        
def Remove() :
    name = input("Enter the name you want to delete: ")
    name_and_number.pop(name)
    print("the name is removed")
    
def View() :
    print(name_and_number,details)
    
contactadd = "add"
contactremove = "remove"
contactview = "view"

def main() :
    for i in range(10):
        a = input("Enter add/remove/view/exit : ")
        if contactadd == a :
            Add()
        elif a == contactremove :
            Remove()
        elif a == contactview :
            View()
        elif a == "exit":
            break
        else :
            print("try again")

main()
