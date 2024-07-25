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
        # Refactor (A): Extract constants for option integers 
 
        #### Menu driven application #### 
        # Display menu and obtain menu choices 
        choice = self.display_menu() 
 
        while choice != 5: 
            if choice == 1: 
                assetTag = input("Enter asset tag >") 
                description = input("Enter description >") 
                 
                print("\nItem types:") 
                print("1. Digital Camera") 
                print("2. Laptop") 
                option = int(input("Enter option to select item type >")) 
                 
                if option == 1: 
                    opticalzoom = int(input("Enter optical zoom >")) 
                    result = self.inventory.addCamera(assetTag, description, opticalzoom) 
                     
                    if result: 
                        print("Digital camera added.") 
                    else: 
                        print("Error adding digital camera.") 
                         
                elif option == 2: 
                    os = input("Enter OS >") 
                    result = self.inventory.addLaptop(assetTag, description, os) 
                     
                    if result: 
                        print("Laptop added.") 
                    else: 
                        print("Error adding laptop.") 
                else: 
                    print("Invalid item type.") 
 
            elif choice == 2: 
                # Display Inventory 
                print("\nInventory:") 
                self.inventory.display() 
                print(self.inventory.getAvailableCamera()) 
                print(self.inventory.getAvailableLaptop()) 
                 
            elif choice == 3: 
                # Loan an item 
                print("") 
                print("==============================================") 
                print("Loan an item") 
                print("==============================================") 
                 
                print("\nItem types:") 
                print("1. Digital Camera") 
                print("2. Laptop") 
                option = int(input("Enter option to select item type >")) 
 
                # TO-DO: Write the code to LOAN a digital camera or laptop 
 
            elif choice == 4: 
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