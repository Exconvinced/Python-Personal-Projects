# Python Personal Projects

## 1. Tic Tac Toe
Features: 
> * Controls: Each cell of the 3x3 board is mapped to each numeric key in the NumPad.
> * Opponent selection: The player can compete against either a BOT or a HUMAN.
> * Another round: No need to re-run the code to play another round.
> * Faster moves: No need to press Enter to send a move. 'msvcrt' module is used.

Updates: 
> * Added clear screen function to avoid jumping of texts and elements on screen.
> * Updated prompt and system messages.
> * Added few `\n` whitespaces to separate promt messages from system messages.
> * Replaced msvcrt by getch module

For improvement:
> * Custom control mappings
> * Custom puck displays (Default is 'X' vs 'O')
> * New board unicode designs
> * More generalized lists appending for nxn boards
> * Testing for OSX and Linux compatibility

## 2. Random Password Generator
Features: 
> * Password preference: Allows the user to include or exclude alphabet, numeric or punctuation characters before generating.
> * Password length: Can be increased or decreased using the [+] and [-], respectively. Minimum value is 1.
> * Live password generation: a new password is generated whenever the the password length or preference is changed.
> * Toggles: A tickbox appears filled whenever its preference is activated. Displays its associated keyboard key when deactivated.
> * No scrolling: The screen stays in place thanks to the clear function invoked at every loop.

Update: Replaced msvcrt by getch module

For improvement:
> * Encrypted password/credentials vault
> * Add export-to-file function
> * Add send-to-email function
> * Interface rearrangement

## 3. Passphrase Strengthener
Features: 
> * Based on a Codewars training kata
> * Translates a user's passphrase into an cryptographic-like string
> * Aims to mask a phrase that is only known to the user

For improvement:
> * Add an interactive user interface
> * Add export-to-file function
> * Add send-to-email function

# Upcoming Projects
> * Rock, Papers, Scissors
> * Euclidean Algorithm
> * Big - Little Endian Converter
> * Multiple Choice ABCDE Randomizer
> * Todo App
> * Authentication System
