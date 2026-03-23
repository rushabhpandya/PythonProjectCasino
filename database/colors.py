from colorama import Fore, Back, Style, init
init(autoreset=True)

def red(text):
    return Fore.RED + str(text) + Style.RESET_ALL

def green(text):
    return Fore.GREEN + str(text) + Style.RESET_ALL

def yellow(text):
    return Fore.YELLOW + str(text) + Style.RESET_ALL

def blue(text):
    return Fore.BLUE + str(text) + Style.RESET_ALL

def cyan(text):
    return Fore.CYAN + str(text) + Style.RESET_ALL

def magenta(text):
    return Fore.MAGENTA + str(text) + Style.RESET_ALL

def white(text):
    return Fore.WHITE + str(text) + Style.RESET_ALL

def bold_green(text):
    return Fore.GREEN + Style.BRIGHT + str(text) + Style.RESET_ALL

def bold_red(text):
    return Fore.RED + Style.BRIGHT + str(text) + Style.RESET_ALL

def bold_yellow(text):
    return Fore.YELLOW + Style.BRIGHT + str(text) + Style.RESET_ALL

def bold_cyan(text):
    return Fore.CYAN + Style.BRIGHT + str(text) + Style.RESET_ALL