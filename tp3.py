import tkinter as tk
from tkinter import messagebox
import subprocess

# Update these lists with your VM names
SERVER_VMS = ["WINGATE SERVER", "serveur apache"]
CLIENT_VMS = ["CLIENT 1", "CLIENT 2", "CLIENT 3"]  # Ensure this matches the actual client names

def start_vms():
    try:
        # Get the number of clients to start
        num_clients = int(client_input.get())
        
        if num_clients <= 0 or num_clients > len(CLIENT_VMS):
            raise ValueError("Please enter a valid number of clients.")

        # Start server VMs
        for server in SERVER_VMS:
            print(f"Starting server: {server}")
            subprocess.run(["VBoxManage", "startvm", server, "--type", "headless"], check=True)

        # Start the specified number of clients
        for i in range(num_clients):
            print(f"Starting client: {CLIENT_VMS[i]}")
            subprocess.run(["VBoxManage", "startvm", CLIENT_VMS[i], "--type", "headless"], check=True)

        messagebox.showinfo("Success", f"Started {num_clients} client(s) and {len(SERVER_VMS)} server(s).")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"{e}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to start a VM. Details: {e}")

# Initialize the main application window
root = tk.Tk()
root.title("VM Controller")

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(pady=20, padx=20)

# Input for number of clients
tk.Label(main_frame, text="Number of Client VMs:").pack()
client_input = tk.Entry(main_frame)
client_input.pack(pady=5)

# Start button
start_btn = tk.Button(main_frame, text="Start", command=start_vms)
start_btn.pack(pady=10)

# Run the application
root.mainloop()
