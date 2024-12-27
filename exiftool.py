import os
import sys
from PIL import Image
import piexif
from pymediainfo import MediaInfo
from rich.console import Console
from rich.table import Table

console = Console() 

# Reading
def read_exif(file_path):
    # Trying to read the EXIF Data
    try:
        img = Image.open(file_path)
        
        if img.format not in ["JPEG", "TIFF"]:
            console.print(f"[bold yellow]EXIF data is not supported for {img.format} files.[/bold yellow]") 
            return None
        
        exif_bytes = img.info.get("exif", b"")
        if not exif_bytes:
            console.print("[bold yellow]No EXIF data found in the file.[/bold yellow]")
            return None
        
        exif_data = piexif.load(exif_bytes)
        return exif_data
    except Exception as e:
        console.print(f"[bold red]Error reading EXIF data: {e}[/bold red]")
        return None
def extract_mediainfo_metadata(file_path):
    # Try to Get the metainfo from the image file
    try:
        media_info = MediaInfo.parse(file_path)
        metadata = {}
        for track in media_info.tracks:
            for key, value in track.to_data().items():
                metadata[key] = value
        return metadata
    except Exception as e:
        console.print(f"[bold red]Error extracting MediaInfo metadata: {e}[/bold red]")
        return {}

# Display MetaData
def display_metadata(metadata, title):
    if not metadata:
        console.print(f"[bold yellow]No {title} metadata found.[/bold yellow]")
        return
    
    table = Table(title=title)
    table.add_column("Key", style="bold cyan")
    table.add_column("Value", style="green")

    for key, value in metadata.items():
        table.add_row(str(key), str(value))
    
    console.print(table)

def display_exif(exif_data):
    # Display the EXIF & Meta Data
    if not exif_data or all(not data for data in exif_data.values()):
        console.print("[bold yellow]No EXIF metadata found in the file.[/bold yellow]")
        return

    table = Table(title="EXIF Data")
    table.add_column("Tag", style="bold cyan")
    table.add_column("Value", style="green")

    for ifd_name, ifd_data in exif_data.items():
        if isinstance(ifd_data, bytes):
            console.print(f"[bold yellow]{ifd_name} contains binary data (e.g., thumbnail), skipping...[/bold yellow]")
            continue

        if not ifd_data:  
            console.print(f"[bold yellow]No data for {ifd_name}[/bold yellow]")
            continue

        for tag, value in ifd_data.items():
            try:
                tag_name = piexif.TAGS[ifd_name][tag]["name"]
                table.add_row(tag_name, str(value))
            except KeyError:
                console.print(f"[bold red]Unknown tag: {tag}[/bold red]")
    
    console.print(table)

# Stripping of the exif data from image file
def strip_exif(file_path, output_path):
    try:
        img = Image.open(file_path)
        img.save(output_path, "jpeg", exif=b"")
        console.print(f"[bold green]Saved without EXIF data: {output_path}[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error removing EXIF data: {e}[/bold red]")

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Usage: python exiftools.py <image_path> [--strip] [--output=<output_path>][/bold red]")
        return

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        console.print("[bold red]File does not exist.[/bold red]")
        return

    if "--strip" in sys.argv:
        output_path = "output.jpg"
        for arg in sys.argv:
            if arg.startswith("--output="):
                output_path = arg.split("=")[1]
        strip_exif(file_path, output_path)
    else:
        console.print(f"[bold blue]Extracting metadata for: {file_path}[/bold blue]")

        exif_data = read_exif(file_path)
        if exif_data:
            display_exif(exif_data)

        mediainfo_metadata = extract_mediainfo_metadata(file_path)
        if mediainfo_metadata:
            display_metadata(mediainfo_metadata, "Detailed Metadata (MediaInfo)")

if __name__ == "__main__":
    main()
