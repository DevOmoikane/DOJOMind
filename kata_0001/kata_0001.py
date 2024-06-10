
def rgbToHex(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

if __name__ == '__main__':
    text_input = input('Enter R, G, B: ')
    r, g, b = map(int, text_input.split(','))
    print(rgbToHex(r, g, b))
