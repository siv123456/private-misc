from PyQt4.QtGui import QDialog, QPalette, QFont, QLabel, QComboBox, \
    QLineEdit, QPushButton, QGridLayout, QColor, QIcon, QPixmap, QApplication, QStyleFactory
from PyQt4.QtCore import Qt, SIGNAL, QUrl

from defs import general_defs
from time import sleep
import subprocess


class View(QDialog):

    def __init__(self):

        super(View, self).__init__()
        hpalette = QPalette()  # Header Palette
        lpalette = QPalette()  # simple label Palette
        bpalette = QPalette()  # button Palette
        bgpalette = QPalette()  # background Palette
        apalette = QPalette()  # alert Palette

        hpalette.setColor(QPalette.WindowText, QColor("#6F3662") )  # Header Color

        lpalette.setColor(QPalette.WindowText, QColor("#74828F"))  # labels color
        lpalette.setColor(QPalette.Window, QColor("#DDDDDD"))  # labels color
        apalette.setColor(QPalette.WindowText, QColor("#FF0000"))  # alert text color
        bpalette.setColor(QPalette.ButtonText, QColor("#6F3662"))  # button text color
        bpalette.setColor(QPalette.Button, QColor("#6F3662"))      # button background color
        # bgpalette.setColor(QPalette.Window, QColor("#F8F8F8"))     # background color

        self.palettes = dict()
        self.palettes['header'] = hpalette
        self.palettes['button'] = bpalette
        self.palettes['label'] = lpalette
        self.palettes['support'] = lpalette
        self.palettes['note'] = lpalette
        self.palettes['alert'] = apalette
        self.palettes['bg'] = bgpalette

        self.label_types = dict()
        self.label_types['label'] = QFont(general_defs['_font'], general_defs['label_font_size'])
        self.label_types['button'] = QFont(general_defs['_font'], general_defs['button_font_size'])
        self.label_types['support'] = QFont(general_defs['_font'], general_defs['support_font_size'])
        self.label_types['alert'] = QFont(general_defs['_font'], general_defs['alert_font_size'])
        self.label_types['note'] = QFont(general_defs['_font'], general_defs['note_font_size'])
        self.label_types['header'] = QFont(general_defs['_font'], general_defs['header_font_size'], QFont.Bold)

    def create_button(self, btn_label, enabled = True):
        b = QPushButton(btn_label)
        b.setEnabled(enabled)
        b.setFont(self.label_types['button'])
        b.setPalette(self.palettes['button'])
        b.setAutoFillBackground(True)
        return b

    def create_qlabel(self, string_to_label, wtype='label'):
        # label_type can be label, button  or header, support, alert, note

        qlbl = QLabel(string_to_label)
        qlbl.setFont(self.label_types[wtype])
        qlbl.setPalette(self.palettes[wtype])
        if string_to_label == ".":
            qlbl.setFixedWidth(15)
        return qlbl

    def create_label_lineedit_pair(self, groupName):
        """
        This method is for creating a group like the one showing the router name
        Recognized automatically. used in ViewAuthForm and ViewRouterCredentials
        :param groupName: the
        :param password: is True when the field will hold a password
        :return: two horizontal labels and the second is styled
        """
        group = dict()
        group['label'] = self.create_qlabel(groupName)
        group['value'] = QLineEdit("")
        return group

class TimerGuiView(View):

    def __init__(self):
        super(TimerGuiView, self).__init__()


        # Header
        self.header_label = self.create_qlabel("Shutdown Timer App", 'header')
        # textbox to insert the time to shutdown
        self.time_group = self.create_label_lineedit_pair('time in minutes:')
        # Execute BTN
        self.exec_btn = self.create_button("GO")
        # Execute Now BTN
        self.exec_now_btn = self.create_button("Now")

        grid = QGridLayout()
        grid.addWidget(self.header_label, 0, 0, 2, 0, Qt.AlignCenter) # add Gui Header
        grid.addWidget(self.time_group['label'], 1, 0, Qt.AlignLeft) # add Text Box
        grid.addWidget(self.time_group['value'], 1, 1, Qt.AlignCenter) # add Text Box
        grid.addWidget(self.exec_btn, 2, 0,   Qt.AlignCenter) # add button
        grid.addWidget(self.exec_now_btn, 2, 1,  Qt.AlignCenter) # add button
        self.setLayout(grid)  # "close" grid

class TimerGuiCtrl:

    def __init__(self, view_obj):
        self.time2Shutdown = None
        self.ready = False
        self.view = view_obj

        # Signals Connect
        self.view.connect(self.view.exec_btn, SIGNAL("clicked ()"), self.count_down)
        self.view.connect(self.view.exec_now_btn, SIGNAL("clicked ()"), self.shutdown_now)

    def count_down(self):
        if not self.view.time_group['value'].text() == "":
            self.time2Shutdown = int(self.view.time_group['value'].text())
        else:
            self.time2Shutdown = 500

        if not self.time2Shutdown == None and self.time2Shutdown < 500:
            # print "counting down: " + str(self.time2Shutdown)
            self.ready = True

        self.view.accept()

    def shutdown_now(self):
        self.time2Shutdown = 0
        self.ready = True
        self.view.accept()

    def sleepTime(self):
        sleep(60 * self.time2Shutdown)

class Day2Day:

    def __init__(self):
        pass

    def restart(self):
        subprocess.call(["shutdown", "/r"])

    def logoff(self):
        subprocess.call(["shutdown", "/l"])

    def shutdown(self):
        subprocess.call(["shutdown", "/s"])

################### JUST SOME Functions
def create_app(arguments):

    app = QApplication(arguments)
    p = QPalette()
    p.setColor(QPalette.Window, QColor("#DDDDDD"))
    app.setPalette(p)
    keys = QStyleFactory.keys()
    # list of themes include:
    # ['Windows', 'WindowsXP', 'WindowsVista', 'Motif', 'CDE', 'Plastique', 'Cleanlooks']
    # i'm using WindowsXP
    app.setStyle(QStyleFactory.create(keys[1]))
    # app.setWindowIcon(get_qicon(general_defs['icon']))

    return app


