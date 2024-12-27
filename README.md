
# EXIF Tool Clone

A Python-based tool for extracting and displaying EXIF and other metadata from image files.

- ## Features

    - **Extract EXIF Data**: Retrieve EXIF metadata from JPEG files.
    - **Display Metadata**: Show metadata in a structured and readable table.
    - **Strip EXIF Data**: Remove EXIF data from images and save them without it.

## Installation

### Prerequisites

- Python 3.7+ installed on your machine.
- Dependencies:
  - `Pillow` for opening and processing images.
  - `piexif` for working with EXIF data.
  - `rich` for rich formatting and table display.
  - `pymediainfo` for additional media metadata extraction.

### Installing Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/exiftools.git
   cd exiftools


2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Additional Setup for MediaInfo (If Required)

- **On Ubuntu/Debian**:
  ```bash
  sudo apt install libmediainfo0v5 mediainfo
  ```

- **On Arch Linux**:
  ```bash
  sudo pacman -S libmediainfo mediainfo
  ```

- **On macOS**:
  ```bash
  brew install mediainfo
  ```

## Usage

### Extract EXIF Data

To extract and display EXIF data from an image, run:

```bash
python exiftool.py <path_to_image>
```

Example:
```bash
python exiftool.py /home/user/Pictures/photo.jpg
```

This will display the EXIF data in a table format.

### Strip EXIF Data

To remove EXIF data from an image and save it as a new file, use the `--strip` flag:

```bash
python exiftool.py <path_to_image> --strip --output=/path/to/output.jpg
```

Example:
```bash
python exiftool.py /home/user/Pictures/photo.jpg --strip --output=/home/user/Pictures/photo_no_exif.jpg
```

### MediaInfo Metadata Extraction (Optional)

To extract metadata from media files (audio, video), you can use the `--mediainfo` flag:

```bash
python exiftool.py <path_to_media_file> --mediainfo
```

Example:
```bash
python exiftool.py /home/user/Videos/sample.mp4 --mediainfo
```

## Acknowledgements

- **Pillow**: Python Imaging Library used for image processing.
- **piexif**: EXIF handling in Python.
- **Rich**: For rich-text output in the terminal.
- **pymediainfo**: Media metadata extraction (optional).
```