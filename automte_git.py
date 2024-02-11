import os
import subprocess

def modify_file(file_path, text_to_add):
    with open(file_path, 'a') as file:
        file.write(text_to_add)

def git_add_commit(date, commit_message):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '--date=' + date, '-m', commit_message])

def main():
    # Clone the GitHub repository to a local folder
    repo_url = 'https://github.com/yourusername/yourrepository.git'
    local_folder = 'local_repo'
    subprocess.run(['git', 'clone', repo_url, local_folder])

    # Dates to commit changes
    commit_dates = [
        "2023-01-01 15:35:08",
        "2023-01-02 10:20:00",
        # Add more dates as needed
    ]

    # Text to add to the file
    text_to_add = "Your text goes here\n"

    # File to modify
    file_path = os.path.join(local_folder, 'path', 'to', 'your', 'file.txt')

    # Iterate over dates, modify file, add, and commit
    for date in commit_dates:
        modify_file(file_path, text_to_add)
        git_add_commit(date, "New Changes")

if __name__ == "__main__":
    main()
