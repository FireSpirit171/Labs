from tkinter import *
from tkinter import ttk
from config import ICON_PATH, BACK_BUTTON_PATH, STAT_PATH

class Window(Toplevel):
    def __init__(self):
        super().__init__()

        #конфигурация окна
        self.title("Game")
        self.geometry("900x600+300+100")

        #кнопка закрытия
        photo = PhotoImage(file=BACK_BUTTON_PATH)
        self.button = ttk.Button(self, image=photo)
        self.button["command"] = self.go_back
        self.button.pack(expand=True)
    
    def go_back(self):
        self.destroy()

def finish():
    global widget
    widget.destroy()

def show_stat():    
    #Читаем 3 строки файла и присваиваем значения в переменные
    with open(STAT_PATH, 'r') as stat_file:
        info_numbers = []
        for line in stat_file.readlines():
            info_numbers.append(line.split(": ")[1])
    games, wons, percant = info_numbers
    good_open = True

    #Преобразование типов и печать об удачном/неудачном открытии
    try:
        games = int(games)
        wons = int(wons)
        percant = int(percant)
    except:
        good_open = False

    if good_open:
        print("Обработано")
        print(f"Количество игр: {games}\nПобед: {wons}\nПроцент побед: {percant}%") 
    else:
        print("Ошибка!")

def game():
    game_widget = Window()

def main():

    #Управление на главном окне
    frame_main = ttk.Frame(borderwidth=1, relief=SOLID)
    button_start = ttk.Button(frame_main, text="Новая игра", command = game, width=50)
    button_continue = ttk.Button(frame_main, text="Продолжить игру", width=50)
    button_stat = ttk.Button(frame_main, text="Статистика", command = show_stat, width=50)
    button_start.pack(fill=X, ipadx=10, ipady=10)
    button_continue.pack(fill=X, ipadx=10, ipady=10)
    button_stat.pack(fill=X, ipadx=10, ipady=10)

    #frame_main.place(x=300, y=232, height=136, width=300)
    frame_main.pack(expand=True)

    widget.mainloop()
    widget.protocol("WM_DELETE__WINDOW", finish)

if __name__ == "__main__":
    widget = Tk()
    widget.title("BlackJack")
    icon = PhotoImage(file=ICON_PATH)
    widget.iconphoto(False, icon)
    widget.geometry("300x200")
    main()