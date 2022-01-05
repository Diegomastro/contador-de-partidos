from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QDialog
from ui import ui_dialog
import openpyxl


class Dialog:
    wb = None

    def __init__(self, path):
        self.path = path
        # Setup window
        self.this_window = QDialog()
        self.ui = ui_dialog.Ui_Dialog()
        self.ui.setupUi(self.this_window)

        # center
        frame_geometry = self.this_window.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.this_window.move(frame_geometry.topLeft())

        self.populate_labels()

        # Show or exec
        self.this_window.show()

    def populate_labels(self):
        if self.wb is None:
            self.wb = openpyxl.load_workbook(self.path, data_only=True)

        cells_dates = self.wb.active['A']
        cells_plays = self.wb.active['B']
        cells_wins = self.wb.active['C']
        cells_losses = self.wb.active['D']

        # salteamos el header con [1:]
        dates = [cell.value for cell in cells_dates][1:]
        plays = [cell.value for cell in cells_plays][1:]
        wins = [cell.value for cell in cells_wins][1:]
        losses = [cell.value for cell in cells_losses][1:]

        self.ui.lbl_totalplays.setText(str(sum(plays)))
        self.ui.lbl_totalwins.setText(str(sum(wins)))
        self.ui.lbl_totallosses.setText(str(sum(losses)))

        self.ui.lbl_mostplayedday.setText(str(dates[plays.index(max(plays))]))
        self.ui.lbl_mostwinningday.setText(str(dates[wins.index(max(wins))]))
        self.ui.lbl_mostlosingday.setText(str(dates[losses.index(max(losses))]))

        self.ui.lbl_mostplaysinonesession.setText(str(max(plays)))
        self.ui.lbl_mostwinsinonesession.setText(str(max(wins)))
        self.ui.lbl_mostlossesinonesession.setText(str(max(losses)))

        self.ui.lbl_avgplayspersession.setText(str(sum(plays) / len(plays)).format("{:2d}"))
        self.ui.lbl_avgwinspersession.setText(str(sum(wins) / len(wins)).format("{:2d}"))
        self.ui.lbl_avglossespersession.setText(str(sum(losses) / len(losses)).format("{:2d}"))
