import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import putiopy

def is_file_done_downloading(file_path, timeout=30):
    prev_size = 0
    start_time = time.time()
    
    while True:
        current_size = os.path.getsize(file_path)
        
        if current_size == prev_size:
            return True

        prev_size = current_size

        if time.time() - start_time > timeout:
            print("File download check timed out.")
            return False
        
        time.sleep(3)

# Put.io API credentials
PUTIO_OAUTH_TOKEN = os.environ.get('PUTIO_OAUTH_TOKEN')

# Create a Put.io client
client = putiopy.Client(PUTIO_OAUTH_TOKEN)

# Folder to monitor
folder_to_monitor = '/torrents'
parent_id = os.environ.get('PARENT_ID')

# Create the folder if it doesn't exist
if not os.path.exists(folder_to_monitor):
    os.makedirs(folder_to_monitor)

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        if is_file_done_downloading(file_path):
            upload_file = client.File.upload(file_path, parent_id=parent_id)
            if upload_file:
                print(f"File uploaded successfully to Put.io. File ID: {upload_file.id}")

if __name__ == "__main__":
    print(f"Starting to monitor {folder_to_monitor} ...") 
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_monitor, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
