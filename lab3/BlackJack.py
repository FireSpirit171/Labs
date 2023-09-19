from tkinter import *
from tkinter import ttk
from config import ICON_PATH, STAT_PATH

def finish():
    pass

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

def main():
    widget = Tk()
    widget.title("BlackJack")
    icon = PhotoImage(file=ICON_PATH)
    widget.iconphoto(False, icon)
    widget.geometry("900x600+300+100")

    frame_main = ttk.Frame(borderwidth=1, relief=SOLID)
    button_start = ttk.Button(frame_main, text="Новая игра")
    button_continue = ttk.Button(frame_main, text="Продолжить игру")
    button_stat = ttk.Button(frame_main, text="Статистика", command = show_stat)
    button_start.pack()
    button_continue.pack()
    button_stat.pack()

    frame_main.pack(anchor=CENTER, fill=NONE)

    widget.mainloop()
    widget.protocol("WM_DELETE__WINDOW", finish)

if __name__ == "__main__":
    main()