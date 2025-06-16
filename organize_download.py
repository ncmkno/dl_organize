"""
Download Folder Organizer

This module automatically organizes files in the Downloads folder by moving them
into categorized subfolders based on their file extensions. It supports various
file types including images, videos, documents, code files, and more.

The script creates organized folders within the Downloads directory and moves
files accordingly, handling duplicates by appending numbers to filenames.
All operations are logged for tracking purposes.
"""

import os
import shutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(f'file_organizer_{datetime.now().strftime("%Y%m%d")}.log'),
        logging.StreamHandler()
    ]
)

DOWNLOAD_FOLDER = "/Users/kinomalonzo/Downloads"
DESTINATION = {
    "Images": [".png", ".jpg", ".jpeg", ".gif",".icon", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Compressed": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".php"],
    "PDFs": [".pdf"],
    "Spreadsheets": [".xlsx", ".xls", ".ods"],
    "Audio Files": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Executable": [".exe", ".msi", ".apk", ".dmg"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Scripts": [".sh", ".bat", ".ps1", ".py", ".js"],
    "Database": [".sql", ".db", ".sqlite"],
    "Configuration": [".ini", ".cfg", ".conf"],
    "Backup": [".bak", ".tmp"],
    "Ebooks": [".epub", ".mobi", ".azw3"],
    "Torrent": [".torrent"],
    "Virtual Machines": [".vmdk", ".vdi", ".ova", ".ovf"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar", ".tar", ".tgz", ".jar", ".dmg"],
    "JSON": [".json"],
    "YAML": [".yaml", ".yml"],
    "HTML": [".html"],
    "Audio": [".wav"],
    "Presentation": [".pptx", ".ppt"],
    "Markdown": [".md"],
    "CSV": [".csv"],
    "Spreadsheet": [".xlsx", ".xls"],
    "Log File": [".log"],
}

def organize_downloads():
    """
    Organize files in the Downloads folder by moving them into categorized subfolders.
    
    Returns:
        tuple: A tuple containing (moved_count, error_count) representing the number
               of files successfully moved and the number of errors encountered.
    """
    moved_count = 0
    error_count = 0

    for file in os.listdir(DOWNLOAD_FOLDER):
        file_path = os.path.join(DOWNLOAD_FOLDER, file)
        if os.path.isfile(file_path):
            for folder, extensions in DESTINATION.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(DOWNLOAD_FOLDER, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    dest_path = os.path.join(folder_path, file)

                    # Handle duplicate files
                    if os.path.exists(dest_path):
                        base, extension = os.path.splitext(file)
                        counter = 1
                        while os.path.exists(dest_path):
                            new_name = f"{base}_{counter}{extension}"
                            dest_path = os.path.join(folder_path, new_name)
                            counter += 1

                    try:
                        shutil.move(file_path, dest_path)
                        logging.info("Moved: %s -> %s/%s", file, folder,
                                   os.path.basename(dest_path))
                        moved_count += 1
                    except PermissionError:
                        logging.error("Permission denied: Could not move %s", file)
                        error_count += 1
                    except (shutil.Error, OSError) as e:
                        logging.error("Error moving %s: %s", file, str(e))
                        error_count += 1
                    break

    return moved_count, error_count

if __name__ == "__main__":
    logging.info("Starting download folder organization...")
    moved_files, errors = organize_downloads()
    logging.info("Organization complete! Files moved: %d, Errors: %d", moved_files, errors)
