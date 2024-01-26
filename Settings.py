import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('580x1100')

        self.frame = ctk.CTkFrame(master = self, width = 500, height = 500)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)
        self.appearance_mode_label = ctk.CTkLabel(master = self.frame, text = 'Appearance Mode:', anchor = 'w')
        self.appearance_mode_label.place(relx = 0.125, rely = 0.3, anchor = ctk.CENTER)
        self.appearance_mode_option_menu = ctk.CTkOptionMenu(master = self.frame, values = ['System','Dark','Light'], command = self.change_appearance_mode_event)
        self.appearance_mode_option_menu.place(relx = 0.0, rely = 0.38, anchor = 'w')

        self.UI_slider_label = ctk.CTkLabel(master = self.frame, text = 'Scale:', anchor = 'w' )
        self.UI_slider_label.place(relx = 0.125, rely = 0.5, anchor = 'w')
        self.slider = ctk.CTkSlider(master = self.frame, from_ = 80, to= 120, command = self.change_scaling)
        self.slider.place(relx = 0.0, rely = 0.57, anchor = 'w')


        self.contact_button = ctk.CTkButton(master = self.frame, width = 100, height = 30, text = 'Contact', command = self.contact )
        self.contact_button.place(relx = 0.0, rely = 0.67, anchor = 'w')

    
    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def change_scaling(self, value):
        scale_factor = int(value) / 100
        ctk.set_widget_scaling(scale_factor)
    
    def contact(self):
        self.new_window = ctk.CTkToplevel()
        self.new_window.geometry('580x1100')

        self.new_frame = ctk.CTkFrame(master = self.new_window, width = 500, height = 500)
        self.new_frame.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

        self.textbox = ctk.CTkTextbox(master = self.new_frame, width = 350, height = 350, )
        self.textbox.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

        self.collect_text_button = ctk.CTkButton(master = self.new_frame, width = 100, height = 30, text = 'Submit', command = self.get_text )
        self.collect_text_button.place(relx = 0.15, rely = 0.9, anchor = 'w')

        self.new_window.focus()

    def get_text(self):
        self.paragraph = self.textbox.get('1.0', ctk.END)
        print(self.paragraph)
        


if __name__ == '__main__':
    app = App()
    app.mainloop()