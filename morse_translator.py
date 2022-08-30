code = {
    'A': ['.-'],'B': ['-...'],'C': ['-.-.'],
    'D': ['-..'],'E': ['.'],'F': ['..-.'],
    'G': ['--.'],'H': ['....'],'I': ['..'],
    'J': ['-.-'],'K': ['-.-'],'L': ['.-..'],
    'M': ['--'],'N': ['-.'],'O': ['---'],
    'P': ['.--.'],'Q': ['--.-'],'R': ['.-.'],
    'S': ['...'],'T': ['-'],'U': ['..-'],
    'V': ['...-'],'W': ['.--'],'X': ['-..-'],
    'Y': ['-.--'],'Z': ['--..'],'0': ['-----'],
    
    '1': ['.----'],'2': ['..---'],'3': ['...--'],
    '4': ['....-'],'5': ['.....'],'6': ['-....'],
    '7': ['--...'],'8': ['---..'],'9': ['----.'],
    
    '.': ['.-.-.-'],',': ['--..--'],'?': ['..--..'],
    '\'': ['.----.'],'!': ['-.-.--'],'/': ['-..-.'],
    '(': ['-.--.'],')': ['-.--.-'],'&': ['.-...'],
    ':': ['---...'],';': ['-.-.-.'],'=': ['-...-'],
    '+': ['.-.-.'],'-': ['-....-'],'_': ['..--.-'],
    '"': ['.-..-.'],'$': ['...-..-'],'@': ['.--.-.'],
    ' ': ['','_']
}
mode_prompt = """Choose mode: 
    1. English to Morse
    2. Morse to English
Your choice: """
while (mode := input(mode_prompt)) not in list('12'):
    print("\nInvalid choice.\n")
while 1:
    if mode == '1':
        text = input("Enter text: ")
        for letter in text:
            print(code[letter.upper()][0], end=' ')
    elif mode == '2':
        morse = input("Enter morse code: ")
        for letter in morse.replace('  ',' / ').split(' '):
            for key, value in code.items():
                if value[-1] == letter:
                    print(key, end='')
    print()