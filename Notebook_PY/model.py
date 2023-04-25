import view;
import import_Export_File;
from datetime import datetime;
from time import time;
import json;

data_dateTime = []
data_tema = []
notebook = {}
note={}


def create_note():
    #получение данных
    tema = input("Тема: ")
    textNote = input("Текст заметки: ")
    time = datetime.now().strftime('%d.%m.%Y %H-%M-%S')   
    
    #запись для показа одной созданной заметки.
    note.clear()
    note[time]={tema: textNote}
       
    #запись заметок в общий список для показа истории в этом сеансе.
    notebook[time]={tema:textNote} 
    print("\nВы создали заметку: \n")    
    print_note(note)

    #запрос на сохраение
    print("\nВы хотите её сохранить в файл?\n")
    import_Export_File.import_json(note)    
    return notebook
#end create_note

#Вывод в консоль заметок.
def print_note(dic):
    for k, v in dic.items():
        print(k, v)
#end print_note

#Вывод в консоль истории ввода всех заметок этой сесии программы записанных и не замисанных в файл.
def print_notebook_history():
    print("\nИстория вводов: ")
    print_note(notebook)
#end print_notebook_history

#Вывод в консоль всех заметок сохраненых в файл.
def print_notebook_json():
    notebook_data = import_Export_File.export_json()
    print(json.dumps(notebook_data,
        sort_keys=False,
        indent=1,
        ensure_ascii=False,
        separators=(',', ': ')))
#end print_notebook_json