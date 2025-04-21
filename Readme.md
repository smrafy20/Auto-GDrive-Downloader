Google Drive Batch Downloader

This Python script allows you to batch download files from Google Drive links stored in a text file, automatically preserving original filenames when possible.

Features:
Downloads multiple files from Google Drive links at once
Extracts original filenames from Google Drive metadata
Reads links from a text file (one link per line)
Supports various Google Drive URL formats
Shows progress during download

Installation Prerequisites:
Python 3.6 or higher
pip (Python package installer)

Step 1: Clone or download this repository
Save the main.py file to your local machine.

Step 2: Install dependencies
Open a command prompt or terminal and run:
```bash
pip install gdown requests
```

How It Works:
The script reads Google Drive links from links.txt
For each link, it extracts the file ID
It attempts to get the original filename from Google Drive
It downloads the file to the specified directory
It reports success or failure for each file

License:This project is open-source and free to use for personal or commercial purposes.

Acknowledgements:

gdown: For downloading files from Google Drive
requests: For fetching file metadata