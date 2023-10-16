### README.md

---

# Put.io Torrent Monitor

A simple torrent monitoring tool that watches for new torrents in a specified folder (blackhole) and automatically uploads them to Put.io.

## Requirements

- Docker
- Docker Compose
- Put.io account

## Quick Start

### Build and Run with Docker

1. Build the image:
   ```bash
   docker build -t putio-torrent-monitor .
   ```
   
2. Run the container:
   ```bash
   docker run -it -v /path/to/your_blackhole_folder:/data/torrents -e PUTIO_OAUTH_TOKEN='your_token' -e PARENT_ID='your_parent_id' putio-torrent-monitor
   ```

### Run with Docker Compose

You can also use Docker Compose for an easier setup:

1. Create a `docker-compose.yml` file:
   ```yaml
   version: '3'
   services:
     torrent-monitor:
       image: monxas/putio-torrent-monitor:latest
       volumes:
         - /path/to/your_blackhole_folder:/data/torrents
       environment:
         - PARENT_ID=your_folder_parent_id_here
         - PUTIO_OAUTH_TOKEN=your_token_here


2. Run the service:
   ```bash
   docker-compose up
   ```

## Environment Variables

- `PUTIO_OAUTH_TOKEN`: Your Put.io OAuth token.
- `/path/to/your_blackhole_folder`: The folder you want to monitor for new torrent files.
- `PARENT_ID`: The parent folder ID in Put.io where the new files will be uploaded.

## How it Works

This tool uses the watchdog library to monitor the specified folder for new files. When a new file is detected, it's automatically uploaded to your Put.io account using the specified parent ID.

---

