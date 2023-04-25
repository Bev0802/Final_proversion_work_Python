import view;
import json;
import os;

def import_json(data): #создание файла и запись заметок в файл   
    answer= view.booton()
    if (answer.lower() =="Да".lower()):
        if ((not(os.path.isfile("notebook.json"))) or (((os.stat("notebook.json")).st_size)==0)):
            json_data=[data]
            with open('notebook.json', 'w') as file:                               
                file.write(json.dumps(json_data, indent=1, ensure_ascii=False))
                                  
        else:
            json_data=json.load(open("notebook.json"))
            json_data.append(data)
            with open('notebook.json', 'w') as file:
                file.write(json.dumps(json_data, indent=1, ensure_ascii=False))
              
    else: 
        return print("\nПосле закрытия программы, не сохнаренные данные будут очищены.\n")
#end import_json

def export_json(): #импор заметок из файла
    notebook_data = json.load(open("notebook.json"))  # загружаем из файла данные       
    return notebook_data
#end export_json

