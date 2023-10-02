import tkinter as tk
#cool litle borat program
def show_message_window(message, count):
    # Create the main window
    root = tk.Tk()
    root.title("Message Window")

    # Function to display the message
    def display_message():
        nonlocal count
        if count > 0:
            label.config(text=message)
            count -= 1
            root.after(1000, display_message)  # Display for 1 second
        else:
            root.destroy()

    label = tk.Label(root, text="")
    label.pack(padx=20, pady=20)

    # Start displaying the message
    display_message()

    root.mainloop()

if __name__ == "__main__":
    message = "BORAT IS THE BEST AND KAZAKSTAN IS THE BEST"  # Change this to your desired message
    count = 999
    show_message_window(message, count)
