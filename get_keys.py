# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    output_keys_to_notepad(keys)
    return keys

def output_keys_to_notepad(text):
    keyfile = open("keyfile.txt", "a")
    for entry in text:
        keyfile.write(entry)
    keyfile.close()