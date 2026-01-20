
import string

###############################################################################
#  Program Name   : CT1
#  Author         : Amro
#  Task           : Take in a string, remove punctuation, spaces, and numbers, convert everything to UPPERCASE, and return the cleaned text.
#  Date           : november 30, 2025
###############################################################################

def clean_text(text):
    # Remove punctuation, spaces, and numbers
    cleaned = ''.join(char for char in text if char not in string.punctuation and char not in string.digits and char != ' ')
    # Convert to uppercase
    return cleaned.upper()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = clean_text(user_input)
    print(f"Cleaned text: {result}")


   
    ###############################################################################
#  Program Name   : CT1
#  Author         : Amro
#  Task           : Take the cleaned, uppercase text from CT1 and format it into groups of five letters.                    Each line should contain eight groups of five letters, separated by spaces.
#  Date           : November 30, 2025
###############################################################################






def format_groups(text):
        """Format text into groups of 5 letters, 8 groups per line"""
        groups = [text[i:i+5] for i in range(0, len(text), 5)]
        
        formatted_lines = []
        for i in range(0, len(groups), 8):
            line = ' '.join(groups[i:i+8])
            formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)


    # Add this to main() after the "print(cleaned_text)" line:
    # formatted_text = format_groups(cleaned_text)
    # print("\nFormatted text (5 letters per group, 8 groups per line):")
    # print(formatted_text)


    ###############################################################################
#  Program Name   : CT3 Key Validation.py
#  Author         : Amro
#  Task           : Write a function get_key() -> int that prompts the user.
#date            : december 31, 2025
###############################################################################




def get_key() -> int:
    """
    Prompts the user for an integer key between 1-25.
    Handles non-numeric input and range validation.
    Returns a valid integer key.
    """
    while True:
        try:
            user_input = input("Enter a key (1-25): ")
            key = int(user_input)
            
            # Check range
            if 1 <= key <= 25:
                return key
            else:
                print(f"Error: Key must be between 1 and 25. You entered {key}.")
                
        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer. Please enter a number.")

if __name__ == "__main__":
    key = get_key()
    print(f"Valid key recieved: key = {key}")




    ###############################################################################
#  Program Name   : CT4
#  Author         : Amro
#  Task           : Write a function that encodes cleaned, uppercase text (A–Z only) using a Caesar shift with a valid key (1–25). Return the encoded string.
#date           : january 5, 2026
###############################################################################




def caesar_encode(text, key):
    """
    Encodes cleaned, uppercase text (A-Z only) using Caesar shift.
    
    Args:
        text: String containing only uppercase letters A-Z
        key: Integer shift value (1-25)
    
    Returns:
        Encoded string with Caesar shift applied
    """
    if not (1 <= key <= 25):
        raise ValueError("Key must be between 1 and 25")
    
    encoded = []
    for char in text:
        if char.isalpha():
            # Shift character by key positions, wrapping around alphabet
            shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encoded.append(shifted)
        else:
            encoded.append(char)
    
    return ''.join(encoded)


# Example usage
result = caesar_encode("HELLO", 3)
print(result)  # Output: KHOOR





###############################################################################
#  Program Name   : CT5
#  Author         : Amro
#  Task           : Write a function that decodes uppercase A–Z text that was encoded with a Caesar shift key (1–25). Return the decoded string.
#date           : january 6, 2026
###############################################################################






def decode_caesar(encoded_text, shift):
    """
    Decodes a Caesar cipher with the given shift key.
    
    Args:
        encoded_text: The encoded uppercase text (A-Z)
        shift: The shift key used for encoding (1-25)
    
    Returns:
        The decoded string
    """
    decoded = ""
    for char in encoded_text:
        if char.isalpha():
            # Shift back by the key amount
            decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decoded.append(decoded_char)
        else:
            # Keep non-alphabetic characters as-is
            decoded += char
    return decoded

# Example usage
print(decode_caesar("KHOOR", 3))  # Output: HELLO




###############################################################################
#  Program Name   : CT6
#  Author         : Amro
#  Task           : Write a function that counts th frequrncy of each letter in a given text (case-insensitive) and identifies the most common double letter (consecutive identical letters).
#date           : january 6, 2026
###############################################################################


def count_letters(text):
    """Count the frequency of each letter in the text (case-insensitive)."""
    letter_count = {}
    for char in text.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count


def most_common_double_letter(text):
    """Find the most frequently occurring double letter (consecutive identical letters)."""
    double_letter_count = {}
    text_lower = text.lower()
    
    for i in range(len(text_lower) - 1):
        if text_lower[i].isalpha() and text_lower[i] == text_lower[i + 1]:
            double = text_lower[i:i+2]
            double_letter_count[double] = double_letter_count.get(double, 0) + 1
    
    if not double_letter_count:
        return None
    
    return max(double_letter_count, key=double_letter_count.get)


# Example usage
if __name__ == "__main__":
    sample_text = "hello world, this is a test with letters like ll and ss"
    
    print("Letter frequencies:", count_letters(sample_text))
print("Most common double letter:", most_common_double_letter(sample_text))
    
    
    
    
    


    ###############################################################################
#  Program Name   : CT7
#  Author         : Amro
#  Task           : Complete strategy for decoding a block of encrypted text that has been formatted into 5-character chunks, 8 chunks per line.
#  Date           : January 6, 2026
###############################################################################





def decode(text: str, key: int) -> str:
    base = ord('A')
    out  = ""
    if key not in range(1, 25):
        print('Incorret key provided! Key must be within 1-25')
        return ''
    for ch in text:
        if ch == ' ': #if the character is just space, add it to output text
            out = out + ' ' #without modifying it
            continue
        # 1) Map 'A'..'Z' to 0..25
        pos = ord(ch) - base
        # 2) Shift BACKWARD and wrap
        shifted = (pos - key)%26
        # 3) Convert back to a letter
        dec = chr(shifted + base)
        # 4) Append to output
        out = out + dec
    return out #return the final string
