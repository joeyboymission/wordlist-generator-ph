# PASSWORD WORDLIST GENERATOR

**Author:** J01B01 (Alias Zero One "01")  
**Co-Author:** ChatGPT4o (Python Programmer)  
**Date Created:** August 2024
**Status** Active and still in progress

## Summary
This is a simple script implemented in Python that generates password wordlists for internet service providers, including:

1. PLDT (PLDTMyDSL, PLDTHome, PLDTHomeFibr, PLDTHomeULTERA, PLDTHOMEWIFI, PLDTHomePrepaidWiFi, PLDTWIFI)
2. Converge (ConvergeICT, ConvergeXFiber, ConvergeX, ConvergePrepaidWiFi, ConvergeFiberX, ConvergeEnterprise)

**Disclaimer:**  
This script is provided solely for educational and informational purposes. It is intended for use in penetration testing, vulnerability assessment, and security auditing. Any use of this script for illegal activities, including those that cause harm, damage, or violate the law, is strictly forbidden and will not be tolerated.

## Background
My curiosity about how things work has driven me to investigate the vulnerabilities and loopholes within various systems, particularly networks. Every system, including routers and modems that secure our networks with passwords or Pre-Shared Keys (PSK), possesses inherent weaknesses. It is our responsibility to use this knowledge ethically.

Passwords generally consist of symbols and characters arranged in diverse patterns. These may be default passwords provided by network providers or customized by users, often based on personal preferences such as names, favorite sports teams, games, artists, or pets.

The complexity and length of a password determine its resistance to machine-based guessing. However, even complex passwords can be compromised through methods like Social Engineering, Man-in-the-Middle Attacks, or Rogue Attacks. It is crucial to use this knowledge wisely and cautiously, as misuse can result in severe consequences or penalties.

## Requirements
- Any operating system that supports a command-line interface (CLI) and Python.
- Knowledge of networking concepts.
- Tools: Aircrack-ng and John the Ripper.

## Usage
To use the script, you can either download the ZIP file or clone the repository.

1. Access the script using any CLI available on your operating system, such as Command Line Terminal or PowerShell. Ensure that you run the CLI in administrator mode to allow the program to write output to the specified directory.
  
2. Navigate to the directory containing the script using the `cd` command followed by the directory path. For example, if you want to create a wordlist for PLDT, navigate to the "PLDTDictionaries" directory. For ZTE, navigate to the "ZTEDictionaries" directory.

3. Inside the specified folder, you will find a Python script named:
   - **PLDT**: `pldtwifiFIBR.py`
   - **ZTE**: `zteF670L.py`

4. To run the script, use the following command:

   ```bash
   python [script_filename] "[output_directory]" "[output_filename]" [number_of_lines] [number_of_batches]
   ```

   For example:

   ```bash
   python pldtwifiFIBR.py "C:\Custom\Directory\" "customName.txt" 1000 10
   ```

   If the command is incorrect, error handling will provide feedback.

## Contributing
Contributions are welcome! Feel free to refactor the current codebase or add to the project. This project is primarily for educational and demonstration purposes, so detailed documentation and verbose contributions are appreciated.