import os
import time
def get_file_data(filename:str) -> str | None:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f'The the file with name {filename} doesn\'t exist. Create it first!')
        return None
    
def save_file_data(filename:str, data:str):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
            print('Saved data to', filename)
    except Exception as e:
        print(f'An error occured while writing encoded data to file')

def format_file_data(data:str) -> str | None:
   initstring:str=''
   alphabets:str="abcdefghijklmnopqrstuvwxyz"
   for ch in data:
       if ch.lower() in alphabets:
           initstring = initstring + ch.upper()
   return initstring

def chunk5(data:str):
    blocks = [data[i:i+5] for i in range(0, len(data), 5)]
    return blocks

def get_key() -> int:
    """Prompt until the user enters an integer key in [1, 25], then return it."""
    while True:
        raw = input("Enter a key (1â€“25): ").strip()
        try:
            k = int(raw)
            if k in range(1, 25):
                return k
            else:
                print("Invalid â€” key must be between 1 and 25.")
        except ValueError:
            print("Invalid â€” please enter a number (e.g., 5).")

def encode(text:str, key:int) -> str:
    """
    Returs the Caesar-encoded version of text.

    Parameters
    ----------
    text: `str`
    The text you want to encode
    """
    if key not in range(1, 25):
        return 'Incorret key provided! Key must be within 1-25'
    alphabets:str="abcdefghijklmnopqrstuvwxyz".upper()
    output_text:str=""
    sor = ord(' ')
    for letter in text:
        if letter in alphabets:
            shifted_position = (alphabets.index(letter) + key)%26
            output_text = output_text + alphabets[shifted_position]
        else:
            val = sor + key
            output_text += chr(val) #it must be space so i encoded it this way. I found this easy
    return output_text


def main():
    try:
        filedata = None
        while True:
            filedata = get_file_data(input('Enter the name of file you want to encrypt: '))
            if filedata:
                break
            else:
                time.sleep(2)
        formated = format_file_data(filedata)
        key = get_key()
        encoded = encode(formated, key)
        chunks = chunk5(encoded)
        initlist = []
        initstring = ''
        m = 0
        for chnk in chunks:
            if m == 8:
                initlist.append(initstring)
                initstring = ''
                m = 0
            initstring += chnk
            m = m + 1
        final = '\n'.join(initlist)
        save_file_data(input('Enter the filename where you want to save encoded stuff: '), final)
    except Exception as e:
        print(f'Error {e}')

if __name__ == '__main__':
    try:
        while True:
            os.system('cls' if os.name=='nt' else 'clear')
            main()
            print()
            choice = input('You wna do it again? ')
            if choice.lower() == 'yes':
                continue
            else:
                break
    except KeyboardInterrupt:
        pass