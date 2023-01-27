import model
import view


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_dp('C:\Python GB\DZ\Seminar7\PhoneBook\dataBase.txt')
            view.db_success(model.db_list)
        case 3:
            model.save_contact('C:\Python GB\DZ\Seminar7\PhoneBook\dataBase.txt')
        case 4:
            model.set_gb(view.create_newcontact())
        case 5:
            model.change_modul(view.change(), view.create_contact())            
        case 6:
            model.deleted_contact(view.del_cont())
        case 7:
            view.exit_program()




def start():
    while True:
        user_inp= view.show_menu()
        input_handler(user_inp)