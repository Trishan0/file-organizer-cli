# Smart File Organizer

Smart File Organizer is a tool that automatically organizes your files into categorized directories based on file extensions. It helps keep your directories clean and structured by sorting files into appropriate folders such as Documents, Images, Videos, etc.

The project offers two implementations:
- A Bash script for Unix/Linux users
- A Python program with added features and cross-platform support

## Features

- Automatically sorts files based on their extensions
- Customizable category definitions
- Preserves original filenames
- Detects and handles filename conflicts
- Creates category directories as needed
- Provides execution logs

## Installation

### Prerequisites

#### Bash Implementation
- Bash shell (available by default on most Unix/Linux systems)

#### Python Implementation
- Python 3.6 or higher

### Setup

1. Clone this repository:
```
git clone https://github.com/yourusername/smart-file-organizer.git
cd smart-file-organizer
```

2. Make the Bash script executable (if using the Bash implementation):
```
chmod +x bash/organize.sh
```

## Configuration

### Bash Implementation

The file categorization is defined in `bash/categories.conf`. Each line contains a category name followed by file extensions to be included in that category, separated by a colon.

Example:
```
DOCUMENTS:pdf,doc,docx,txt,rtf,odt
IMAGES:jpg,jpeg,png,gif,bmp,svg
VIDEOS:mp4,mkv,avi,mov,wmv
```

### Python Implementation

The Python version uses `python/categories.json` for configuration. It's a JSON file mapping categories to arrays of file extensions.

Example:
```json
{
"DOCUMENTS": ["pdf", "doc", "docx", "txt", "rtf", "odt"],
"IMAGES": ["jpg", "jpeg", "png", "gif", "bmp", "svg"],
"VIDEOS": ["mp4", "mkv", "avi", "mov", "wmv"]
}
```

## Usage

### Bash Implementation

```bash
./bash/organize.sh /path/to/directory
```

If no directory is specified, it will organize files in the current directory.

### Python Implementation

```bash
python3 python/main.py /path/to/directory
```

If no directory is specified, it will organize files in the current directory.

## Examples

### Organizing Downloads Folder

#### Using Bash:
```bash
./bash/organize.sh ~/Downloads
```

#### Using Python:
```bash
python3 python/main.py ~/Downloads
```

## How It Works

1. The script/program scans the target directory for files
2. It determines the category of each file based on its extension
3. It creates category directories if they don't exist
4. It moves each file to its corresponding category directory
5. If a file with the same name already exists in the destination, it handles the conflict by adding a unique identifier

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Thanks to all the contributors who have helped improve this tool
- Inspired by the need for a simple, customizable file organization solution
