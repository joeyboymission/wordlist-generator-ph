#!/usr/bin/env python3

import string
import argparse
import os
import sys
import numpy as np
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def generate_unique_combinations(num_combinations):
    characters = string.ascii_lowercase + string.digits  # Includes lowercase letters and digits
    ascii_characters = np.array([ord(c) for c in characters], dtype=np.int32)
    seen = set()
    combinations = []

    while len(combinations) < num_combinations:
        batch_size = min(num_combinations - len(combinations), 10000)
        batch = np.random.choice(ascii_characters, (batch_size, 8))
        for comb in batch:
            comb_str = ''.join(chr(c) for c in comb)
            if comb_str not in seen:
                seen.add(comb_str)
                combinations.append(comb_str)
                if len(combinations) % 1000 == 0:  # Update progress every 1000 combinations
                    print_progress(len(combinations), num_combinations)
    
    return combinations

def write_to_file(output_dir, filename, combinations, total_combinations):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        sys.exit(1)

    file_path = os.path.join(output_dir, filename)
    
    with open(file_path, 'w') as file:
        for i, comb in enumerate(combinations, 1):
            file.write(comb + '\n')
            if i % 1000 == 0:  # Update progress every 1000 combinations
                print_progress(i, total_combinations)
    
    return file_path

def print_progress(current, total):
    progress = (current / total) * 100
    filled_length = int(progress // 5)  # Each character represents 5%
    bar = '=' * filled_length + ' ' * (20 - filled_length)  # Fixed bar length of 20
    print(f'\rProgress: {progress:.2f}% ({current}/{total}) [{bar}]', end='')
    sys.stdout.flush()

def main():
    parser = argparse.ArgumentParser(description="Generate random 8-character strings and export to a text file.")
    parser.add_argument('-d', '--directory', required=True, help="Directory to export the text file.")
    parser.add_argument('-n', '--number', type=int, required=True, help="Number of combinations to generate.")
    
    args = parser.parse_args()

    start_time = datetime.now()
    combinations = generate_unique_combinations(args.number)
    total_combinations = args.number
    
    file_path = write_to_file(args.directory, 'ztelib.txt', combinations, total_combinations)
    end_time = datetime.now()
    duration = end_time - start_time
    
    print(f"\n\n********************************************")
    print(f"{Fore.GREEN}===== Generate library file successfully! =====")
    print(f"Total number of passwords: {total_combinations}")
    print(f"Time duration: {start_time.strftime('%Y-%m-%d %H:%M:%S')} to {end_time.strftime('%Y-%m-%d %H:%M:%S')} ({str(duration)})")
    print(f"File saved to: {file_path}")
    print(f"********************************************\n\n")

if __name__ == '__main__':
    main()
