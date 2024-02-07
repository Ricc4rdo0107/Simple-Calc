import math
import PySimpleGUI as sg

class Calcolatrice:#÷
    def __init__(self, size=None):
        if size is None:
            size = (400,300)
        self.size = size

    def GUI(self):
        layout = [
            [ sg.Input(expand_x=True, border_width=0, font=("Helvetica", 36),key="-output-") ],
            [ sg.Button("CE", expand_x=True, size=(3,1), key="-cls-"), sg.Button("←", expand_x=True, size=(3,1), key="-delete-") ],
            [ sg.Button("%", expand_x=True, size=(3,1)), sg.Button(",", expand_x=True, size=(3,1)), sg.Button("(", expand_x=True, size=(3,1)), sg.Button(")", expand_x=True, size=(3,1)) ],
            [ sg.Button("x²", expand_x=True, size=(3,1), key="-sqrtd-"),sg.Button("^", expand_x=True, size=(3,1)),sg.Button("√", expand_x=True, size=(3,1), key="-sqrt-"),sg.Button("÷", expand_x=True, size=(3,1)) ],
            [ sg.Button("1", expand_x=True , size=(3,1)),sg.Button("2", expand_x=True, size=(3,1)),sg.Button("3", expand_x=True, size=(3,1)),sg.Button("x", expand_x=True, size=(3,1)) ],
            [ sg.Button("4", expand_x=True , size=(3,1)),sg.Button("5", expand_x=True, size=(3,1)),sg.Button("6", expand_x=True, size=(3,1)),sg.Button("-", expand_x=True, size=(3,1)) ],
            [ sg.Button("7", expand_x=True , size=(3,1)),sg.Button("8", expand_x=True, size=(3,1)),sg.Button("9", expand_x=True, size=(3,1)),sg.Button("+", expand_x=True, size=(3,1)) ],
            [ sg.Button("0", expand_x=True, size=(3,1) ),sg.Button("=", expand_x=True, size=(3,1), key="-eq-") ],
        ]

        self.window = sg.Window(title="Calcolatrice", layout=layout, size=self.size)

        symbols = ["÷", "x", "-", "+"]
        keep_on_top = False
        while True:
            event, values = self.window.read()

            if event in ("exit", sg.WIN_CLOSED):
                break
            else:
                if event not in ( "-cls-", "-eq-"):
                    self.window["-output-"].update(values["-output-"]+event)
                try:
                    op = values["-output-"].replace("x", "*").replace("÷", "/").replace("^", "**").replace(",", ".")
                    if event == "-eq-":
                        self.window["-output-"].update(eval(op))

                    if event == "-sqrt-":
                        self.window["-output-"].update(eval(op))
                        self.window["-output-"].update(math.sqrt(int(values["-output-"])))

                    if event == "-sqrtd-":
                        self.window["-output-"].update(eval(op))
                        self.window["-output-"].update(int(values["-output-"])**2)

                except SyntaxError:
                    self.window["-output-"].update("Syntax Error")

                except NameError:
                    self.window["-output-"].update("Syntax Error")

                except Exception as e:
                    sg.popup_error(e)
                    print(op)

                if event == "-delete-":
                    self.window["-output-"].update(values["-output-"][:-1])

                if event == "-cls-":
                    self.window["-output-"].update("")

        self.window.close()


Calcolatrice().GUI()
