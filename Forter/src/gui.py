from tkinter import Tk, Menu, Button, Label, Entry, Toplevel, IntVar
from count_unique_names import MAX_TYPOS,change_max_typos
def menu():
    # Create the main window
    root = Tk()
    root.title("Count Unique Names GUI")
    # Function to handle button click (replace with your desired action)
    def edit_max_typos():
        def update_max_typos(user_input):
            try:
                max_typos_input_int = user_input.get()  # Get the user input
                if max_typos_input_int < 0:
                    raise ValueError("Max typos cannot be negative")  # Handle negative input
                change_max_typos(max_typos_input_int)  # Update the global variable
                print(f"Max typos updated to: {max_typos_input_int}")  # Print for debugging
                max_typos_label.config(text=f"Max Typos Allowed: {max_typos_input_int}")  # Update the label
                edit_window.destroy()
            except ValueError as e:
                print(f"Error: {e}")  # Print error message for invalid input

        edit_window = Toplevel(root)  # Create a new top-level window
        edit_window.title("Edit Max Typos")

        # Label for max typos
        max_typos_label_edit = Label(edit_window, text="Max Typos Allowed:")
        max_typos_label_edit.pack(padx=5, pady=5)

        # Entry box for user input
        max_typos_user_input = IntVar(value=MAX_TYPOS)  # Initialize IntVar with current value
        entry = Entry(edit_window, textvariable=max_typos_user_input)  # Link entry to IntVar
        entry.pack(padx=5, pady=5)

        # Button to update max typos
        update_button = Button(edit_window, text="Update", command= lambda: update_max_typos(max_typos_user_input))
        update_button.pack(padx=5, pady=5)

    def button_click():
        print("Button clicked!")

    # Create three buttons
    global max_typos_label
    title_label = Label(root, text=f"Count Unique Names GUI")
    max_typos_label = Label(root, text=f"Max Typos Allowed: {MAX_TYPOS}")
    update_max_typos_button = Button(root, text="Set maximum amount of typos", command=edit_max_typos)
    button2 = Button(root, text="run all automated tests", command=button_click)
    button3 = Button(root, text="run a manual test", command=button_click)

    # Create the exit button
    exit_button = Button(root, text="Exit", command=root.quit)

    # Pack the buttons with additional arguments for centering
    root.columnconfigure(0, weight=1)  # Allow widgets to stretch horizontally
    root.rowconfigure(1, weight=1)  # Allow widgets to stretch vertically (for exit button)

    title_label.pack(fill="both", expand=True, padx=5, pady=5)
    max_typos_label.pack(fill="both", expand=True, padx=5, pady=5)
    update_max_typos_button.pack(fill="both", expand=True, padx=5, pady=5)
    button2.pack(fill="both", expand=True, padx=5, pady=5)
    button3.pack(fill="both", expand=True, padx=5, pady=5)



    # Pack the exit button at the bottom, still centered
    exit_button.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

    root.geometry("500x300")  # Adjust width and height as needed
    # Start the main event loop
    root.mainloop()



if __name__ == '__main__':
    menu()