import os
import subprocess

def modify_file(file_path, text_to_add):
    with open(file_path, 'a') as file:
        file.write(text_to_add)

