# README

## Introduction

This is a simple keylogger script written in Python, which records every key press and saves it into a log file. It uses the `keyboard` module to listen to the keyboard input and the `datetime` module to timestamp each event.

The script creates a folder called `Key` in the `C:/ProgramData/` directory and saves the log file `log.txt` inside this folder.

## Requirements

The script requires the `keyboard` module to be installed. You can install it using the following command:

``pip install keyboard``


## Usage

### Python

To use this script, simply run the `main.py` file using Python.
The keylogger will start running as soon as you execute the script. It will record every key press and save it to the `log.txt` file in the `Key` folder.

### Executable

You can also create an executable file using the `pyinstaller` command mentioned in the code comments.
It will record every key press and save it to the `log.txt` file in the `Key` folder.
The command to create the exe with pyinstaller is: 
```pyinstaller --noconfirm --onefile --windowed --name "key" --hidden-import "keyboard"  "path/to/script/main.py"```


## Disclaimer

This keylogger script is intended for educational purposes only. Please use it responsibly and do not use it for illegal activities. The author is not responsible for any damage caused by the misuse of this script.
