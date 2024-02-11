import os
import subprocess
from datetime import datetime, timedelta

def modify_file(file_path, text_to_add):
    with open(file_path, 'a') as file:
        file.write(text_to_add)

def git_add_commit_push(date, commit_message):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '--date=' + date.strftime("%Y-%m-%d %H:%M:%S"), '-m', commit_message])
    subprocess.run(['git', 'push'])

def main():
    # Clone the GitHub repository to a local folder
    repo_url = 'https://github.com/yourusername/yourrepository.git'
    local_folder = 'local_repo'
    subprocess.run(['git', 'clone', repo_url, local_folder])

    # Change directory to the cloned repository
    os.chdir(local_folder)

    # User input for start and end dates
    start_date_input = input("Enter start date (YYYY-MM-DD): ")
    end_date_input = input("Enter end date (YYYY-MM-DD): ")

    # Convert input strings to datetime objects
    start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_input, "%Y-%m-%d")

    # Text to add to the file
    text_to_add = "Your text goes here\n"

    # File to modify
    file_path = os.path.join(local_folder, 'path', 'to', 'your', 'file.txt')

    # Iterate over dates, modify file, add, commit, and push
    current_date = start_date
    while current_date <= end_date:
        modify_file(file_path, text_to_add)
        git_add_commit_push(current_date, "New Changes")
        current_date += timedelta(days=1)

if __name__ == "__main__":
    main()
