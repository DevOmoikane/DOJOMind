# Convert RGB decimal to hexadecimal
# Input: Integers R, G, and B, as charcode from 0 to 255 (0 <= R,G,B <= 255)
# Output: Display color RGB in hexadecimal starts with hash (Uppercase)
# Example:
# Input: R=65, G=122, B=180
# Output: #417AB4

def rgbToHex(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

if __name__ == '__main__':
    text_input = input('Enter R, G, B: ')
    r, g, b = map(int, text_input.split(','))
    print(rgbToHex(r, g, b))
