# Keylogger with Idle Time Monitoring

This Python script is a keylogger that logs all key presses and monitors system idle time. If the system is idle for a specified amount of time, it records this event in the log file.

## Features

- Logs all key presses including spaces, special keys, and new lines.
- Monitors idle time and logs a message if the system is idle for a specified duration.
- Uses multi-threading to handle key logging and idle time monitoring concurrently.

## Requirements

- Python 3.x
- pynput library

You can install the pynput library using pip:

sh
pip install pynput


## Usage

1. Clone the repository:

sh
git clone https://github.com/your-username/Python-Keylogger-IdleTracker
.git
cd Python-Keylogger-IdleTracker


2. Run the script:

sh
python keylogger.py


The key logs will be saved in a file named keylogger.txt.

## Configuration

You can adjust the idle time duration by changing the value of record_time in the script:

python
record_time = 10  # Set the idle time in seconds


## Warning

This script is intended for educational purposes only. Do not use it for any illegal activities, including but not limited to unauthorized monitoring of individuals without their consent. Misuse of this software can result in severe legal consequences. Always obtain proper authorization before using this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
