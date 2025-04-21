import os
import gdown
import re
from pathlib import Path

def extract_file_id(url):
    """Extract the file ID from a Google Drive URL."""
    # Match patterns like /d/FILE_ID/ or id=FILE_ID
    match = re.search(r'/d/([^/]+)', url) or re.search(r'id=([^&]+)', url)
    if match:
        return match.group(1)
    return url  # Return the original if it's already an ID

def get_filename_from_drive(file_id):
    """Try to get the original filename from Google Drive metadata."""
    try:
        import requests
        from urllib.parse import unquote
        
        response = requests.get(f"https://drive.google.com/uc?id={file_id}&export=download", 
                               stream=True, allow_redirects=False)
        
        if 'content-disposition' in response.headers:
            content_disposition = response.headers['content-disposition']
            filename_match = re.search(r'filename="(.+)"', content_disposition)
            if filename_match:
                return unquote(filename_match.group(1))
    except:
        pass
    
    # Default filename if we can't get the original
    return f"{file_id}.pdf"

def download_pdf_from_drive(url, output_path):
    """Download a PDF from Google Drive."""
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Extract file ID from the URL
    file_id = extract_file_id(url)
    
    # Try to get original filename, otherwise use file_id
    filename = get_filename_from_drive(file_id)
    
    # Construct output filename
    output_file = os.path.join(output_path, filename)
    
    try:
        # Download the file
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, quiet=False)
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")
        return False

def read_links_from_file(filepath):
    """Read Google Drive links from a text file."""
    links = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # Strip whitespace and skip empty lines
                link = line.strip()
                if link:
                    links.append(link)
        return links
    except Exception as e:
        print(f"Error reading links file: {str(e)}")
        return []

def batch_download_pdfs(urls, output_path):
    """Download multiple PDFs from a list of Google Drive URLs."""
    success_count = 0
    total = len(urls)
    
    print(f"Starting download of {total} PDF files...")
    
    for i, url in enumerate(urls, 1):
        print(f"Downloading file {i}/{total}...")
        if download_pdf_from_drive(url, output_path):
            success_count += 1
    
    print(f"Download complete: {success_count}/{total} files downloaded successfully")

if __name__ == "__main__":
    # Path to the links text file (in the same directory)
    links_file = os.path.join(os.path.dirname(__file__), "links.txt")
    
    # Specific download directory path
    download_dir = r"C:\Users\Shadman Rafy\Downloads\425"
    
    # Read links from the file
    drive_links = read_links_from_file(links_file)
    
    if drive_links:
        # Download all PDFs to the specified directory
        batch_download_pdfs(drive_links, download_dir)
    else:
        print("No links found in the file. Make sure 'links.txt' exists and contains valid URLs.")