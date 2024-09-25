	#Basic

from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)

# Print text with different foreground colors
print(Fore.RED + 'This text is red')
print(Fore.GREEN + 'This text is green')
print(Fore.BLUE + 'This text is blue')

# Print text with different background colors
print(Back.YELLOW + 'This text has a yellow background')
print(Back.CYAN + 'This text has a cyan background')

# Reset styles
print(Style.RESET_ALL + 'This text is back to normal')




	#Combining styles

print(Fore.WHITE + Back.RED + 'White text on red background')
print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + 'Bright yellow text on blue background')
print(Fore.BLACK + Back.WHITE + Style.DIM + 'Dim black text on white background')

print(Style.BRIGHT + 'This text is bright')
print(Style.DIM + 'This text is dim')
print(Style.NORMAL + 'This text is normal')




	#Function that prints a styled message

def styled_message(message, fore_color, back_color):
    print(fore_color + back_color + message + Style.RESET_ALL)

styled_message('Hello, World!', Fore.YELLOW, Back.BLUE)




	#Complete example

from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)

def print_colored_messages():
    print(Fore.RED + 'Error: Something went wrong!')
    print(Fore.GREEN + 'Success: Operation completed successfully!')
    print(Fore.YELLOW + Back.BLUE + 'Warning: Check your input!')
    print(Fore.CYAN + 'Info: Here is some information for you.')

print_colored_messages()


