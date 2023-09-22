from tkinter import *
from tkinter import ttk
import random
from copy import deepcopy
from logic import total, show_cards, get_winner, player_turn, croupier_turn
from config import ICON_PATH, BACK_BUTTON_PATH, STAT_PATH

#/////////////////////////////ВЗЯТО ИЗ LOGIC.PY//////////////////////////
hearts = {
    "2_h": 2,
    "3_h": 3,
    "4_h": 4,
    "5_h": 5,
    "6_h": 6,
    "7_h": 7,
    "8_h": 8,
    "9_h": 9,
    "10_h": 10,
    "J_h": 10,
    "Q_h": 10,
    "K_h": 10,
    "A_h": 11 
}

diamonds = {
    "2_d": 2,
    "3_d": 3,
    "4_d": 4,
    "5_d": 5,
    "6_d": 6,
    "7_d": 7,
    "8_d": 8,
    "9_d": 9,
    "10_d": 10,
    "J_d": 10,
    "Q_d": 10,
    "K_d": 10,
    "A_d": 11 
}

spades = {
    "2_s": 2,
    "3_s": 3,
    "4_s": 4,
    "5_s": 5,
    "6_s": 6,
    "7_s": 7,
    "8_s": 8,
    "9_s": 9,
    "10_s": 10,
    "J_s": 10,
    "Q_s": 10,
    "K_s": 10,
    "A_s": 11 
}

clubs = {
    "2_c": 2,
    "3_c": 3,
    "4_c": 4,
    "5_c": 5,
    "6_c": 6,
    "7_c": 7,
    "8_c": 8,
    "9_c": 9,
    "10_c": 10,
    "J_c": 10,
    "Q_c": 10,
    "K_c": 10,
    "A_c": 11 
}

#Информация о всех картах
info = {}
info.update(hearts)
info.update(diamonds)
info.update(clubs)
info.update(spades)

#Непосредственно сами карты
all_cards = []
for m in [hearts, diamonds, spades, clubs]:
    all_cards.extend(m.keys())
#///////////////////////////////////////////////////////////////////////////////



class Window(Tk):
    def __init__(self):
        super().__init__()

        #конфигурация окна
        self.title("Game")
        self.geometry("900x600+300+100")

        #кнопка закрытия
        photo = PhotoImage(file=BACK_BUTTON_PATH)
        self.button = ttk.Button(self, text="Выйти из игры!")
        self.button["command"] = self.go_back
        self.button.pack(anchor="sw")
    
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

def start_game():
    ans = 'y'
    while ans != 'n':
        game()
        print("Начать новую игру? [y/n]")
        ans = input()
        while (ans!='y' and ans!='n'):
            print("Повторите ввод")
            ans = input()

def game():
    game_widget = Window()
    game_widget["bg"] = "green"

    #Тасовка карт
    random.shuffle(all_cards)
    cards = deepcopy(all_cards)

    #Раздаем начальные карты
    player = [cards[0], cards[1]]
    croupier = [cards[2], cards[3]]
    for i in range(4):
        cards.pop(0)
    
    player_tot = total(player)
    croupier_tot = total(croupier)

    #Передаем ход игроку
    player, player_tot, player_took = player_turn(player, cards)
    if player_took ==-1:
        print("Сумма: ", player_tot)
        print("Вы проиграли!")
        return
    
    #Удаляем из колоды карты, которые взял игрок
    for _ in range(player_took):
        cards.pop(0)
    
    #Передаем ход крупье
    croupier, croupier_tot, croupier_took = croupier_turn(croupier, cards)
    if croupier_took == -1:
        print("*************")
        show_cards(player)
        print("Сумма: ", player_tot)
        show_cards(croupier, False)
        print("Сумма: ", croupier_tot)
        print("*************")
        print("Вы выиграли")
        return
    for _ in range(croupier_took):
        cards.pop(0)

    print("*************")
    show_cards(player)
    print("Сумма: ", player_tot)
    show_cards(croupier, False)
    print("Сумма: ", croupier_tot)
    print("*************")

    get_winner(player_tot, croupier_tot)




def main():

    #Управление на главном окне
    frame_main = ttk.Frame(borderwidth=1, relief=SOLID)
    button_start = ttk.Button(frame_main, text="Новая игра", command = start_game, width=50)
    button_continue = ttk.Button(frame_main, text="Продолжить игру", width=50)
    button_stat = ttk.Button(frame_main, text="Статистика", command = show_stat, width=50)
    button_start.pack(fill=X, ipadx=10, ipady=10)
    button_continue.pack(fill=X, ipadx=10, ipady=10)
    button_stat.pack(fill=X, ipadx=10, ipady=10)

    #frame_main.place(x=300, y=232, height=136, width=300)
    frame_main.pack(expand=True)

    widget.mainloop()
    #widget.protocol("WM_DELETE__WINDOW", finish)

if __name__ == "__main__":
    widget = Tk()
    widget.title("BlackJack")
    icon = PhotoImage(file=ICON_PATH)
    widget.iconphoto(False, icon)
    widget.geometry("300x200")
    main()