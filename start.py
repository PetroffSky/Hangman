import PySimpleGUI as sg
import help, options, engine
import string
from importlib import reload


class GuiGame:
    """ Интерфейс игры. Старт программы и приветствие"""
    def __init__(self, open_let=0, len_word=(), name='не выбран', letter=''):
        self.name = name
        # self.diff = diff
        self.len_word = len_word
        self.open_let = open_let
        self.letter = letter

    @classmethod
    def __str__(cls):
        return 'Для начала новой игры выберите сложность игры и нажмите Start'


    @staticmethod
    def callback_no():
        # print('Exit')
        layouts = [[sg.Text('Вы хотите покинуть игру')],
                   [sg.Button('Yes'), sg.Button('No')]]

        pop_win = sg.Window('Выход из игры', layouts)

        while True:  # Event Loop
            events, value = pop_win.read()
            if events == sg.WIN_CLOSED:
                break
            elif events == 'No':
                pop_win.close()
                print('Приятной игры!')
                break
            elif events == 'Yes':
                pop_win.close()
                return 'close'  # call the "Callback" function
        pop_win.close()

    @staticmethod
    def callback_help():
        print(help.Help.__str__())


if __name__ == '__main__':
    layout = [[sg.Multiline(GuiGame.__str__(), size=(65, 20), font='Helvetica 10', \
                            reroute_stdout=True, reroute_stderr=True, autoscroll=True, \
                            enter_submits=False, key='-QUERY-', do_not_clear=True, disabled=True)],
              [sg.Text("Выбор сложности игры:"),
               sg.DropDown(values=('', 'лёгкая', 'средняя', 'сложная'), size=(20, 30), key='-DROP-', readonly=True),
               sg.Button('Start', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
               sg.Button('Exit', button_color=(sg.YELLOWS[0], sg.GREENS[0])),
               sg.Button('Help', button_color=(sg.YELLOWS[0], sg.GREENS[0]))],
              [sg.Text('Ввод букв:'),
               sg.Input(key='-INPUT-', do_not_clear=False, visible=True, disabled=True),   # Неактивность disabled окна для развития
               sg.OK(disabled=True)]]

    window = sg.Window(f'Угадайка!', layout, finalize=True)
    # Функция bind из TKinter обрабатывает нажатие клавиши enter на событие
    window['-INPUT-'].bind("<Return>", "_Enter")
    result = True  # Флаг для остановки игры по окончании
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Exit':
            if GuiGame.callback_no() == 'close':
                window.close()
                break
        elif event == 'Start':
            window['-INPUT-'].update(disabled=False)  # После старта активируется строка ввода
            window['OK'].update(disabled=False)  # Активируется отправка слова / буквы
            if values['-DROP-'] in ('лёгкая', 'средняя', 'сложная'):
                window['Start'].update(disabled=True)  # Инактивируется старт игры
                window['-DROP-'].update(disabled=True)  # Инактивируется возможность выбора сложности
                diff = values['-DROP-']
                len_word = options.res.game_difficulty(diff)
                print(f'\nВыбрана сложность: {diff}!')
                engine.a.randomizer(len_word)
                window['-DROP-'].update(values=('', 'лёгкая', 'средняя', 'сложная'))
            elif values['-DROP-'] == '':
                window['Start'].update(disabled=False)
                window['-INPUT-'].update(disabled=True)
                window['OK'].update(disabled=True)
                print('Сложность игры не выбрана! Выберите сложность.')
        elif event == 'Help':
            GuiGame.callback_help()
        elif event == 'OK' or event == '-INPUT-' + '_Enter':  # обработка отправки ответа с помощью Enter
            if len(values['-INPUT-']) < 1 or len(values['-INPUT-']) > 1:
                print('Ошибка! Ввести можно только 1 букву!')
            elif values['-INPUT-'] in string.ascii_letters:
                print('Ошибка! Ввести можно только кириллицу!')
            elif not values['-INPUT-'].isalpha():
                print(f'Ошибка! Введена не буква: {values["-INPUT-"]}!')
            elif values['-INPUT-'].isalpha():
                letter = values['-INPUT-'].upper()
                result = engine.a.target(letter)
                # print(result)
                if not result:
                    result = True
                    window['-INPUT-'].update(disabled=True)
                    window['OK'].update(disabled=True)
                    window['Start'].update(disabled=False)
                    window['-DROP-'].update(disabled=False)
                    reload(options)  # перезагружаем переменные в модуле options
                    reload(engine)  # перезагружаем переменные в модуле engine

    window.close()
