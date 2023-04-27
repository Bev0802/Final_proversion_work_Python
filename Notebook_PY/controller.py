import model, view; 
import import_Export_File as ie_file;

def start():
    while True:
        dr = view.data_request()
        if dr == 0:
            model.create_note()
        elif dr == 1:
            model.print_dir()
        elif dr == 2:            
            model.search_date()
        elif dr == 3:
            model.search_date()
        elif dr == 4:
            model.print_notebook_history()
        elif dr == 5:
            break
#end start