import model, view, import_Export_File;

def start():
    while True:
        dr = view.data_request()
        if dr == 0:
            model.create_note()
        elif dr == 1:
            model.print_notebook_json()
        elif dr == 2:
            return dr
        elif dr == 3:
            return dr
        elif dr == 4:
            model.print_notebook_history()
        elif dr == 5:
                 break
#end start