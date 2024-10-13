import os
import csv
import shutil
import logging
from typing import Tuple, List, Optional
from PIL import Image

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def resize_images(source_dir: str, dest_dir: str, output_size: Tuple[int, int]) -> None:
    """
    Resize images in the source directory and save them to the destination directory.

    Args:
        source_dir (str): Path to the source directory containing images to resize.
        dest_dir (str): Path to the destination directory to save resized images.
        output_size (Tuple[int, int]): Desired output size as (width, height).

    Raises:
        FileNotFoundError: If the source directory does not exist.
    """
    if not os.path.isdir(source_dir):
        logging.error(f"Source directory '{source_dir}' does not exist.")
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

    os.makedirs(dest_dir, exist_ok=True)
    logging.info(f"Resizing images from '{source_dir}' to '{dest_dir}' with size {output_size}.")

    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(supported_formats):
            try:
                with Image.open(filepath) as img:
                    img = img.resize(output_size, Image.LANCZOS)
                    img.save(os.path.join(dest_dir, filename))
                logging.info(f"Resized and saved '{filename}' to '{dest_dir}'.")
            except Exception as e:
                logging.warning(f"Failed to process '{filename}': {e}")
    logging.info("Completed resizing images.")


def move_files(source_dir: str, dest_dir: str, file_extension: Optional[str] = None) -> None:
    """
    Move files from the source directory to the destination directory.

    Args:
        source_dir (str): Path to the source directory containing files to move.
        dest_dir (str): Path to the destination directory.
        file_extension (Optional[str]): Specific file extension to move (e.g., '.jpg'). If None, moves all files.

    Raises:
        FileNotFoundError: If the source directory does not exist.
    """
    if not os.path.isdir(source_dir):
        logging.error(f"Source directory '{source_dir}' does not exist.")
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

    os.makedirs(dest_dir, exist_ok=True)
    logging.info(f"Moving files from '{source_dir}' to '{dest_dir}' with extension '{file_extension}'.")

    for filename in os.listdir(source_dir):
        if file_extension is None or filename.lower().endswith(file_extension.lower()):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            if os.path.isfile(source_path):
                try:
                    shutil.move(source_path, dest_path)
                    logging.info(f"Moved '{filename}' to '{dest_dir}'.")
                except Exception as e:
                    logging.warning(f"Failed to move '{filename}': {e}")
    logging.info("Completed moving files.")


def generate_csv(
    csv_filename: str,
    source_dir: str,
    columns: Optional[List[str]] = None,
    label: Optional[str] = None
) -> None:
    """
    Generate a CSV file with filenames and an optional label.

    Args:
        csv_filename (str): Path to the CSV file to create or append to.
        source_dir (str): Path to the source directory containing files to list.
        columns (Optional[List[str]]): Column headers for the CSV. Required if creating a new CSV.
        label (Optional[str]): Label to assign to each file. If None, labels are omitted.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        ValueError: If columns are not provided when creating a new CSV.
    """
    if not os.path.isdir(source_dir):
        logging.error(f"Source directory '{source_dir}' does not exist.")
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

    file_exists = os.path.isfile(csv_filename)
    logging.info(f"Generating CSV '{csv_filename}' from '{source_dir}'.")

    with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            if columns is None:
                logging.error("Column headers must be provided when creating a new CSV.")
                raise ValueError("Column headers must be provided when creating a new CSV.")
            writer.writerow(columns)
            logging.info(f"Created CSV with columns: {columns}")

        for filename in os.listdir(source_dir):
            filepath = os.path.join(source_dir, filename)
            if os.path.isfile(filepath):
                row = [filename]
                if label is not None:
                    row.append(label)
                writer.writerow(row)
                logging.info(f"Added '{filename}' to CSV.")
    logging.info("Completed generating CSV.")