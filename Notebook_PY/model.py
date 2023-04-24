import view;
import Import_Export_File;
from datetime import datetime;
from time import time;

data_dateTime = []
data_tema = []
notebook = {}

def create_note():
    tema = input("Тема: ")
    textNote = input("Текст заметки: ")
    time = datetime.now().strftime('%d.%m.%Y %H-%M-%S')
    data_dateTime.append(time)
    data_tema.append(tema)
    notebook[time]={}   
    notebook[time][tema]=[]
    notebook[time][tema].append(textNote)
    print("Вы создали заметку: ")
    print_notebook()
    print("Вы хотите её сохранить в файл?")
    Import_Export_File(notebook)
    return notebook

def print_notebook():
    for time, tema in notebook.items():
        print(time, tema)
    
