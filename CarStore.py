import customtkinter # Import the customtkinter library
import Items.Hamburger as Hamburger # Import the Hamburger module
import Items.HomeRow as HomeRow # Import the HomeRow module

WINDOW_HEIGHT = 1100 # Set the window height
WINDOW_WIDTH = 580 # Set the window width

customtkinter.set_appearance_mode("System")  # Set the appearance mode of the customtkinter
# Available modes: "System" (standard), "Dark" "Light"
customtkinter.set_default_color_theme("blue")  # Set the default color theme of the customtkinter library
# Available themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Car Store") # Set the window title
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}") # Set the window size

        # Create an instance of the Button class from the Hamburger module
        self.button_instance = Hamburger.Button(self)

        self.test = HomeRow.HomeRow(self)
        self.test2 = HomeRow.HomeRow(self)
        self.test3 = HomeRow.HomeRow(self)

if __name__ == "__main__":
    app = App() # Create an instance of the App class
    app.mainloop() # Start the main event loop of the application
