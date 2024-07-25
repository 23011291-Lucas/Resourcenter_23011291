from inventory.inventory import Inventory 
 
class ResourceCenter: 
    def __init__(self): 
        ## Prepare the data (Inventory list) 
        self.inventory = Inventory() 
 
    def display_menu(self): 
        choice = -1 
        while not 1 <= choice <= 5: 
            print("\n==============================================") 
            print('RESOURCE CENTRE SYSTEM:') 
            print("1. Add item") 
            print("2. Display Inventory") 
            print("3. Loan item") 
            print("4. Return item") 
            print("5. Quit") 
            choice = int(input("Enter your choice >")) 
            if not 1 <= choice <= 5: 
                print("Invalid choice, please enter again.\n") 
        return choice 
 
    def main(self): 
        # Refactor (A): Extract constants for choice integers 
        CHOICE_ADD = 1
        CHOICE_VIEW = 2
        CHOICE_LOAN = 3
        CHOICE_RETURN = 4
        CHOICE_QUIT = 5
        # Refactor (A): Extract constants for option integers
        OPTION_CAMERA = 1
        OPTION_LAPTOP = 2
 
        #### Menu driven application #### 
        # Display menu and obtain menu choices 
        choice = self.display_menu() 
 
        while choice != CHOICE_QUIT: 
            if choice == CHOICE_ADD: 
                assetTag = input("Enter asset tag >") 
                description = input("Enter description >") 
                 
                print("\nItem types:") 
                print("1. Digital Camera") 
                print("2. Laptop") 
                option = int(input("Enter option to select item type >")) 
                 
                if option == OPTION_CAMERA: 
                    opticalzoom = int(input("Enter optical zoom >")) 
                    result = self.inventory.addCamera(assetTag, description, opticalzoom) 
                     
                    if result: 
                        print("Digital camera added.") 
                    else: 
                        print("Error adding digital camera.") 
                         
                elif option == OPTION_LAPTOP: 
                    os = input("Enter OS >") 
                    result = self.inventory.addLaptop(assetTag, description, os) 
                     
                    if result: 
                        print("Laptop added.") 
                    else: 
                        print("Error adding laptop.") 
                else: 
                    print("Invalid item type.") 
 
            elif choice == CHOICE_VIEW: 
                # Display Inventory 
                print("\nInventory:") 
                self.inventory.display() 
                print(self.inventory.getAvailableCamera()) 
                print(self.inventory.getAvailableLaptop()) 
                 
            elif choice == CHOICE_LOAN: 
                # Loan an item 
                print("") 
                print("==============================================") 
                print("Loan an item") 
                print("1==============================================") 
                 
                print("\nItem types:") 
                print("1. Digital Camera") 
                print("2. Laptop") 
                option = int(input("Enter option to select item type >")) 
 
                # TO-DO: Write the code to LOAN a digital camera or laptop 
 
            elif choice == CHOICE_RETURN: 
                # Return an item 
                print("") 
                print("==============================================") 
                print("Return an item") 
                print("==============================================") 
                 
                print("\nItem types:") 
                print("1. Digital Camera") 
                print("2. Laptop") 
                option = int(input("Enter option to select item type >")) 
 
                # TO-DO: Write the code to RETURN a digital camera or laptop 
 
            else: 
                print("Invalid choice.") 
             
            choice = self.display_menu() 
 
        print("Good bye.") 
 
if __name__ == "__main__": 
    app = ResourceCenter() 
    app.main()