import random
import string
import os
import sys
import time
from datetime import datetime, timedelta

# Default parameters
DEFAULT_DIRECTORY = r"D:\Documents\PROGRAMMING FILES\Wifi Hacking\dictionaries\PLDTDictionaries"
DEFAULT_FILENAME = "pldtlib.txt"
DEFAULT_NUM_LINES = 1000
DEFAULT_NUM_BATCHES = 10
STATIC_PART = "PLDTWIFI"

def generate_passwords(num_lines):
    """Generates a set of unique passwords with a static part and a random part."""
    passwords = set()
    while len(passwords) < num_lines:
        random_part = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=5))
        password = STATIC_PART + random_part
        passwords.add(password)
    return passwords

def save_passwords_to_file(passwords, file_path):
    """Saves the generated passwords to a text file."""
    with open(file_path, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def display_progress_bar(progress, total, prefix=''):
    """Displays a progress bar with the percentage of completion."""
    bar_length = 50  # Modify this for a shorter or longer bar
    block = int(round(bar_length * progress / total))
    percentage = round(progress / total * 100, 1)
    progress_bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\r{prefix} [{progress_bar}] {percentage}%")
    sys.stdout.flush()

def main(output_dir=DEFAULT_DIRECTORY, filename=DEFAULT_FILENAME, num_lines=DEFAULT_NUM_LINES, num_batches=DEFAULT_NUM_BATCHES):
    """Main function to generate multiple batches of password files."""
    start_time = datetime.now()
    print(f"Starting password generation at {start_time.strftime('%H:%M:%S')}")

    for batch_number in range(1, num_batches + 1):
        batch_file_name = f"{filename.split('.')[0]}_{batch_number}.txt"
        output_file = os.path.join(output_dir, batch_file_name)

        print(f"\nGenerating {batch_file_name}...")
        passwords = generate_passwords(num_lines)

        # Display progress bar for generating a single batch
        for i, _ in enumerate(passwords):
            display_progress_bar(i + 1, num_lines, prefix=batch_file_name)
            time.sleep(0.01)  # Simulate work being done

        save_passwords_to_file(passwords, output_file)

        # Update overall progress
        display_progress_bar(batch_number, num_batches, prefix=f"batch {batch_number} of {num_batches}")
        time.sleep(0.5)  # Small delay to simulate the time taken to save the file

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\nYour library {filename} is successfully generated.")
    print(f"Time {start_time.strftime('%H:%M:%S')} to {end_time.strftime('%H:%M:%S')} with duration of {str(duration)}")

if __name__ == "__main__":
    # Default arguments or command line input
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
        filename = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_FILENAME
        num_lines = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_NUM_LINES
        num_batches = int(sys.argv[4]) if len(sys.argv) > 4 else DEFAULT_NUM_BATCHES
    else:
        output_dir = DEFAULT_DIRECTORY
        filename = DEFAULT_FILENAME
        num_lines = DEFAULT_NUM_LINES
        num_batches = DEFAULT_NUM_BATCHES

    main(output_dir, filename, num_lines, num_batches)
