import openpyxl
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from ui import ui_main_window
from datetime import datetime
import threading
import time
from dialog import Dialog


class MainWindow:
    path = None
    wins = 0
    losses = 0
    wb = None
    dialog = None
    mandando = False

    def __init__(self):
        with open("excelpath.txt", "r") as f:
            self.path = f.readline().strip()

        # Setup window
        self.this_window = QMainWindow()
        self.ui = ui_main_window.Ui_MainWindow()
        self.ui.setupUi(self.this_window)

        # center
        frame_geometry = self.this_window.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.this_window.move(frame_geometry.topLeft())

        # Show or exec
        self.this_window.show()

        # conectar signals a slot
        self.ui.btn_loss_minus.clicked.connect(self.on_btn_loss_minus_clicked)
        self.ui.btn_loss_plus.clicked.connect(self.on_btn_loss_plus_clicked)
        self.ui.btn_wins_minus.clicked.connect(self.on_btn_wins_minus_clicked)
        self.ui.btn_wins_plus.clicked.connect(self.on_btn_wins_plus_clicked)
        self.ui.btn_excel.clicked.connect(self.on_btn_excel_clicked)
        self.ui.btn_stats.clicked.connect(self.on_btn_stats_clicked)

    def thread_reset_btn_name(self):
        time.sleep(3)
        self.ui.btn_excel.setText("MANDAR AL EXCEL")
        self.mandando = False

    # definir funciones de slots
    def on_btn_loss_minus_clicked(self):
        self.losses -= 1
        if self.losses < 0:
            self.losses = 0
        self.set_lbl_loss()

    def on_btn_loss_plus_clicked(self):
        self.losses += 1
        self.set_lbl_loss()

    def on_btn_wins_minus_clicked(self):
        self.wins -= 1
        if self.wins < 0:
            self.wins = 0
        self.set_lbl_wins()

    def on_btn_wins_plus_clicked(self):
        self.wins += 1
        self.set_lbl_wins()

    def set_lbl_loss(self):
        self.ui.lbl_loss.setText(f"Losses : {self.losses}")

    def set_lbl_wins(self):
        self.ui.lbl_wins.setText(f"Wins : {self.wins}")

    def on_btn_excel_clicked(self):
        if not self.mandando:
            if self.wb is None:
                try:
                    self.wb = openpyxl.load_workbook(filename=self.path)
                except FileNotFoundError:
                    self.wb = openpyxl.Workbook()

                    self.wb.active.append(["Fecha y hora", "P", "W", "L"])

            today = datetime.today()
            fechahora = today.strftime('%d-%m-%Y %H:%M')
            row = (fechahora, self.wins + self.losses, self.wins, self.losses)

            self.wb.active.append(row)
            self.wb.save(self.path)
            self.mandando = True
            self.ui.btn_excel.setText("ENVIADO!")
            t1 = threading.Thread(target=self.thread_reset_btn_name)
            t1.start()

    def on_btn_stats_clicked(self):
        self.dialog = Dialog(self.path)
