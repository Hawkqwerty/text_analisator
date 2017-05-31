# -*- coding: utf-8 -*-
"""
На входе: принимает название файла (в формате .txt) и язык анализируемого текста (англ\рус)
На выходе: файл со списком уникальных слов которые используются в файле (в формате .txt)

"""
import re
from stemming.porter2 import stem
from nltk.stem.snowball import RussianStemmer

d = {}
eng_pattern  = re.compile('[^a-zA-Z ]')
rus_pattern  = re.compile('[^а-яА-Я ]') 

def write_result (dic):
    
    file_n = input('Введите имя сохраняемого файла (или нажмите "Enter" для автоматического создания): ')
    if file_n:
        f = open(file_n, 'w')
    else:
        f = open('result({}).txt'.format(file_name), 'w')      
    f.write('--------------------------------------------------------------\n')
    f.write('Произведение содержит *{}* слова, из них @{}@ уникальные.'.format(sum(d.values()), len(d)))
    f.write('\n--------------------------------------------------------------\n\n')   
    number = 0
    for i in sorted(d):
        number += 1 
        f.write('{}. Слово "{}" и его формы встречается -{}- раз'.format(number, i, d[i]) + '\n')
    f.close()
    
while True:
    language = input('Введите язык файла (eng/rus): ')
    if language == 'eng' or language == 'rus':
        break
    else:
        print ('\nК сожалению, программа не поддерживает этот язык\nВведите "eng" для английского, или "rus" для русского')
file_name = input('Введите название файла для анализа: ')


try:
    with open(file_name, 'r') as f:
        for line in f:
            if language == 'eng':
                text_line = [stem(word) for word in eng_pattern.sub('', line).lower().split(' ')]
            elif language == 'rus':
                text_line = [RussianStemmer().stem(word) for word in rus_pattern.sub('', line).lower().split(' ')]
            for i in text_line:              
                if i in d:                
                    d [i] += 1
                else:
                    d [i] = 1
    del(d[''])
    write_result (d)
                      
except FileNotFoundError:
    print('Простите, но мы не можем найти файл с таким названием =(')

except:
    print('Упс, что-то пошло не так =(')
                 

    