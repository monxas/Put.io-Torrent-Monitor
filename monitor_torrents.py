import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import putiopy
import os

# Put.io API credentials
CLIENT_ID = "15"
CLIENT_SECRET = "nr5taj15dg0f80x7sw8h"
OAUTH_TOKEN = "4GXATZHKOFMUF5AAN3SN"

# Create a Put.io client
client = putiopy.Client(OAUTH_TOKEN)

# Define the folders to monitor inside the Docker container
folders_to_monitor = {
    "/data/torrents/sonarr": 718436026,  # Map sonarr folder to sonarr_parent_id
    "/data/torrents/radarr": 1244692884  # Map radarr folder to radarr_parent_id
}

# Define a handler class to respond to file system events
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super(MyHandler, self).__init__()
        self.parent_ids = {}  # Store parent IDs for each monitored folder

    def on_created(self, event):
        if event.is_directory:
            return  # Skip directories
        file_path = event.src_path
        print(f"New file created: {file_path}")

        # Determine the parent ID based on the folder where the file was created
        parent_id = self.get_parent_id_for_folder(os.path.dirname(file_path))
        print(f"Using parent_id: {parent_id}")

        # Upload the newly created file to Put.io with the specified parent ID
        upload_file = client.File.upload(file_path, parent_id=parent_id)

        # Check if the upload was successful
        if upload_file:
            upload_file_str = upload_file.decode('utf-8')  # Decode bytes to string
            print(f"File uploaded successfully to Put.io. File ID: {upload_file_str}")
        else:
            print("Failed to upload file to Put.io.")

    def get_parent_id_for_folder(self, folder_path):
        # Get the parent ID for the specified folder
        return self.parent_ids.get(folder_path, 0)  # Default to 0 if not found

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()

    for folder, parent_id in folders_to_monitor.items():
        observer.schedule(event_handler, path=folder, recursive=False)
        event_handler.parent_ids[folder] = parent_id  # Store parent ID for the folder
        print(f"Monitoring folder: {folder} with Parent ID: {parent_id}")

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
