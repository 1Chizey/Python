shopping_list = ["plantain"]
max_items = 10


menu = {"1":"chips", "2":"plantain", "3":"garri", "4":"yam", "5":"rice", "6":"beans", "7":"banana", "8":"bread", "9":"juice"}
while True:
    print("\nOptions: add / remove / view / exit")
    option = input("What will you like to do?: ").lower()

    # option 1 add
    if option == "add":
        print(f"Here is a list of available items:\n {menu}")
        while True:
            user_choice = input("kindly select the corressponding item number: ")
            if user_choice == "done":
                break
            if user_choice not in menu.keys():
                print("Wrong menu item seleted")
            else:
                print(f"{menu[user_choice]} has been added to your cart.")
                shopping_list.append(menu[user_choice])

    
    #option 2 remove
    elif option == "remove":
        print("What item do you want to remove?:")
        # print(f"Here is a list of available items:\n {user_choice(shopping_list)}")
        while True:
            user_choice = input("enter item to be removed: ")
            if user_choice in shopping_list:
                shopping_list.remove(user_choice)
                print(f"{user_choice} has be removed from your shopping list")
                for item in shopping_list:
                    print(item)
            elif user_choice == "done":
                break
            else:
                print("Item not found!")
    
    # option 3
    elif option == "view":
       for item in shopping_list:
          print(item)
    
    # option 4      
    elif option == "exit":
        print("Thank You For Shopping With Us!!❤️")
        break


    

    else:
        print("Invalid choice. Please kindly type add, remove, view, or exit. ")
    
