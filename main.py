import math
import PySimpleGUI as sg

class Calcolatrice:#÷
    def __init__(self, size=None):
        if size is None:
            size = (400,300)
        self.size = size

    def GUI(self):
        layout = [
            #[ sg.Multiline(disabled=True, expand_x=True, border_width=0, no_scrollbar=True, font=("Helvetica", 36),key="-output-") ],
            [ sg.Input(expand_x=True, border_width=0, font=("Helvetica", 36),key="-output-") ],
            [ sg.Button("CE", expand_x=True, size=(3,1), key="-cls-"), sg.Button("←", expand_x=True, size=(3,1), key="-delete-") ],
            [ sg.Button("x²", expand_x=True, size=(3,1), key="-sqrtd-"),sg.Button("^", expand_x=True, size=(3,1)),sg.Button("√", expand_x=True, size=(3,1), key="-sqrt-"),sg.Button("÷", expand_x=True, size=(3,1)) ],
            [ sg.Button("1", expand_x=True , size=(3,1)),sg.Button("2", expand_x=True, size=(3,1)),sg.Button("3", expand_x=True, size=(3,1)),sg.Button("x", expand_x=True, size=(3,1)) ],
            [ sg.Button("4", expand_x=True , size=(3,1)),sg.Button("5", expand_x=True, size=(3,1)),sg.Button("6", expand_x=True, size=(3,1)),sg.Button("-", expand_x=True, size=(3,1)) ],
            [ sg.Button("7", expand_x=True , size=(3,1)),sg.Button("8", expand_x=True, size=(3,1)),sg.Button("9", expand_x=True, size=(3,1)),sg.Button("+", expand_x=True, size=(3,1)) ],
            [ sg.Button("0", expand_x=True, size=(3,1) ),sg.Button("=", expand_x=True, size=(3,1), key="-eq-") ],
        ]

        self.window = sg.Window(title="Calcolatrice", layout=layout, size=self.size)

        symbols = ["÷", "x", "-", "+"]

        while True:
            event, values = self.window.read()

            if event in ("exit", sg.WIN_CLOSED):
                break
            else:
                if event not in ( "-cls-", "-eq-"):
                    self.window["-output-"].update(values["-output-"]+event)

                if event == "-eq-":
                    self.window["-output-"].update(eval(values["-output-"].replace("x", "*").replace("÷", "/").replace("^", "**")))

                if event == "-sqrt-":
                    self.window["-output-"].update(eval(values["-output-"].replace("x", "*").replace("÷", "/").replace("^", "**")))
                    self.window["-output-"].update(math.sqrt(int(values["-output-"])))

                if event == "-sqrtd-":
                    self.window["-output-"].update(eval(values["-output-"].replace("x", "*").replace("÷", "/").replace("^", "**")))
                    self.window["-output-"].update(int(values["-output-"])**2)

                if event == "-delete-":
                    self.window["-output-"].update(values["-output-"][1:])

                if event == "-cls-":
                    self.window["-output-"].update("")

        self.window.close()


Calcolatrice().GUI()
