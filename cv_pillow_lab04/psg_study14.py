import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox


layout = [
    [psg.ProgressBar(max_value=1000, orientation="h", size=(20,20), key="-PROG-")],
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("Progress 테스트", layout, )

for i in range(1000):
    event, values = window.read(timeout=1)
    if event == "Cancel" or event == psg.WIN_CLOSED:
        break
    window['-PROG-'].UpdateBar(i+1)
window.close()
print(event, values)

