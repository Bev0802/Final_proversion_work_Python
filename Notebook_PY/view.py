dr_list=["0","1","2","3","4",'5',"6"]

def data_request():
    dr = (input(
            "\nМеню:\n" 
            "0 - Добавление новой заметки(тема, заметка).\n"
            "1 - Показать список заметок.\n"
            "2 - Поиск и редактирование заметки.\n"            
            "3 - Удалить заметку.\n"
            "4 - Показать историю записей в этом сеансе, в том числе не записанных в файл.\n"          
            "5 - Выход из программы.\n"
            "\nВведите номер действия, которое вы хотите совершить: "))
    if (dr in dr_list):
        return int(dr)             
    else:
        print("\n!!!!!!!!!! Вы ввели не верную команду. Пропробуйте еще !!!!!!!!!")
        data_request()
       
# end data_request

def booton():
    answer = input("Ответье: Да или Нет: ")
    return answer
# end booton