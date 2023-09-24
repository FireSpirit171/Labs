from tkinter import *
from tkinter import ttk
import random
from copy import deepcopy
from PIL import Image, ImageTk
from logic import total, show_cards, get_winner, player_turn, croupier_turn
from config import ICON_PATH, BACK_BUTTON_PATH, STAT_PATH, CARD_PATH

ACES = {"A_s", "A_h", "A_c", "A_d"}

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
    global widget
    hide_widgets()
    game()

def hide_widgets():
    global widget
    for child_widget in widget.winfo_children():
        child_widget.destroy()

def show_widgets():
    global widget
    for child_widget in widget.winfo_children():
        child_widget.pack()

def exit_game():
    global widget
    for w in widget.winfo_children():
        w.destroy()
    main()

all_images = []
num_cards_on_screen = 0
def show_card(path, X, Y = 480):
    global widget
    global all_images
    global num_cards_on_screen
    image_file = Image.open(path)
    vp_image = ImageTk.PhotoImage(image_file)
    all_images.append(vp_image)

    label = Label(image=all_images[num_cards_on_screen])
    num_cards_on_screen += 1
    label.place(x=X, y=Y)
    #widget.update()
    #widget.update_idletasks()

def sum_player(player):
    player_tot = total(player)
    correct = 0
    if player_tot>21:
        counter = 0
        for card in player:
            if card in ACES:
                counter+=1
        correct = 10*counter 
    return player_tot - correct

def take_card(player, cards):
    global widget
    player.append(cards[0])

    counter = 0
    for card in player:
        if card in ACES:
            counter+=1
    correct = 10*counter #Необходима для корректировки значения туза - 1 или 11

    show_card(CARD_PATH.format(cards.pop(0)), 240+len(player)*80)

    player_tot = total(player) - correct
    score = ttk.Label(widget, text=f"Сумма: {player_tot}", background="green", foreground="white", font=("Arial", 14))
    score.place(height=40, width=100, x=10, y=520)

    if player_tot>21:
        for w in widget.winfo_children():
            if type(w)==ttk.Button:
                w.destroy()
        end = ttk.Label(widget, text="Вы проиграли!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
        menu_button = ttk.Button(text="Меню", command=main)
        new_game_button = ttk.Button(text="Новая игра", command=game)
        
        menu_button.place(height=50, width=120, x=340, y=330)
        new_game_button.place(height=50, width=120, x=470, y=330)

def croupier_take(croupie, cards, player):
    global widget
    show_card(CARD_PATH.format(croupie[1]), 400, 10)
    player_tot = sum_player(player)
    for w in widget.winfo_children():
        if type(w)==ttk.Button:
            w.destroy()

    if len(set(croupie).intersection(ACES))==2:
        croupie_tot = 2
    else:
        croupie_tot = total(croupie)
    correct = 0

    while croupie_tot<17:
        croupie.append(cards[0])
        show_card(CARD_PATH.format(cards.pop(0)), 240+len(croupie)*80, 10)
        croupie_tot = total(croupie)
        if croupie_tot>21:
            counter = 0
            for card in croupie:
                if card in ACES:
                    counter+=1
            correct = 10*counter
        croupie_tot = total(croupie) - correct

    #После добора крупье считаем победителя
    if croupie_tot>21 or croupie_tot<player_tot:
        end = ttk.Label(widget, text="Вы выиграли!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
    elif croupie_tot==player_tot:
        end = ttk.Label(widget, text="Ничья!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
    else:
        end = ttk.Label(widget, text="Вы проиграли!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
    
    #Кнопки возврата в меню или начала новой игры
    menu_button = ttk.Button(text="Меню", command=main)
    new_game_button = ttk.Button(text="Новая игра", command=game)
    menu_button.place(height=50, width=120, x=340, y=330)
    new_game_button.place(height=50, width=120, x=470, y=330)


def game():
    global widget
    for w in widget.winfo_children():
        w.destroy()
    X = 320
    Y = 480

    back_button = ttk.Button(widget, text="Выйти из игры", command=exit_game)
    back_button.pack(anchor='nw')
    
    #Тасовка карт
    random.shuffle(all_cards)
    cards = deepcopy(all_cards)

    #Раздаем начальные карты
    player = [cards[0], cards[1]]
    croupier = [cards[2], cards[3]]
    for i in range(4):
        cards.pop(0)
    
    if len(set(player).intersection(ACES))==2:
        player_tot = 2
    else:
        player_tot = total(player)

    #Показываем начальные карты
    show_card(CARD_PATH.format(player[0]), X, Y)
    show_card(CARD_PATH.format(player[1]), X+80, Y)
    
    show_card(CARD_PATH.format(croupier[0]), X, Y-470)
    show_card(CARD_PATH.format("back"), X+80, Y-470)

    #Счет
    score = ttk.Label(widget, text=f"Сумма: {player_tot}", background="green", foreground="white", font=("Arial", 14))
    score.place(height=40, width=100, x=10, y=520)

    #Передаем ход игроку
    new_card_button = ttk.Button(widget, text="Ещё!", command=lambda pl = player, cs = cards: take_card(pl, cs))
    new_card_button.place(x=400, y=450)

    #Передаем ход крупье
    stop_card_button = ttk.Button(widget, text="Хватит", command=lambda cr = croupier, cs = cards, pl = player: croupier_take(cr, cs, pl))
    stop_card_button.place(x=500, y=450)


def main():
    for w in widget.winfo_children():
        w.destroy()
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
    widget["bg"] = "green"
    widget.title("BlackJack")
    icon = PhotoImage(file=ICON_PATH)
    widget.iconphoto(False, icon)
    widget.geometry("900x600+300+100")
    main()
