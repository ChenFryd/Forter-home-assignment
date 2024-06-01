import unittest
from tkinter import Tk, Menu, Button, Label, Entry, Toplevel, IntVar
from count_unique_names import get_max_typos,change_max_typos, countUniqueNames
from names_testing import MyTestCase
def menu():
    root = Tk()
    root.title("Count Unique Names GUI")
    def edit_max_typos():
        """
        Opens a new window to edit the maximum amount of typos allowed
        """
        def update_max_typos(user_input):
            """
            the function that updates the maximum amount of typos allowed
            :param user_input: the new maximum amount of typos allowed
            """
            try:
                max_typos_input_int = user_input.get()  # Get the user input
                if max_typos_input_int < 0:
                    raise ValueError("Max typos cannot be negative")  # Handle negative input
                change_max_typos(max_typos_input_int)  # Update the global variable
                print(f"Max typos updated to: {max_typos_input_int}")  # Print for debugging
                max_typos_label.config(text=f"Max Typos Allowed: {max_typos_input_int}")  # Update the label
            except ValueError as e:
                output_label.config(text=f"Error: {e}")
                print(f"Error: {e}")  # Print error message for invalid input
            edit_window.destroy()

        edit_window = Toplevel(root)  # Create a new top-level window
        edit_window.title("Edit Max Typos")

        # Label for max typos
        max_typos_label_edit = Label(edit_window, text="Max Typos Allowed:")
        max_typos_label_edit.pack(padx=5, pady=1)

        # Entry box for user input
        max_typos_user_input = IntVar(value=get_max_typos())  # Initialize IntVar with current value
        entry = Entry(edit_window, textvariable=max_typos_user_input)  # Link entry to IntVar
        entry.pack(padx=5, pady=5)

        # Button to update max typos
        update_button = Button(edit_window, text="Update", command= lambda: update_max_typos(max_typos_user_input))
        update_button.pack(padx=5, pady=5)

        edit_window.geometry("+%d+%d" % (root.winfo_rootx() + 200, root.winfo_rooty() + 100))

    def run_all_tests():
        """
        Runs all automated tests, prints the results to the console, and updates the output label.
        """
        print("Running all automated tests")
        test_suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
        results = unittest.TextTestRunner(verbosity=2).run(test_suite)
        num_failures = len(results.failures)
        total = results.testsRun
        output_label.config(text=f"All tests complete. Tests run: {total}, Failures: {num_failures}, acceptance: {((total - num_failures)*100)/total}%")

    def run_manual_test_button():
        def handle_submission(entries):
            """Handles user input from the entry boxes."""
            # Access user input from entries
            user_input = [entry.get() for entry in entries]
            try:
                if int(user_input[-1]) < 0:
                    raise Exception("Expected result cannot be negative")
                amount_of_unique_names = countUniqueNames(*user_input[:-1])
                print(f"Manual test input: {user_input}")
                print(f"Manual test output: {amount_of_unique_names}")
                status = "PASS" if amount_of_unique_names == int(user_input[-1]) else "FAIL"
                output_label.config(
                    text=f"{status}! Manual test output: {amount_of_unique_names}, expected: {user_input[-1]}")
            except Exception as e:
                print(f"Error: {e}")
                output_label.config(text=f"Error: {e}")
            manual_window.destroy() # Close the window

        manual_window = Toplevel(root)
        manual_window.title("Manual Test")

        # Define labels and entry boxes
        labels = ["Bill first name:", "Bill last name:", "ship first name:", "Bill last name:", "Bill name on card:", "Expected result"]
        placeholder_values = ["John", "Doe", "John", "Doe", "John Doe", "1"]
        entries = []
        for i, label_text in enumerate(labels):
            label = Label(manual_window, text=label_text)
            label.grid(row=i, column=0)

            entry = Entry(manual_window, width=20)
            entry.insert(0, placeholder_values[i])
            entry.grid(row=i, column=1)
            entries.append(entry)

        # Submit button
        submit_button = Button(manual_window, text="Submit", command=lambda: handle_submission(entries))
        submit_button.grid(row=len(labels), columnspan=2)

        # Center the window
        manual_window.geometry("+%d+%d" % (root.winfo_rootx() + 200, root.winfo_rooty() + 100))

    # labels
    title_label = Label(root, text=f"Count Unique Names GUI")
    max_typos_label = Label(root, text=f"Max Typos Allowed: {get_max_typos()}")
    output_label = Label(root, text="")

    # Create the buttons
    update_max_typos_button = Button(root, text="Set maximum amount of typos", command=edit_max_typos)
    run_all_tests_button = Button(root, text="run all automated tests", command=run_all_tests)
    run_manual_test_button = Button(root, text="run a manual test", command=run_manual_test_button)
    exit_button = Button(root, text="Exit", command=root.quit)

    # Pack the buttons with additional arguments for centering
    root.columnconfigure(0, weight=1)  # Allow widgets to stretch horizontally
    root.rowconfigure(1, weight=1)  # Allow widgets to stretch vertically (for exit button)

    title_label.pack(fill="both", expand=True, padx=5, pady=5)
    max_typos_label.pack(fill="both", expand=True, padx=5, pady=5)
    output_label.pack(fill="both", expand=True, padx=5, pady=5)
    update_max_typos_button.pack(fill="both", expand=True, padx=5, pady=5)
    run_all_tests_button.pack(fill="both", expand=True, padx=5, pady=5)
    run_manual_test_button.pack(fill="both", expand=True, padx=5, pady=5)

    # Pack the exit button at the bottom, still centered
    exit_button.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)


    #center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    x = (screen_width - window_width) // 3
    y = (screen_height - window_height) // 3
    root.wm_geometry(f"+{x}+{y}")
    root.geometry("500x300")  # Adjust width and height as needed
    # Start the main event loop
    root.mainloop()

if __name__ == '__main__':
    menu()