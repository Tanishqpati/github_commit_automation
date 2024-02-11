import os
import subprocess
from datetime import datetime, timedelta

def modify_file(file_path, text_to_add):
    with open(file_path, 'a') as file:
        file.write(text_to_add)

def git_add_commit_push(date, commit_message):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '--date=' + date, '-m', commit_message])
    subprocess.run(['git', 'push'])

def generate_dates(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d %H:%M:%S"))
        current_date += timedelta(days=1)
    return dates

def main():
    # Clone the GitHub repository to a local folder
    repo_url = 'https://github.com/yourusername/yourrepository.git'
    local_folder = 'local_repo'
    subprocess.run(['git', 'clone', repo_url, local_folder])

    # Change directory to the cloned repository
    os.chdir(local_folder)

    # Specify the start and end dates for commits
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Generate commit dates for the whole year
    commit_dates = generate_dates(start_date, end_date)

    # Text to add to the file
    text_to_add = "Your text goes here\n"

    # File to modify
    file_path = os.path.join(local_folder, 'path', 'to', 'your', 'file.txt')

    # Iterate over dates, modify file, add, and commit
    for date in commit_dates:
        modify_file(file_path, text_to_add)
        git_add_commit_push(date, "New Changes")

if __name__ == "__main__":
    main()
