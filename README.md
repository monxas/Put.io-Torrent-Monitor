
## README.md

# Put.io Torrent File Monitor

Monitor your specified local folders for newly created torrent files and automatically upload them to your Put.io account.

## Features
- Monitors multiple folders
- Automatic file upload to Put.io
- OAuth2 authenticated

## Requirements
- Python 3.9+
- Docker (optional)

## Dependencies
- Watchdog
- putio.py

## Environment Variables
- `CLIENT_ID`
- `CLIENT_SECRET`
- `OAUTH_TOKEN`

## Quick Start

### Clone the Repo
```bash
git clone https://github.com/yourusername/putio-torrent-monitor.git
```

### Run with Docker

1. Build the image
   ```bash
   docker build -t putio-torrent-monitor .
   ```
2. Run the container
   ```bash
   docker run putio-torrent-monitor
   ```

### Run Locally

1. Install dependencies
   ```bash
   pip install watchdog putio.py
   ```
2. Run the script
   ```bash
   python monitor_torrents.py
   ```

## How It Works

1. Watches folders specified in `folders_to_monitor` dictionary.
2. When a new file is created, the script triggers.
3. Checks the parent folder to determine the Put.io folder where the file should be uploaded.
4. Uploads the file to Put.io.

## Customization

Edit the `folders_to_monitor` dictionary to specify which folders to monitor and what their corresponding Put.io parent folder IDs are.

```python
folders_to_monitor = {
    "/data/torrents/sonarr": 1244743180,
    "/data/torrents/radarr": 1244692884
}
```

## License

MIT

---

docker run -v /root/putio_folders/sonarr:/data/torrents/sonarr -v /root/putio_folders/radarr:/data/torrents/radarr torrent-monitor python -u monitor_torrents.py
