# Git Automation Script

This script automates the process of making changes to a file in a GitHub repository and committing those changes with specified dates.

## Overview

The script is written in Python and utilizes the Git command-line tool to perform the following tasks:

- Clone a GitHub repository to a local folder.
- Modify a specified file by adding text to it.
- Stage the changes using `git add .`.
- Commit the changes with the specified dates using `git commit`.

## Usage

1. **Clone the Repository**: Replace `repo_url` in the script with the URL of your GitHub repository and `local_folder` with the desired local folder name.

2. **Specify Dates and Text**: Add the dates you want to commit changes for and the text you want to add to the file in the script.

3. **Run the Script**: Execute the Python script by running `python automate_git.py` in your terminal or command prompt.

4. **Monitor Output**: The script will print progress and any errors encountered during the process.

## Requirements

- Python 3.x
- Git

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
