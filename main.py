import clipboard
PER_alphabet = ["ض","ص","ث","ق","ف","غ","ع","ه","خ","ح","ج","چ","پ","ش","س","ی","ب","ل","ا","ت","ن","م","ک","گ","ظ","ط","ز","ژ","ر","ذ","د","پ","و","۱","۲","۳","۴","۵","۶","۷","۸","۹","۰","؟"]
ENG_alphabet = ["q","w","e","r","t","y","u","i","o","p","[","]","\\","a","s","d","f","g","h","j","k","l",";","'","z","x","c","C","v","b","n","m",",","1","2","3","4","5","6","7","8","9","0","?",]
text = clipboard.paste()
export=""
for i in text:
    if i in PER_alphabet:
        export=export+ENG_alphabet[PER_alphabet.index(i)]
    elif i in ENG_alphabet:
        export=export+PER_alphabet[ENG_alphabet.index(i)]
    else:
        export=export+i
clipboard.copy(export)