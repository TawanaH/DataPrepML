# DataPrepML

**DataPrepML** is a Python library designed to streamline data preparation tasks for machine learning projects. It provides a set of utility functions to handle common tasks such as image resizing, file management, and CSV generation, allowing data scientists and machine learning engineers to focus more on model development and less on data preprocessing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Resizing Images](#resizing-images)
  - [Moving Files](#moving-files)
  - [Generating CSV Files](#generating-csv-files)
- [Example Workflow](#example-workflow)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Image Resizing**: Easily resize batches of images to a specified dimension.
- **File Management**: Move files between directories based on file extensions.
- **CSV Generation**: Create CSV files listing filenames with optional labeling for dataset annotations.
- **Logging**: Integrated logging to monitor the progress and handle errors gracefully.
- **Flexible and Extensible**: Designed to be easily integrated into various data preprocessing pipelines.

## Installation

## Usage

- ### Resizing Images
  ```
  resize_images(
      source_dir='path/to/source/images',
      dest_dir='path/to/destination/images',
      output_size=(256, 256)  # Width, Height in pixels
  )
  ```

- ### Moving Files
  ```
  # Move all files
  move_files(
      source_dir='path/to/source/files',
      dest_dir='path/to/destination/files'
  )
  
  # Move only JPEG images
  move_files(
      source_dir='path/to/source/images',
      dest_dir='path/to/destination/images',
      file_extension='.jpg'
  )
  ```

- ### Generating CSV Files
  ```
  # Without labels
  generate_csv(
      csv_filename='dataset.csv',
      source_dir='path/to/files',
      columns=['filename']
  )
  
  # With labels
  generate_csv(
      csv_filename='dataset.csv',
      source_dir='path/to/files',
      columns=['filename', 'label'],
      label='cat'
  )
  ```

## Example Workflow

```
import DataPrep as dp

# Step 1: Resize Images
dp.resize_images(
    source_dir='data/raw_images',
    dest_dir='data/resized_images',
    output_size=(224, 224)
)

# Step 2: Move Processed Images to Training Directory
dp.move_files(
    source_dir='data/resized_images',
    dest_dir='data/train_images',
    file_extension='.png'
)

# Step 3: Generate CSV for Training Labels
dp.generate_csv(
    csv_filename='data/train_labels.csv',
    source_dir='data/train_images',
    columns=['filename', 'label'],
    label='dog'
)
```

## Conributing

Contributions are welcome! If you have suggestions for improvements or want to report issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
