import model, view;

def start():
    while True:
        dr = view.data_request()
        if dr == 0:
                model.create_note()
        elif dr == 1:
             return dr
        elif dr == 2:
            return dr
        elif dr == 3:
            return dr
        elif dr == 5:
                 break