import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str, effect: str) -> None:
    """
    :param text: text to print
    :param effect: One of the effects which will be applied to the using one of the CONSTANTS defined at start of this module.
    :return: None
    """
    print(effect, text, RESET, flush=True)
colorama.init()
color_print("This text will be in red color", RED)
color_print("This text will be in cyan color", CYAN)
color_print("This text will be in green color", GREEN)
color_print("This text will be in yellow color", YELLOW)
color_print("This text will be in blue color", BLUE)
color_print("This text will be in magenta color", MAGENTA)
color_print("This text will be in bold", BOLD)
color_print("This text will be underlined", UNDERLINE)
color_print("This text will be reversed", REVERSE)
colorama.deinit()
