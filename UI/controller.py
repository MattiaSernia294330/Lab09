import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._distanza=None

    def handleAnalizza(self,e):
        if self._distanza==None:
            self._view.window_alert("la distanza inseritra non va bene")
        self._model.creaGrafo(self._distanza)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"{self._model.numNodi}"))
        lista=self._model.Edge()
        self._view._txt_result.controls.append(ft.Text(f"{lista[2]}"))
        for i in range(len(lista[0])):
            self._view._txt_result.controls.append(ft.Text(f"Tratta {lista[0][i]} di distanza media : {lista[1][i]}"))
        self._view.update_page()

    def readDistanza(self,e):
        try:
            numero = float(e.control.value)
            self._distanza = numero
        except ValueError:
            self._distanza = None

