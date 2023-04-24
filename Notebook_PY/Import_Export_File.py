import json;
import model;
import view;

data = model.create_note()
answer = view.booton()

def import_json(data):
    if (answer=="Y"):
        with open('notebook.txt', 'w') as outfile:
                json.dump(data, outfile)
    else: 
        return print("После закрытия программы, не сохнаренные данные будут очищены.")