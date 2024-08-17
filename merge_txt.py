import os
import sys
import time
from datetime import datetime

def merge_text_files(input_dir, output_file):
    # Start timing the process
    start_time = datetime.now()
    print(f"Start time: {start_time.strftime('%H:%M:%S')}")
    
    # Initialize variables
    all_lines = set()  # Use a set to remove duplicates
    total_files = len([f for f in os.listdir(input_dir) if f.endswith('.txt')])
    
    if total_files == 0:
        print(f"No .txt files found in {input_dir}")
        return

    files_processed = 0
    duplicates_count = 0

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                initial_length = len(all_lines)
                all_lines.update(line.strip() for line in lines)
                duplicates_count += (len(lines) - (len(all_lines) - initial_length))
            
            files_processed += 1
            
            # Update progress bar
            progress = int((files_processed / total_files) * 50)  # Scale to 50 characters wide
            sys.stdout.write(f"\rMerging files: [{'#' * progress}{' ' * (50 - progress)}]")
            sys.stdout.flush()

    # Write merged content to output file
    with open(output_file, 'w', encoding='utf-8') as output:
        for line in all_lines:
            output.write(line + '\n')

    # End timing the process
    end_time = datetime.now()
    duration = end_time - start_time

    print("\n")
    print(f"End time: {end_time.strftime('%H:%M:%S')}")
    print(f"Duration: {str(duration).split('.')[0]}")  # Removing microseconds for HH:MM:SS format

    # Print final messages
    print(f"The text file merge successfully! All text files from '{input_dir}' have been merged into '{output_file}'")
    print(f"{duplicates_count} duplicates have been removed successfully")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_txt.py <input_directory> <output_file>")
    else:
        input_directory = sys.argv[1]
        output_file = sys.argv[2]
        merge_text_files(input_directory, output_file)
