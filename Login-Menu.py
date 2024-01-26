# imports all the modules 
import customtkinter as ctk 
import tkinter as tk 
from CTkMessagebox import CTkMessagebox as ctkmb 
import Database_Intergration

# create a login class with toplevel window and set up window 
class Login(ctk.CTkToplevel):
        def __init__(self):
                super().__init__()
                self.geometry('580x1100')
                #self._set_appearance_mode('system')
                
                #create frame to place all entry and buttons for login
                self.frame = ctk.CTkFrame(master = self, width = 500, height = 500)
                self.frame.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)
    
                #create entry fields for user to enter username and passwrod and places them on the fame
                self.username = ctk.CTkEntry(master = self.frame, placeholder_text = 'Username: ', width = 150, height = 30,)
                self.password = ctk.CTkEntry(master = self.frame, placeholder_text = 'Password: ', width = 150, height = 30, show = '*')

                self.username.place( relx = 0.5, rely = 0.2, anchor = ctk.CENTER)
                self.password.place( relx = 0.5, rely = 0.3, anchor = ctk.CENTER)

                #create buttons for user to choose to sign up or login and places them on the fame
                self.login_Button = Button_item(master = self.frame, name = 'Login', user = self, password = self)
                self.login_Button.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

                self.signup_Button = Button_item(master = self.frame, name = 'Sign Up', user = self, password = self)
                self.signup_Button.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)
        
        #reurns the username and password entrys to be used to validate later 
        def get_User(self):
                return self.username.get()
        
        def get_Pass(self):
                return self.password.get()
            
#creates a button class to make diffferent buttons and initalise them
class Button_item(ctk.CTkButton):
        def __init__(self, master, name, user, password):
                super().__init__(master, text = name, command= self.login_Button, width = 100, height = 30)
                
                self.get_user = user
                self.get_password = password
        
        #gets the name of the button
        def getName(self):
                return self._text
        
        #gives function to the button depending on the name of the button
        def login_Button(self):
                textName = self.getName()

        #checks what type of button the user clicked and validates the username and password 
        #then proceeds to the homepage if all checks are passed
                
                if textName == 'Login':
                        if len(self.get_user.get_User()) == 0 or len(self.get_password.get_Pass()) == 0:
                                print('unsucessful login try again')
                                ctkmb(message = 'Unsucessful Login Try Again', icon = 'cancel')
                        else:
                                #try:
                                        get_check_username = self.get_user.get_User()
                                        get_check_password = self.get_password.get_Pass()
                                        check_username = Database_Intergration.runSQL(f"SELECT Username FROM Login WHERE Username = '{get_check_username}'", True)
                                        #check_password = Database_Intergration.runSQL(f"SELECT Password FROM Login")
                                        print('you have logged in')
                                        ctkmb(title = 'Logged in', message = 'Sucessfully Logged In! ', icon = 'check')
                                #except:
                                        print('why')
                                # move onto homepage

                elif textName == 'Sign Up':
                        if len(self.get_user.get_User()) == 0 or len(self.get_password.get_Pass()) == 0:
                                print('unsucessful Sign Up try again')
                                ctkmb(message = 'Unsucessful Sign Up Try Again', icon = 'cancel')
                        else:
                                print('you have signed up your Username and Password Are: ')
                                print(self.get_user.get_User())
                                print(self.get_password.get_Pass())
                                ctkmb(title = 'Signed Up', message = 'Signed Up Sucessfully', icon = 'check')
                                # move onto homepage
                                

login = Login()
login.mainloop()

