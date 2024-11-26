# Title: HOW TO GET THE UNICODE VALUE OF THE UNICODE CHARACTER such as 🥰😍😇🥸🤩

def enter_char():
    return input("Enter character to get its ASCII's value: ")

def print_char_ascii_value(character):
    if len(character) > 1:
        return [ord(char) for char in character]
    else: 
        return ord(character) if len(character) > 1 else ord(" ")

symbol = enter_char()
ascii_value = print_char_ascii_value(symbol)

print(f"The ASCII value for {symbol} is {ascii_value}")
'''
😀🥰😍😇🥸🤩🥳🤣😆
🐣🦅🍏🍎🍐🍓🍉🥐🫛
⚽️🏀🏈🏓🎱⛸️🥊🚕🚐
📱⌚️💻❤️🇳🇬🇺🇸🇮🇱🇩🇪🇬🇧💔
'''