import PySimpleGUI as sg
import webbrowser



def acwing():
    dict = {}
    with open('links.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            name = line[0:line.find(' ')]
            link = line[line.find(' ') + 1:len(line) - 2]
            dict[name] = link


    layout = [

        [sg.Text("题号:      "), sg.InputText(size=(10, 1)),
         sg.Button('输入'),
         sg.Button('转到'),
         sg.Button('退出')],
        [sg.Text('题目链接:'), sg.Input(size=(70, 1), key='-OUTPUT-', disabled=True, enable_events=True)],
    ]

    window = sg.Window('1281题之前', layout)

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        try:
            url = dict[value[0]]
        except KeyError:
            if event == '转到' or event == '输入':
                sg.popup('重新输入')
            else:
                break
        if event == '输入':
            try :
                window['-OUTPUT-'].update(url)
            except NameError:
                continue
        elif event == '转到':
            try :
                webbrowser.open(url)
            except NameError:
                continue
        else:
            break
    window.close()
