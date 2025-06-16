# Downloads Organizer 📂

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/dl-organize/graphs/commit-activity)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A robust and efficient Python script that automatically organizes your Downloads folder by categorizing files into appropriate directories based on their extensions. The script uses uppercase constants for configuration (`DOWNLOAD_FOLDER`, `DESTINATION`) and follows Python best practices with comprehensive docstrings and error handling.

## 🌟 Features

- **Automatic file organization** by type into designated folders
- **Smart duplicate file handling** with automatic renaming
- **Comprehensive logging system** with daily log files
- **Robust error handling** for permissions and file system issues
- **Pylint compliant code** following Python best practices
- **Extensive file type support** covering 25+ categories
- Supports multiple file formats:
  - 🖼️ Images (png, jpg, jpeg, gif, icon, svg, webp)
  - 🎬 Videos (mp4, mkv, avi, mov, flv, wmv)
  - 📦 Compressed Files (zip, rar, tar, gz, 7z)
  - 💻 Code Files (py, js, java, c, cpp, cs, html, css, php)
  - 📄 PDFs (pdf)
  - 📊 Spreadsheets (xlsx, xls, ods)
  - 🎵 Audio Files (mp3, wav, flac, aac, ogg)
  - ⚙️ Executable Files (exe, msi, apk, dmg)
  - 🔤 Fonts (ttf, otf, woff, woff2)
  - 📜 Scripts (sh, bat, ps1, py, js)
  - 🗄️ Database Files (sql, db, sqlite)
  - ⚙️ Configuration Files (ini, cfg, conf)
  - 💾 Backup Files (bak, tmp)
  - 📚 Ebooks (epub, mobi, azw3)
  - 🌐 Torrent Files (torrent)
  - 💻 Virtual Machines (vmdk, vdi, ova, ovf)
  - 📄 Documents (pdf, docx, txt)
  - 📦 Archives (zip, rar, tar, tgz, jar, dmg)
  - 📊 JSON Files (json)
  - 📝 YAML Files (yaml, yml)
  - 🌐 HTML Files (html)
  - 🎵 Audio (wav)
  - 📑 Presentations (pptx, ppt)
  - 📝 Markdown (md)
  - 📊 CSV Files (csv)
  - 📊 Spreadsheet Files (xlsx, xls)
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
DOWNLOAD_FOLDER = "/Users/yourusername/Downloads"  # Change this to your downloads path
```

## 🚀 Usage

Run the script from the command line:

```bash
python organize_download.py
```

### Sample Output:
```
2024-06-16 10:30:15,123 - Starting download folder organization...
2024-06-16 10:30:15,234 - Moved: document.pdf -> PDFs/document.pdf
2024-06-16 10:30:15,345 - Moved: image.png -> Images/image.png
2024-06-16 10:30:15,456 - Organization complete! Files moved: 2, Errors: 0
```

## 📁 Directory Structure

After running the script, your Downloads folder will be organized as follows:

```
Downloads/
├── Images/
├── Videos/
├── Compressed/
├── Code/
├── PDFs/
├── Spreadsheets/
├── Audio Files/
├── Executable/
├── Fonts/
├── Scripts/
├── Database/
├── Configuration/
├── Backup/
├── Ebooks/
├── Torrent/
├── Virtual Machines/
├── Documents/
├── Archives/
├── JSON/
├── YAML/
├── HTML/
├── Audio/
├── Presentation/
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

## 🏗️ Code Quality

This project maintains high code quality standards:
- **Pylint compliant**: All code passes Pylint checks with proper naming conventions
- **Comprehensive documentation**: Module and function docstrings following Python standards
- **Type safety**: Proper error handling with specific exception types
- **Logging best practices**: Structured logging with timestamps and appropriate levels
- **Constants**: Configuration values use uppercase naming convention (`DOWNLOAD_FOLDER`, `DESTINATION`)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] Add support for additional file types
- [ ] Implement file organization by date/size
- [ ] Add a GUI interface using tkinter or PyQt
- [ ] Add undo functionality with file history
- [ ] Implement custom folder mapping configuration file
- [ ] Add file organization by content type detection (magic numbers)
- [ ] Add dry-run mode to preview changes
- [ ] Implement recursive subdirectory organization
- [ ] Add file age-based organization options

## 📫 Contact

If you have any questions or suggestions, please open an issue in the repository.

## 🙏 Acknowledgments

- Python standard library for making file operations simple
- All contributors and users of this tool

---
Made with ❤️ by Kino
