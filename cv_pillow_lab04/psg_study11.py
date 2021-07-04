import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import Checkbox

# 다시하기
menu = [
    ["&File", ["!&Open", "&Save", "---", "E&xit"]],
    ["&Edit", ["Copy", "Paste"]]
]

layout = [
    [psg.Menu(menu)],
    [psg.Ok(), psg.Cancel()]
]


window = psg.Window("메뉴 테스트", layout, size=(200,200))

event, values = window.read()
window.close()
print(event, values)

