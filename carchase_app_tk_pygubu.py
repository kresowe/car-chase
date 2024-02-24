import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import pathlib

proj_path = pathlib.Path(__file__).parent
proj_ui = proj_path / "carchase.ui"


class CarChaseAppTkPyGubu:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_path(proj_path)
        self.builder.add_from_file(proj_ui)
        self.mainwindow = self.builder.get_object('main_window', master)
        self.builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_start_clicked(self):
        print(self.builder.get_variable('c1_x0').get())


if __name__ == '__main__':
    app = CarChaseAppTkPyGubu()
    app.run()