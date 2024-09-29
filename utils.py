from pathlib import Path
import sys


# Function to read the config
def read_config(config_file="config.txt"):
    """Read input and output file paths from the config file."""
    config = {}
    with open(config_file, 'r') as file:
        for line in file:
            key, value = line.strip().split(' = ')
            config[key] = value
    return config



# Function to check if the file exists and valid in the config
def check_file_exists_and_valid(file_path):
    try:
        file = Path(file_path)

        # Check if the file exists, is a .txt file, and is not empty
        if not file.is_file():
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        if file.suffix != '.txt':
            raise ValueError(f"File '{file_path}' is not in .txt format. It's a '{file.suffix}' file.")

        if file.stat().st_size == 0:
            raise ValueError(f"File '{file_path}' is empty.")

        print(f"File '{file_path}' is a valid non-empty .txt file")
        return True

    except Exception as e:
        print(e)
        sys.exit(1)

