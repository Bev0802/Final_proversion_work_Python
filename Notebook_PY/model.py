import view;
import import_Export_File as iefile;
from datetime import datetime;
from time import time;
import json;

list_notebook_dateTime = []
list_notebook_tema = []
notebook = {}
note={}

def create_note():
    #получение данных
    tema = input("Тема: ")
    textNote = input("Текст заметки: ")
    time = datetime.now().strftime('%d.%m.%Y %H.%M.%S')   
    
    #запись для показа одной созданной заметки.
    note.clear()
    note[time]={tema: textNote}
       
    #запись заметок в общий список для показа истории в этом сеансе.
    notebook[time]={tema:textNote} 
    print("\nВы создали заметку: \n")    
    print_note(note)

    #запрос на сохраение
    print("\nВы хотите её сохранить в файл?\n")
    iefile.import_json(note)    
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

#Вывод в консоль всех заметок сохраненых в файл в формате json
def print_notebook_json():
    notebook_list_notebook = iefile.export_json()
    print(json.dumps(notebook_list_notebook,
        sort_keys=False,
        indent=1,
        ensure_ascii=False,
        separators=(',', ': ')))
#end print_notebook_json

#преобрзование в списка в справочник
def notebook_dir():
    notebook_list = iefile.export_json()
    notebook_dir={}   
    for note in notebook_list:
        notebook_dir.update(note)  
    return notebook_dir
#end notebook_dir

#Вывод в консоль всех заметок сохраненых в файл в формате справочника
def print_dir():    
    notebook_d = notebook_dir()
    for data, tema  in notebook_d.items():
        print(data, tema)
#end print_dir

#печать даты
def print_dir_d():
    notebook_d = notebook_dir()
    list_date_key=[]
    for date, tema in notebook_d.items():
        list_date_key.append(date)
        print(date)
    return list_date_key
#end print_dir_d


#редактирование заметки
def сhanging_note(key_data):
    notebook_dis=notebook_dir()   
    print("Введите данные: ")
    tema = input("Введите тему заметки, которую хотите изменить: ")
    textNote = input("Текст заметки: ")
    notebook_dis[key_data].clear()
    notebook_dis[key_data]={tema: textNote}

    print(f'Заметка изменена:\n {notebook_dis[key_data]}')

    #запрос на сохраение
    print("\nВы хотите её сохранить в файл?\n")
    answer= view.booton()
    if (answer.lower() =="Да".lower()):        
         iefile.creat_file(notebook_dis)    
    #############тест
    print_notebook_json()    
#end сhanging_note
  
#удаление
def deleting_note(key_data):
    notebook_dis=notebook_dir()
    print("Заметка удалена: ")
    notebook_dis.pop(key_data)
    #запрос на сохраение
    print("\nВы хотите сохранить изменения в файл?\n")
    answer= view.booton()
    if (answer.lower() =="Да".lower()):        
         iefile.creat_file(notebook_dis)    
    #############тест
    print_notebook_json()      
# end deleting_note  

#поиск заметки по дате
def search_date():            
    list_date_key = print_dir_d()
    notebook_dis = notebook_dir()        
    key_data = input("\nВведите дату на которую вы ходите посмотреть или отредактировать заметку: ")
    if (key_data in list_date_key):
        note=notebook_dis[key_data]
        print(note)  

        print("Вы хотите изменить заметку?")
        answer= view.booton()
        if (answer.lower() =="Да".lower()):
            сhanging_note(key_data)
        else: 
            print("Может вы хотите удалить заметку?")
            answer= view.booton()
            if (answer.lower() =="Да".lower()):
                deleting_note(key_data) 
            else: print("Удачи!!!")
    else: 
        print("Дакой даты нет! Попробуйте с копипастить из списка дат. Он для этого и выводится. )))")
        search_date()
#end search_date 