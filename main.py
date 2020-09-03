import os
import config

def get_words(file):
    with open(file, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def send_message(phone_number, message):
    os.system('osascript send.scrpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    words = get_words('chickenwing.txt')
    for word in words:
        send_message(config.FRIEND, word)