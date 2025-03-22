from collections import Counter
txt = 'texto de prueba'
def text_counter(txt : str):
    sentences = Counter(txt)['.']
    txt = ''.join(txt.split('.')).split(' ')
    total_letter = len(''.join(txt))
    total_word = len(txt)
    max_word = ''
    for word in txt:
        if len(word) > len(max_word):
            max_word = word
    print(f'el numero de oraciones es: {sentences}\nla longitud media es: {total_letter//total_word}\nla palabra mas larga es: {max_word} ')
