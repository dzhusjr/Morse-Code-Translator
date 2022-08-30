import random as r,winsound,time,requests
from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.image = ImageTk.PhotoImage(Image.open(r"morse_code\1.png").resize((100, 120)))
root.overrideredirect(1)
root.geometry('100x120')
root.eval('tk::PlaceWindow . center')
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", 'black')
Label(root, image=root.image, bg='black').pack()
root.withdraw()

everything = {
    'A': '.-','B': '-...','C': '-.-.',
    'D': '-..','E': '.','F': '..-.',
    'G': '--.','H': '....','I': '..',
    'J': '-.-','K': '-.-','L': '.-..',
    'M': '--','N': '-.','O': '---',
    'P': '.--.','Q': '--.-','R': '.-.',
    'S': '...','T': '-','U': '..-',
    'V': '...-','W': '.--','X': '-..-',
    'Y': '-.--','Z': '--..','0': '-----',

    '1': '.----','2': '..---','3': '...--',
    '4': '....-','5': '.....','6': '-....',
    '7': '--...','8': '---..','9': '----.',

    '.': '.-.-.-',',': '--..--','?': '..--..',
    '\'': '.----.','!': '-.-.--','/': '-..-.',
    '(': '-.--.',')': '-.--.-','&': '.-...',
    ':': '---...',';': '-.-.-.','=': '-...-',
    '+': '.-.-.','-': '-....-','_': '..--.-',
    '"': '.-..-.','$': '...-..-','@': '.--.-.',
    ' ': '/'
}
letters = {
    'A': '.-','B': '-...','C': '-.-.',
    'D': '-..','E': '.','F': '..-.',
    'G': '--.','H': '....','I': '..',
    'J': '-.-','K': '-.-','L': '.-..',
    'M': '--','N': '-.','O': '---',
    'P': '.--.','Q': '--.-','R': '.-.',
    'S': '...','T': '-','U': '..-',
    'V': '...-','W': '.--','X': '-..-',
    'Y': '-.--','Z': '--..'
}
digits = {
    '1': '.----','2': '..---','3': '...--',
    '4': '....-','5': '.....','6': '-....',
    '7': '--...','8': '---..','9': '----.'
}
symbols = {
    '.': '.-.-.-',',': '--..--','?': '..--..',
    '\'': '.----.','!': '-.-.--','/': '-..-.',
    '(': '-.--.',')': '-.--.-','&': '.-...',
    ':': '---...',';': '-.-.-.','=': '-...-',
    '+': '.-.-.','-': '-....-','_': '..--.-',
    '"': '.-..-.','$': '...-..-','@': '.--.-.'
}
type_prompt = """\nChoose type:
    1. English to Morse
    2. Morse to English
Your choice: """
difficulty_prompt ="""\nChoose difficulty:
    1. Easy (only letters)
    2. Medium (letters & digits)
    3. Hard (everything)
    4. Symbols
    5. Master (sentences)
Your choice: """
mode_prompt = """\nChoose mode:
    1. Random
    2. Sound
    3. Light
    4. Text
Your choice: """
guess = ''
answer = ''
morse = ''
type = ' '
difficulty = ' '
mode = ' '

def beep(freq,duration):
    winsound.Beep(freq, duration)

def blink(duration):
    root.deiconify()
    root.update()
    time.sleep(duration)
    root.withdraw()
    root.update()
    time.sleep(0.6)

while (type := input(type_prompt)) not in list('12'):
        print("\nInvalid choice.\n")
while (difficulty := input(difficulty_prompt)) not in list('12345'):
        print("\nInvalid choice.\n")

if difficulty == '1':
    code = letters
elif difficulty == '2':
    code = letters
    code.update(digits)
elif difficulty == '3' or difficulty != '4' and difficulty == '5':
    code = everything
elif difficulty == '4':
    code = symbols
if type == '1':
    while 1:
        if difficulty == '5':
            text = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random").json()['data'][0]['quoteText']
        else:
            item = r.choice(list(code.items()))
            text = item[0]
        answer = ' '.join(code[x] for x in text.upper())
        print(text)
        guess = input('\nTranslate (use " / " as space): ')

        if guess.upper() == answer:
            print(f'\nCorrect! {text}({answer})\n')
        else:
            print(f'\nIncorect! It was: {text}({answer})\n')
        answer = ''

elif type == '2':
    while (mode := input(mode_prompt)) not in list('1234'):
        print("\nInvalid choice.\n")

    while 1:
        if difficulty == '5':
            answer = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random").json()['data'][0]['quoteText']
        else:
            item = r.choice(list(code.items()))
            answer = item[0]
        morse = ' '.join(code[x] for x in answer.upper())

        final_mode = r.choice(['2','3','4']) if mode == '1' else mode
        while guess == '':
            if final_mode == '2':
                winsound.Beep(37, 1000)
                for i in morse:
                    if i == '-':
                        beep(500, 600)
                    elif i == '.':
                        beep(500, 300)
                    else:
                        time.sleep(1)
            elif final_mode == '3':
                time.sleep(1)
                for i in morse:
                    if i == '-':
                        blink(0.8)
                    elif i == '.':
                        blink(0.3)
                    else:
                        time.sleep(1)
            elif final_mode == '4':
                print(morse)
            guess = input('Translate or press enter to try again: ')
                    # if guess != '':
                    #     break
        if guess.upper() == answer:
            print(f'\nCorrect! {morse}({answer})\n')
        else:
            print(f'\nIncorect! It was: {morse}({answer})\n')
        guess,morse = '',''