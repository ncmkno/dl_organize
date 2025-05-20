# Downloads Organizer 📂

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/dl-organize/graphs/commit-activity)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A robust and efficient Python script that automatically organizes your Downloads folder by categorizing files into appropriate directories based on their extensions.

## 🌟 Features

- Automatically sorts files by type into designated folders
- Handles duplicate files intelligently
- Comprehensive logging system
- Supports multiple file formats:
  - 🖼️ Images (png, jpg, jpeg, gif)
  - 📄 Documents (pdf, docx, txt)
  - 📦 Archives (zip, rar, tar, tgz, jar, dmg)
  - 📊 Data Files (json, yaml, yml, csv)
  - 📝 Text & Code (py, js, md, html)
  - 🎵 Audio (wav)
  - 📊 Spreadsheets (xlsx, xls)
  - 📑 Presentations (pptx, ppt)
  - 📋 Log Files (log)

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ncmkno/dl-organize.git
   cd dl-organize
   ```

2. No additional dependencies required! The script uses Python standard library modules only.

## ⚙️ Configuration

By default, the script is configured to organize files from your Downloads folder. You can modify the following variables in `organize_download.py`:

```python
download_folder = "/Users/yourusername/Downloads"  # Change this to your downloads path
```

## 🚀 Usage

Run the script from the command line:

```bash
python organize_download.py
```

### Sample Output:
```
2025-05-20 10:30:15,123 - Starting download folder organization...
2025-05-20 10:30:15,234 - Moved: document.pdf -> Documents/document.pdf
2025-05-20 10:30:15,345 - Moved: image.png -> Images/image.png
2025-05-20 10:30:15,456 - Organization complete! Files moved: 2, Errors: 0
```

## 📁 Directory Structure

After running the script, your Downloads folder will be organized as follows:

```
Downloads/
├── Images/
├── Documents/
├── Archives/
├── JSON/
├── YAML/
├── HTML/
├── Audio/
├── Presentation/
├── Scripts/
├── Markdown/
├── CSV/
├── Spreadsheet/
└── Log File/
```

## 🔍 Features in Detail

### Duplicate File Handling
The script automatically handles duplicate files by appending a counter to the filename:
- `document.pdf` → `document_1.pdf` → `document_2.pdf`

### Logging
- Creates a daily log file (`file_organizer_YYYYMMDD.log`)
- Logs both to file and console
- Records successful moves and any errors encountered

## ⚠️ Error Handling

The script handles various error scenarios:
- Permission errors
- File access issues
- Duplicate files
- Missing directories (creates them automatically)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] Add support for more file types
- [ ] Implement file organization by date
- [ ] Add a GUI interface
- [ ] Add undo functionality
- [ ] Add custom folder mapping configuration
- [ ] Implement file organization by content type detection

## 📫 Contact

If you have any questions or suggestions, please open an issue in the repository.

## 🙏 Acknowledgments

- Python standard library for making file operations simple
- All contributors and users of this tool

---
Made with ❤️ by Kino
