import tkinter as tk
from tkinter import simpledialog
import time
from threading import Thread

# Tworzenie funkcji do wyświetlania informacji
def wyswietl_informacje():
    top = tk.Toplevel(root)
    top.title("Okno z informacją")
    label = tk.Label(top, text="Teraz komputer wyłącza się")
    label.pack(padx=20, pady=20)

def execute_shutdown(shutdown_time):
    current_time = time.strftime("%H:%M")
    while current_time < shutdown_time:
        time.sleep(1)
        current_time = time.strftime("%H:%M")

    wyswietl_informacje()


def czas_hhmm_do_sekund(czas_hhmm):
    
    # Parsowanie czasu w formacie HH:MM
    czas_dt = datetime.strptime(czas_hhmm, "%H:%M")
    # Obliczenie ilości sekund od północy
    sekundy = czas_dt.hour * 3600 + czas_dt.minute * 60

    return sekundy

# Wyłączanie komputera
 #import subprocess
 #subprocess.run(["shutdown", "/s", "/t", "1"])
# Utwórz okno udające wyłączenie komputera

def get_shutdown_time():
    shutdown_time = simpledialog.askstring("Podaj godzinę", "Podaj godzinę wyłączenia (HH:MM):")
    return shutdown_time

def get_countdown_time():
    countdown_time = simpledialog.askstring("Podaj czas odliczania", "Podaj za jaki czas, komputer się wyłączy (HH:MM):")
    return countdown_time

def start_shutdown_hour_thread():
    shutdown_time = get_shutdown_time()
    if shutdown_time:
        thread = Thread(target=execute_shutdown, args=(shutdown_time,))
        thread.start()

def start_shutdown_countdown_thread():
    countdown_time = get_countdown_time()
    time_in_secs = czas_hhmm_do_sekund(countdown_time)
    time.sleep(time_in_secs)


# Utwórz główne okno
root = tk.Tk()
root.geometry("400x200")
root.title("Aplikacja do wyłączania komputera")

# Dodaj pole do wprowadzania godziny
#entry_label = tk.Label(root, text="Godzina wyłączenia:")
#entry_label.pack()
#entry_time = tk.Entry(root)
#entry_time.pack()

# Dodaj przycisk do uruchamiania procesu
start_button = tk.Button(root, text="Dokładna godzina", command=start_shutdown_hour_thread)
start_button.pack(side="left", padx=50, pady=50)
start_button.pack()

# Dodaj przycisk do zamykania okna
exit_button = tk.Button(root, text="Odliczanie", command=start_shutdown_countdown_thread)
exit_button.pack(side="right", padx=50, pady=50)
exit_button.pack()

# Uruchom pętlę główną
root.mainloop()
