import pyperclip
import pyautogui
import time

def copy_to_clipboard():
    """Copies the selected text to clipboard and returns it."""
    pyautogui.hotkey('ctrl', 'c')  # 'command' on macOS
    time.sleep(0.2)  # Let the clipboard catch up
    return pyperclip.paste()

def cut_first_line(input_text):
    """Cuts the first line from the given text and copies it to clipboard."""
    lines = input_text.split("\n")
    pyperclip.copy(lines.pop(0))
    time.sleep(0.2)  # Let the clipboard catch up
    
    return "\n".join(lines)

def paste_from_clipboard():
    """Pastes text from the clipboard."""
    pyautogui.hotkey('ctrl', 'v')  # 'command' on macOS
    time.sleep(0.2)  # Let the clipboard catch up


def navigate_fields():
    """Navigates to the next field."""
    pyautogui.hotkey('tab')
    time.sleep(0.1)  # Let the clipboard catch up


def submit_form():
    """Submits the current form."""
    pyautogui.hotkey('ctrl', 'enter')  # 'command' on macOS
    time.sleep(0.2)  # Let the clipboard catch up


def fill_anki_card():
    """Processes the text block and manages the flashcard formatting."""
    pyautogui.hotkey('ctrl', 'a')  # 'command' on macOS
    input_text = copy_to_clipboard()

    if input_text:
        # Take the first line and paste it
        remaining_text = cut_first_line(input_text)
        paste_from_clipboard()
        navigate_fields()
        navigate_fields()

        # Take the next line and paste it
        remaining_text = cut_first_line(remaining_text)
        paste_from_clipboard()
        submit_form()

        # Update the clipboard with the remaining text
        pyperclip.copy(remaining_text)
        paste_from_clipboard()
        
        return True
    return False

def convert_flashcard_format():
    """Keeps processing text blocks until there's no text left."""
    while fill_anki_card():
        # The loop will call process_text_block() until it returns False
        time.sleep(0.2)  # Prevent potential for rapid-fire input

convert_flashcard_format()
