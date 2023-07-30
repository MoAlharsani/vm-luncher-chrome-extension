import sys
import subprocess
import json

def execute_batch(ip_address):
    try:
        # Replace "path/to/batch_file.bat" with the actual path to your .bat file
        result = subprocess.check_output(["path/to/batch_file.bat", ip_address], text=True)
        return {"response": result.strip()}
    except subprocess.CalledProcessError:
        return {"error": "Failed to execute the batch file."}

def read_message():
    # Your existing read_message() function remains unchanged
    pass

def send_response(response):
    # Your existing send_response() function remains unchanged
    pass

if __name__ == '__main__':
    message = read_message()
    ip_address = message.get('ip_address')
    if ip_address:
        response = execute_batch(ip_address)
        send_response(response)
