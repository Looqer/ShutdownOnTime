import tkinter as tk
from tkinter import simpledialog, Label, Tk
from threading import Thread
from datetime import datetime, timedelta
import time


# Creating a function to display information
def display_information():
    top = tk.Toplevel(root)
    top.title("Information Window")
    label = tk.Label(top, text="Now the computer is shutting down")
    label.pack(padx=20, pady=20)

def execute_shutdown(shutdown_time_str):
    shutdown_time = datetime.strptime(shutdown_time_str, "%H:%M").time()
    while datetime.now().time() < shutdown_time:
        time.sleep(1)
    display_information()

def time_hhmm_to_seconds(time_hhmm):
    # Parsing time in HH:MM format
    time_dt = datetime.strptime(time_hhmm, "%H:%M")
    # Calculating the number of seconds since midnight
    seconds = time_dt.hour * 3600 + time_dt.minute * 60

    return seconds

def update_time():
    current_time_update = datetime.now().strftime("%H:%M:%S")
    label_time.config(text=f"Current time: {current_time_update}")
    root.after(1000, update_time)


def update_remaining_time():
    current_time_remain = datetime.now()
    remaining_time = (shutdown_time - current_time_remain).total_seconds()

    if remaining_time <= 0:
        label_remaining_time.config(text="Time has elapsed!")
        display_information()
    else:
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        label_remaining_time.config(text=f"Time remaining: {formatted_time}")
        root.after(1000, update_remaining_time)

# Get shutdown time from user
def get_shutdown_time():
    shutdown_time = simpledialog.askstring("Enter time", "Enter the shutdown time (HH:MM):")
    return shutdown_time

# Get countdown time from user
def get_countdown_time():
    countdown_time = simpledialog.askstring("Enter countdown time", "Enter the time after which the computer will shut down (HH:MM):")
    return countdown_time

# Start a thread for shutting down at a specific hour
def start_shutdown_hour_thread():
    global shutdown_time, start_time
    shutdown_time_str = get_shutdown_time()
    shutdown_time = datetime.strptime(shutdown_time_str, "%H:%M")
    start_time = datetime.now()
    thread = Thread(target=execute_shutdown, args=(shutdown_time_str,))
    thread.start()

# Start a thread for shutting down after a countdown
def start_shutdown_countdown_thread():
    global shutdown_time, start_time
    countdown_time = get_countdown_time()
    shutdown_time = datetime.now() + timedelta(seconds=time_hhmm_to_seconds(countdown_time))
    start_time = datetime.now()
    root.after(1000, update_remaining_time)

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Computer Shutdown Application")

# Add an entry for entering the hour (commented out)
# entry_label = tk.Label(root, text="Shutdown time:")
# entry_label.pack()
# entry_time = tk.Entry(root)
# entry_time.pack()

# Create a frame to group buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Add a button to initiate the process
start_button = tk.Button(button_frame, text="Specific time", command=start_shutdown_hour_thread)
start_button.pack(side="left", padx=10, pady=10)
start_button.pack()

# Add a button for closing the window
exit_button = tk.Button(button_frame, text="Countdown", command=start_shutdown_countdown_thread)
exit_button.pack(side="left", padx=10, pady=10)
exit_button.pack()

# Add a label for displaying the current time
label_time = tk.Label(root, text="", font=("Helvetica", 14))
label_time.pack(pady=10)
root.after(1000, update_time)

# Add a label for displaying the remaining time
label_remaining_time = tk.Label(root, text="", font=("Helvetica", 14))
label_remaining_time.pack(pady=10)

# Run the main loop
if __name__ == "__main__":
    root.mainloop()
