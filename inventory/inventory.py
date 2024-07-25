
from inventory.camera import Camera
from inventory.laptop import Laptop

class Inventory():
    pass

    def __init__(self):
        self.cameraList = []
        self.laptopList = []
    
    def findAsset(self, assetTag): 
         
        # Refactor (C): Extract long methods to findCamera(assetTag),  
        # return the found camera, return None if not found. 
        # **Don't forget to create test cases for this new method. 
        # Check for existing camera 
        foundAsset = None 
         
        for c in self.cameraList: 
            currentTag = c.getAssetTag() 
             
            if currentTag == assetTag: 
                foundAsset = c 
                 
        for c in self.laptopList: 
            currentTag = c.getAssetTag() 
             
            if currentTag == assetTag: 
                foundAsset = c    
                 
        return foundAsset    
        
        
    def addLaptop(self, assetTag, description, os):
        # Check for correct values
        correct = True
        if len(assetTag)==0 or len(description)==0 or len(os)==0:
            correct = False
            error_message = "Incorrect values."
        # Refactor (C): Extract long methods to findLaptop(assetTag), 
        # return the found laptop, return None if not found.
        # **Don't forget to create test cases for this new method.
        # Check for existing laptop
        if self.findAsset(assetTag) != None: 
            error_message = "Asset already exists." 
                 
        if correct and self.findAsset(assetTag) == None: 
            new_laptop = Laptop(assetTag, description, os) 
            self.laptopList.append(new_laptop) 
            return True
        else:
            print(error_message)
            return False


    def addCamera(self, assetTag, description, opticalzoom):
        # Check for correct values
        correct = True
        if len(assetTag)==0 or len(description)==0 or opticalzoom<0:
            correct = False
            error_message = "Incorrect values."
        # Refactor (C): Extract long methods to findCamera(assetTag), 
        # return the found camera, return None if not found.
        # **Don't forget to create test cases for this new method.
        # Check for existing camera
        notExist = True       
        for l in self.laptopList:
            currentTag = l.getAssetTag()            
            if currentTag == assetTag:
                notExist = False
                error_message = "Asset already exists."
        
        if self.findAsset(assetTag) != None: 
            error_message = "Asset already exists." 
                 
        if correct and self.findAsset(assetTag) == None: 
            new_laptop = Laptop(assetTag, description, os)
            self.laptopList.append(new_laptop) 
            return True
        else:
            print(error_message)
            return False
        
        ############### Test add laptop ######################
    def test_add_laptop(self):
        test_inventory = Inventory()
        assert len(test_inventory.laptopList) == 0
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        assert result == True
        assert len(test_inventory.laptopList) == 1
    def test_add_existing_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        original_len = len(test_inventory.laptopList)
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        assert result == False
        assert len(test_inventory.laptopList) == original_len
    def test_add_laptop_missing_description(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        original_len = len(test_inventory.laptopList)
        result = test_inventory.addLaptop("L004", "", "WIN10")
        assert result == False
        assert len(test_inventory.laptopList) == original_len
    def test_add_laptop_missing_os(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        original_len = len(test_inventory.laptopList)
        result = test_inventory.addLaptop("L004", "Test Laptop 4", "")
        assert result == False
        assert len(test_inventory.laptopList) == original_len

    def getAvailableCamera(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        if len(self.cameraList) == 0:
            output += "There is no camera to display."
        else:
            for i in self.cameraList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += str(i)
            
        return output

    def getAvailableLaptop(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for i in self.laptopList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += str(i)
        return output
    def loanAsset(self, assetTag, dueDate): 
        success = False 
        if len(assetTag) > 0 and len(dueDate) > 0: 
            foundAsset = self.findAsset(assetTag) 
            if foundAsset != None: 
                if foundAsset.getIsAvailable() == "Yes": 
                    foundAsset.setIsAvailable(False) 
                    foundAsset.setDueDate(dueDate) 
                    success = True 
                         
        return success 
     
    def loanCamera(self, assetTag, dueDate): 
        return self.loanAsset(assetTag, dueDate) 
     
    def loanLaptop(self, assetTag, dueDate):  
        return self.loanAsset(assetTag, dueDate)


















































