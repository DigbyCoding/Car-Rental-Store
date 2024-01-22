import customtkinter as ctk 
import tkinter as tk 
import CTkMessagebox as ctkmb 


class Login(ctk.CTkToplevel):
        def __init__(self):
                super().__init__()
                self.geometry('580x1100')
                self._set_appearance_mode('system')
                
                self.frame = ctk.CTkFrame(master = self, width = 500, height = 500)
                self.frame.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)
    
                self.username = ctk.CTkEntry(master = self.frame, placeholder_text = 'Username: ', width = 150, height = 30,)
                self.password = ctk.CTkEntry(master = self.frame, placeholder_text = 'Password: ', width = 150, height = 30, show = '*')

                self.username.place( relx = 0.5, rely = 0.2, anchor = ctk.CENTER)
                self.password.place( relx = 0.5, rely = 0.3, anchor = ctk.CENTER)

                self.login_Button = Button_item(master = self.frame, name = 'Login', user = self, password = self)
                self.login_Button.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

                self.signup_Button = Button_item(master = self.frame, name = 'Sign Up', user = self, password = self)
                self.signup_Button.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)
        
        def get_User(self):
                return self.username.get()
        
        def get_Pass(self):
                return self.password.get()
            

class Button_item(ctk.CTkButton):
        def __init__(self, master, name, user, password):
                super().__init__(master, text = name, command= self.login_Button, width = 100, height = 30)
                
                self.get_user = user
                self.get_password = password
        
        def getName(self):
                return self._text
        
        def login_Button(self):
                textName = self.getName()

                if textName == 'Login':
                        print('you have logged in')
                        # move onto homepage 
                elif textName == 'Sign Up':
                        print('you have signed up your Username and Password Are: ')
                        print(self.get_user.get_User())
                        print(self.get_password.get_Pass())
                        # move onto homepage
        


        
                

login = Login()
login.mainloop()

