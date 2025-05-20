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

download_folder = "/Users/kinomalonzo/Downloads"
destination = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar", ".tar", ".tgz", ".jar", ".dmg"],
    "JSON": [".json"],
    "YAML": [".yaml", ".yml"],
    "HTML": [".html"],
    "Audio": [".wav"],
    "Presentation": [".pptx", ".ppt"],
    "Scripts": [".py", ".js"],
    "Markdown": [".md"],
    "CSV": [".csv"],
    "Spreadsheet": [".xlsx", ".xls"],
    "Log File": [".log"],
}

def organize_downloads():
    moved_count = 0
    error_count = 0

    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)
        if os.path.isfile(file_path):
            for folder, extensions in destination.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(download_folder, folder)
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
                        logging.info("Moved: %s -> %s/%s", file, folder, os.path.basename(dest_path))
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