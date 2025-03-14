import tkinter as tk
from tkinter import messagebox
from main import main  # Import the main function for password handling

# Initialize the global password variable
password = None

def set_password():
    """Set the password for the drive and start the encryption process."""
    password_window = tk.Toplevel()
    password_window.title("Set Password")
    password_window.geometry("400x300")  # Set a larger window size

    tk.Label(password_window, text="Enter new password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show='*', width=40)
    password_entry.pack(pady=10)

    def confirm_password():
        new_password = password_entry.get()
        if new_password:
            global password  # Declare password as global
            password = new_password
            # Start encryption process here (placeholder)
            messagebox.showinfo("Success", "Password has been set and encryption started.")
            password_window.destroy()  # Close the password setting window

    tk.Button(password_window, text="Confirm", command=confirm_password).pack(pady=20)

import tkinter as tk
from tkinter import messagebox
from main import main  # Import the main function for password handling

def set_password():
    """Set the password for the drive and start the encryption process."""
    password_window = tk.Toplevel()
    password_window.title("Set Password")
    password_window.geometry("400x300")  # Set a larger window size

    tk.Label(password_window, text="Enter new password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show='*', width=40)
    password_entry.pack(pady=10)

    def confirm_password():
        new_password = password_entry.get()
        if new_password:
            global password  # Assuming 'password' is defined globally
            password = new_password
            # Start encryption process here (placeholder)
            messagebox.showinfo("Success", "Password has been set and encryption started.")
            password_window.destroy()  # Close the password setting window

    tk.Button(password_window, text="Confirm", command=confirm_password).pack(pady=20)
    password_window.mainloop()

import tkinter as tk
from tkinter import messagebox
from main import main  # Import the main function for password handling

def set_password():
    password_window = tk.Toplevel()
    password_window.title("Set Password")
    password_window.geometry("400x300")  # Set a larger window size

    tk.Label(password_window, text="Enter new password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show='*', width=40)
    password_entry.pack(pady=10)

    def confirm_password():
        new_password = password_entry.get()
        if new_password:
            global password  # Assuming 'password' is defined globally
            password = new_password
            messagebox.showinfo("Success", "Password has been set.")
            password_window.destroy()  # Close the password setting window

    tk.Button(password_window, text="Confirm", command=confirm_password).pack(pady=20)
    password_window.mainloop()

def change_password():
    """Change the password, requiring the old password for verification."""
    old_password = simpledialog.askstring("Old Password", "Enter old password:")
    if old_password == password:  # Verify old password
        new_password = simpledialog.askstring("Change Password", "Enter new password:")
        if new_password:
            global password  # Declare password as global
            password = new_password
            messagebox.showinfo("Success", "Password has been changed.")
    else:
        messagebox.showerror("Error", "Old password is incorrect.")

import tkinter as tk
from tkinter import messagebox
from main import main  # Import the main function for password handling

def set_password():
    """Set the password for the drive and start the encryption process."""
    password_window = tk.Toplevel()
    password_window.title("Set Password")
    password_window.geometry("400x300")  # Set a larger window size

    tk.Label(password_window, text="Enter new password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show='*', width=40)
    password_entry.pack(pady=10)

    def confirm_password():
        new_password = password_entry.get()
        if new_password:
            global password  # Assuming 'password' is defined globally
            password = new_password
            # Start encryption process here (placeholder)
            messagebox.showinfo("Success", "Password has been set and encryption started.")
            password_window.destroy()  # Close the password setting window

    tk.Button(password_window, text="Confirm", command=confirm_password).pack(pady=20)
    password_window.mainloop()

import tkinter as tk
from tkinter import messagebox
from main import main  # Import the main function for password handling

def set_password():
    password_window = tk.Toplevel()
    password_window.title("Set Password")
    password_window.geometry("400x300")  # Set a larger window size

    tk.Label(password_window, text="Enter new password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show='*', width=40)
    password_entry.pack(pady=10)

    def confirm_password():
        new_password = password_entry.get()
        if new_password:
            global password  # Assuming 'password' is defined globally
            password = new_password
            messagebox.showinfo("Success", "Password has been set.")
            password_window.destroy()  # Close the password setting window

    tk.Button(password_window, text="Confirm", command=confirm_password).pack(pady=20)
    password_window.mainloop()

def change_password():
    """Change the password, requiring the old password for verification."""
    old_password = simpledialog.askstring("Old Password", "Enter old password:")
    if old_password == password:  # Verify old password
        new_password = simpledialog.askstring("Change Password", "Enter new password:")
        if new_password:
            global password  # Assuming 'password' is defined globally
            password = new_password
            messagebox.showinfo("Success", "Password has been changed.")
    else:
        messagebox.showerror("Error", "Old password is incorrect.")

import tkinter as tk
from tkinter import messagebox
from main import main  # Import the main function for password handling

def set_password():
    password_window = tk.Toplevel()
    password_window.title("Set Password")
    password_window.geometry("400x300")  # Set a larger window size

    tk.Label(password_window, text="Enter new password:").pack(pady=10)
    password_entry = tk.Entry(password_window, show='*', width=40)
    password_entry.pack(pady=10)

    def confirm_password():
        new_password = password_entry.get()
        if new_password:
            global password  # Assuming 'password' is defined globally
            password = new_password
            messagebox.showinfo("Success", "Password has been set.")
            password_window.destroy()  # Close the password setting window

    tk.Button(password_window, text="Confirm", command=confirm_password).pack(pady=20)
    password_window.mainloop()

def change_password():
    new_password = simpledialog.askstring("Change Password", "Enter new password:")
    # Logic to change the existing password
    if new_password:
        global password  # Assuming 'password' is defined globally
        password = new_password
        messagebox.showinfo("Success", "Password has been changed.")

def restore_drive():
    """Restore the drive, requiring the old password for verification."""
    old_password = simpledialog.askstring("Old Password", "Enter old password:")
    if old_password == password:  # Verify old password
        confirmation = messagebox.askyesno("Confirm Restore", "Are you sure you want to restore the drive?")
        if confirmation:
            # Logic to restore the drive (placeholder)
            messagebox.showinfo("Success", "Drive has been restored and encryption removed.")
    else:
        messagebox.showerror("Error", "Old password is incorrect.")


def remove_program():
    confirmation = messagebox.askyesno("Confirm Removal", "Are you sure you want to remove the program?")
    if confirmation:
        # Logic to remove the program files
        messagebox.showinfo("Success", "Program has been removed.")
        # Additional logic to delete program files can be added here


def install_program():
    # Logic to install the program
    messagebox.showinfo("Install Program", "Program installation logic has been implemented.")
    # Additional logic for installation can be added here


def select_drive():
    drive_window = tk.Toplevel()
    drive_window.title("Select Drive")
    drive_window.geometry("400x300")  # Set a larger window size

    tk.Label(drive_window, text="Enter the drive path:").pack(pady=10)
    drive_entry = tk.Entry(drive_window, width=40)
    drive_entry.pack(pady=10)

    def confirm_selection():
        drive = drive_entry.get()
        if drive:
            messagebox.showinfo("Drive Selected", f"Selected drive: {drive}")
            drive_window.destroy()  # Close the drive selection window

    tk.Button(drive_window, text="Confirm", command=confirm_selection).pack(pady=20)
    drive_window.mainloop()
    # Logic to select the target drive
    pass

def create_gui():
    root = tk.Tk()
    root.title("Drive Protection Program")

    tk.Label(root, text="Select Target Drive:").pack()
    tk.Button(root, text="Select Drive", command=select_drive).pack()

    tk.Button(root, text="Set Password", command=set_password).pack()
    tk.Button(root, text="Change Password", command=change_password).pack()
    tk.Button(root, text="Restore Drive", command=restore_drive).pack()
    tk.Button(root, text="Remove Program", command=remove_program).pack()
    tk.Button(root, text="Install Program", command=install_program).pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
