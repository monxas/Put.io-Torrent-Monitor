import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import putiopy
import os

# Put.io API credentials
PUTIO_OAUTH_TOKEN = os.environ.get('PUTIO_OAUTH_TOKEN')

# Create a Put.io client
client = putiopy.Client(PUTIO_OAUTH_TOKEN)

# Folder to monitor (passed as an argument)
folder_to_monitor = '/torrents'
parent_id = os.environ.get('PARENT_ID')

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        upload_file = client.File.upload(file_path, parent_id=parent_id)
        if upload_file:
            print(f"File uploaded successfully to Put.io. File ID: {upload_file.id}")

if __name__ == "__main__":
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
