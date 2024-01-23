import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, master):
        super().__init__(master, text="=", command=self.customButton, width= 50, height = 50)
        self.place(relx = 0, rely = 0)
        self.toggle = False

    def customButton(self):
        # Check if the toggle flag is False
        if self.toggle == False:
            # Create a custom frame with a width of 200 and a height of 200
            self.frame = customtkinter.CTkFrame(self.master, width=200, height=200)
            # Place the frame at coordinates (50, 0) relative to the master widget
            self.frame.place(x = 50, y = 0)

            # Create a HamburgerItem button with the name "logout" and place it in the custom frame
            self.logoutButton = HamburgerItem(self.frame, "logout")
            self.logoutButton.place(x = 50, y = 25)

            # Create a HamburgetItem button with the name "Exit" and place it in the custom frame
            self.exitButton = HamburgerItem(self.frame, "exit")
            self.exitButton.place(x = 50, y = 75)

            # Set the toggle flag to True
            self.toggle = True

        # Check if the toggle flag is True
        elif self.toggle == True:
            # Destroy the custom frame
            self.frame.destroy()
            # Set the toggle flag to False
            self.toggle = False

    
class HamburgerItem(customtkinter.CTkButton):
    def __init__(self, master, name):
        super().__init__(master, text=name, command = self.hamburgerItemButton, width=100, height=25)
        
    def getName(self):
        return self._text
    
    def hamburgerItemButton(self):        
        # Get the name of the button
        textName = self.getName()

        # Check if the name is "logout"
        if  textName == "logout":
            # Takes you to login page.
            print("You have logged out")
        #Check if the name is "Exit"
        elif textName == "exit":
            # Exits the program
            exit()