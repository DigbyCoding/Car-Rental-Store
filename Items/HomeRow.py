##
# This line imports a module called customtkinter, which presumably 
# contains custom classes for creating GUI elements.
#
import customtkinter

##
# This line defines a class called HomeRow, that inherits from the
# CTkFrame class from the customtkinter module. This means that
# HomeRow is a specialised version of a frame widget.
# 
class HomeRow(customtkinter.CTkFrame):
    ##
    # This is the constructor method of the HomeRow class. It takes a
    # master parameter, which is the parent widget. If first calls the 
    # constructor of the CTkFrame class using the super() function,
    # passing the master parameter and setting the width and height of
    # the frame. Then, it uses the place() method to position the frame
    # at the coordinates (0, 1000) within its parent widget.
    #
    def __init__(self, master):
        super().__init__(master, width=580, height=100)
        self.place(x = 0, y= 1000)

        self.homeButton()
        self.settingsButton()
        self.myCarButton()

    ##
    # This method creates a button widget called homeButton using the
    # CTKButton class from the customtkinter module. It sets the text
    # of the button to "🏠" (this will be changed later), associates
    # it with the homeButtonFunctionality method as its command, and
    # sets its width and height. Finally, it uses the place() method
    # to position the button at coordinates (107, 0.25) * height of
    # the frame) relative to the top-left corner of the frame.
    #
    def homeButton(self):
        self.homeButton = customtkinter.CTkButton(
            self, 
            text="🏠",
            command=self.homeButtonFunctionality,
            width=50,
            height= 50
        )
        self.homeButton.place(x = 107, rely = 0.25)
    ##
    # This method is similar to the homeButton() method, but it
    # creates a button with the text "⚙️" (this will also be changed)
    # and associates it with the settingsButtonFunctionality method
    # as its command. It possitions the button at coordinates (265, 0.25
    # * the height of the frame) relative to the top-left corner of
    # the frame.
    #
    def settingsButton(self):
        self.settingsButton = customtkinter.CTkButton(
            self,
            text="⚙️",
            command=self.settingsButtonFunctionality,
            width=50,
            height= 50
        )
        self.settingsButton.place(x = 265, rely = 0.25)

    ##
    # This method is similar to the previous two methods, but it creates
    # a button with the text "🚗" (also being changed soon) and associates
    # it with the myCarButtonFunctionality method as its command. Its
    # possitions the button at coordinates (423, 0.25 * height of the frame)
    # relative to the top-left corner of the frame.
    #
    def myCarButton(self):
        self.myCarButton = customtkinter.CTkButton(
            self,
            text="🚗",
            command=self.myCarButtonFunctionality,
            width=50,
            height= 50
        )
        self.myCarButton.place(x = 423, rely = 0.25)

    ##
    # This will get changed at some point
    #
    def homeButtonFunctionality(self):
        print("This will take you to the home page.")
    ##
    # This will get changed at some point
    #
    def settingsButtonFunctionality(self):
        print("This will take you to the settings page.")
    ##
    # This will get changed at some point
    #
    def myCarButtonFunctionality(self):
        print("This will take you to the myCar page.")