import os
import shutil
import sys
import pickle
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

data = "C:/ProgramData/BMU_DATA/HF_MWP_BMU/data"
data_core = "C:/ProgramData/BMU_DATA/HF_MWP_BMU"

def stopping():
    messagebox.showinfo("Stopping", "Stopping in 10 seconds")
    time.sleep(10)
    sys.exit()
    

def check_setup():
    try:
        if os.path.exists(f"C:/ProgramData/HF_MWP_BMU/data/"):
            messagebox.showinfo("Update", "Updating version for '3.0' to '4.0'")
            HMB_dr = "C:/ProgramData/HF_MWP_BMU/data/"
            shutil.move(HMB_dr, data_core)
            os.remove("C:/ProgramData/HF_MWP_BMU")
            messagebox.showinfo("Update", "Done updating")
        elif not os.path.exists(data):
            ask_2_to_4_up = simpledialog.askinteger("Setup", "Type 1 if you were using 2.0/1.0 or type 0 if you are new to using this:")
            if ask_2_to_4_up == 1:
                old_data = simpledialog.askstring("Setup", "Open the older version folder and copy its path:")
                if os.path.exists(f"{old_data}/data"):
                    old_data_full = os.path.join(old_data, "data")
                    messagebox.showinfo("Update", "Found data folder, updating...")
                    shutil.move(old_data_full, data)
                    with open(f"{data}/ver.txt", "w") as ver_file:
                        ver_file.write("4.0")
                else:
                    messagebox.showerror("Error", "No location found")
                    stopping()
            elif ask_2_to_4_up == 0:
                messagebox.showinfo("Setup", "Making data folder")
                os.makedirs(f"{data}/a")
                os.makedirs(f"{data}/d/d/m_tester")
                os.makedirs(f"{data}/a/u")
                os.makedirs(f"{data}/a/p")
                with open(f"{data}/a/u/m.txt", "w") as m:
                    m.write("m")
                with open(f"{data}/a/p/m_p.txt", "w") as m_p:
                    m_p.write("tester")
                pinset = simpledialog.askstring("Setup", "Please make a pin:")
                with open(f"{data}/pin.txt", "w") as pin:
                    pin.write(pinset)
            else:
                messagebox.showerror("Error", "Please type a valid input and restart code")
                stopping()
            messagebox.showinfo("Setup", "Done")
        else:
            messagebox.showinfo("Setup", "Starting(do not close the termial it will also clode the app)")
    except Exception as e:
        messagebox.showerror("Error", f"Check setup error: {e}")

def reset():
    try:
        messagebox.showinfo("Reset", "Resetting data")
        resetpath = data_core
        shutil.rmtree(resetpath)
    except Exception as e:
        messagebox.showerror("Error", f"Reset error: {e}")

# Tkinter GUI
root = tk.Tk()
root.title("Hidden Folder MWPBMU 4.0V")
root.iconbitmap(f"{data_core}/logo.ico")


def add_list(key, value):
    dataA[key] = value
    messagebox.showinfo("Success", f"Added {key}: {value}")

def remove_list(key):
    if key in dataA:
        del dataA[key]
        messagebox.showinfo("Success", f"Removed {key}")
    else:
        messagebox.showwarning("Warning", f"{key} not found in the dictionary.")

def change_list(key, new_value):
    if key in dataA:
        dataA[key] = new_value
        messagebox.showinfo("Success", f"Changed {key} to {new_value}")
    else:
        messagebox.showwarning("Warning", f"{key} not found in the dictionary.")

def read_list(key):
    if key in dataA:
        messagebox.showinfo("Read", f"{key}: {dataA[key]}")
    else:
        messagebox.showwarning("Warning", f"{key} not found in the list data.")

def save_data(filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(dataA, file)
        messagebox.showinfo("Success", "Data saved")
    except Exception as e:
        messagebox.showerror("Error", f"Save data error: {e}")

def load_data(filename):
    try:
        with open(filename, "rb") as file:
            loaded_data = pickle.load(file)
            dataA.update(loaded_data)
            messagebox.showinfo("Success", f"Data loaded from {filename}")
    except EnvironmentError as error_save:
        messagebox.showerror("Error", f"Load data error: {error_save}")

dataA = {}

# Create menu functions
def sign_in():
    try:
        username = simpledialog.askstring("Sign In", "Username:")
        password = simpledialog.askstring("Sign In", "Password:", show='*')
        file_name = f"{data}/a/u/{username}.txt"
        login_folder_loc = f"{data}/d/d/{username}_{password}"
        if os.path.isfile(file_name):
            try:
                os.startfile(login_folder_loc)
                messagebox.showinfo("Welcome", f"Welcome {username}, a folder has been opened.")
            except Exception as e:
                messagebox.showerror("Error", f"Incorrect password: {e}")
        else:
            messagebox.showerror("Error", f"Incorrect username: {username} or password: {password}")
    except Exception as e:
        messagebox.showerror("Error", f"Sign-in error: {e}")

def sign_up():
    try:
        username = simpledialog.askstring("Sign Up", "Please make a username:")
        password = simpledialog.askstring("Sign Up", "Password (do not forget it):", show='*')
        file_name = f"{data}/a/u/{username}.txt"
        file_name_P = f"{data}/a/p/{username}_p.txt"
        if username == "m":
            messagebox.showwarning("Warning", f"Sorry, but {username} is a testing account.")
        elif os.path.isfile(file_name):
            messagebox.showwarning("Warning", f"The username '{username}' already exists. Please choose a different username.")
        elif username == "super":
            messagebox.showwarning("Warning", f"Sorry, but '{username}' is an admin account.")
        else:
            with open(file_name, 'w') as user_file_lock:
                user_file_lock.write(username)
            with open(file_name_P, 'w') as user_file_lock_p:
                user_file_lock_p.write(password)
            login_folder_loc = f"{data}/d/d/{username}_{password}"
            os.makedirs(login_folder_loc, exist_ok=True)
            messagebox.showinfo("Success", "Account created successfully. Opening folder.")
            os.startfile(login_folder_loc)
    except Exception as e:
        messagebox.showerror("Error", f"Sign-up error: {e}")

def delete_account():
    try:
        username = simpledialog.askstring("Delete Account", "Username:")
        password = simpledialog.askstring("Delete Account", "Password:", show='*')
        file_name = f"{data}/a/u/{username}.txt"
        file_pass = f"{data}/a/p/{username}_p.txt"
        if os.path.isfile(file_name) and open(file_pass).read() == password:
            try:
                os.remove(file_pass)
                os.remove(file_name)
                messagebox.showinfo("Success", "Account deleted successfully.")
                delful = simpledialog.askstring("Delete Account", "Do you want to delete your folder too? (yes or no):")
                if delful == "yes":
                    f_loc = f"{data}/d/d/{username}_{password}"
                    shutil.rmtree(f_loc)
            except Exception as e:
                messagebox.showerror("Error", f"Delete account error: {e}")
        else:
            messagebox.showerror("Error", f"Incorrect username: {username} or password: {password}")
    except Exception as e:
        messagebox.showerror("Error", f"Delete account error: {e}")

def find_password():
    try:
        pinE = simpledialog.askstring("Find Password", "PIN:")
        pin_loc = f"{data}/pin.txt"
        with open(pin_loc, "r") as pintxt:
            pin = pintxt.read()
        if pinE == pin:
            user = simpledialog.askstring('Find Password', 'Username:')
            loc = f"{data}/a/p/{user}_p.txt"
            if os.path.isfile(loc):
                with open(loc, "r") as file:
                    File_data = file.read()
                messagebox.showinfo("Find Password", f"Your password is [{File_data}]")
            else:
                messagebox.showwarning("Error", "Incorrect PIN or error")
        else:
            messagebox.showwarning("Error", "Incorrect PIN, restart code")
    except Exception as e:
        messagebox.showerror("Error", f"Find password error: {e}")

def settings():
    try:
        sepina = simpledialog.askstring("Settings", "PIN:")
        with open(f"{data}/pin.txt") as sepinaa:
            sepinaan = sepinaa.read()
        if sepina == sepinaan:
            while True:
                dsow = simpledialog.askinteger("Settings", "1: Import (will reset old data)\n2: Export\n3: Combine data (add new data in old data)\n4: Reset (fully)\n5: Go back\nChoose an option:")
                if dsow == 1:
                    reset()
                    EX_loc = simpledialog.askstring("Import", "Copy the file path here (e.g., HF_DATA_EXPORT or C:/HF_DATA_EXPORT):")
                    if os.path.isdir(EX_loc):
                        if os.path.exists(EX_loc + "/HF_EX_MARK.txt"):
                            shutil.move(EX_loc + "/Data", data_core)
                            stopping()
                        else:
                            messagebox.showerror("Error", "Invalid file path")
                            stopping()
                    else:
                        messagebox.showerror("Error", "No folder found")
                        stopping()
                elif dsow == 2:
                    os.makedirs("HF_DATA_EXPORT")
                    with open("HF_DATA_EXPORT/HF_EX_MARK.txt", "w") as HF_EXM:
                        HF_EXM.write("This tells the program this is a valid export. Do not remove to move or copy")
                    shutil.move(data, "HF_DATA_EXPORT")
                    dsowTr = simpledialog.askstring("Export", "Do you want to reset (Y for yes or leave blank for no):")
                    if dsowTr == "Y" or dsowTr == "y":
                        reset()
                        messagebox.showinfo("Reset", "Stopping, restart to setup")
                    else:
                        messagebox.showinfo("Info", "Stopping")
                    stopping()
                elif dsow == 3:
                    EX_loc = simpledialog.askstring("Combine Data", "Copy the file path here (e.g., HF_DATA_EXPORT or C:/HF_DATA_EXPORT):")
                    if os.path.isdir(EX_loc):
                        if os.path.exists(EX_loc + "/HF_EX_MARK.txt"):
                            shutil.move(EX_loc + "/Data", data_core)
                            messagebox.showinfo("Info", "Data combined successfully. Stopping, restart to setup")
                            stopping()
                        else:
                            messagebox.showerror("Error", "No EX_MARK file found")
                            stopping()
                    else:
                        messagebox.showerror("Error", "No folder found")
                        stopping()
                elif dsow == 4:
                    reset()
                    messagebox.showinfo("Reset", "Data reset successfully. Stopping.")
                    stopping()
                elif dsow == 5:
                    messagebox.showinfo("Info", "Going back")
                    break
                else:
                    messagebox.showwarning("Warning", "Invalid input. Going back")
        else:
            messagebox.showwarning("Warning", "Incorrect PIN or error")
    except Exception as e:
        messagebox.showerror("Error", f"Settings error: {e}")

# GUI buttons
check_setup()
tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)
tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)
tk.Button(root, text="Delete Account", command=delete_account).pack(pady=5)
tk.Button(root, text="Find Password", command=find_password).pack(pady=5)
tk.Button(root, text="Settings", command=settings).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()
