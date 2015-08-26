import sys
import main
import logging
from PyQt5.Qt import *


class RLStatTracker(QWidget):

    try:
        json = open('data.json', 'r')
    except FileNotFoundError:
        main.create_new_json()

    def __init__(self):
        super().__init__()

        # Creation of mainwindow
        self.empty_log()
        self.create_main_window()
        self.log('Program successfuly started', 'info')

    def create_main_window(self):
        # Creation of parts of mainwindow
        self.create_input()
        self.create_console()
        self.create_stats()

        # Miscellaneous window properties set
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("RLStatTracker")
        self.setWindowIcon(QIcon("icon.png"))

        # Actions
        exit_action = QAction(QIcon("exit.png"), "&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(qApp.quit)

        # Menubar
        menu_bar = QMenuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(exit_action)

        # Declaration of grid
        grid = QGridLayout()

        grid.setMenuBar(menu_bar)

        self.setLayout(grid)

        # Add group boxes to main window
        grid.addWidget(self.input, 0, 0)
        grid.addWidget(self.console, 0, 1)
        grid.addWidget(self.stats, 0, 2)

        # Display window
        self.show()

    def create_input(self):

        # Create groupbox
        self.input = QGroupBox("Input")
        self.input.setFixedWidth(220)

        # Grid creation
        grid = QGridLayout()
        grid.setOriginCorner(Qt.TopLeftCorner)
        self.input.setLayout(grid)
        columns = 0
        rows = 0

        for i in range(1, 31):
            label = QLabel("")
            grid.addWidget(label, columns, rows)
            if i % 3 == 0:
                columns += 1
                rows -= 2
            else:
                rows += 1

        # Widgets
        your_goals_label = QLabel('Your goals:')
        enemy_goals_label = QLabel('Enemy goals:')
        your_goals = QSpinBox()
        enemy_goals = QSpinBox()
        confirm_button = QPushButton("Confirm")

        # Add to grid
        grid.addWidget(your_goals_label, 0, 0)
        grid.addWidget(enemy_goals_label, 0, 2)
        grid.addWidget(your_goals, 1, 0)
        grid.addWidget(enemy_goals, 1, 2)
        grid.addWidget(confirm_button, 8, 1)

    def create_console(self):
        # Creation of groupbox
        self.console = QGroupBox("Console")
        self.console.setFixedWidth(200)

        # Creation of grid layout
        grid = QGridLayout()
        self.console.setLayout(grid)

        # Creation of console
        self.console_output = QTextEdit()

        # Logging


        # Add widget to grid
        grid.addWidget(self.console_output, 0, 3, 4, 1)
        grid.setColumnStretch(1, 10)
        grid.setColumnStretch(2, 20)

    def create_stats(self):
        self.stats = QGroupBox("Stats")
        grid = QGridLayout()
        self.stats.setLayout(grid)

        names = ['', 'All', '1v1', '2v2', '3v3', 'Wins', '', '', '', '', 'Loses', '', '', '', '', 'Winrate', '', '', '',
                 '', 'Goals scored', '', '', '',  '', 'Goals let in', '', '', '', '']

        positions = [(i,j) for i in range(6) for j in range(5)]

        for i, name in zip(positions, names):
            label = QLabel(name)
            grid.addWidget(label, *i)

    def log(self, message, kind):
        log_filename = 'latestlog.txt'
        logging.basicConfig(filename=log_filename, level=logging.DEBUG,)

        if kind == 'info':
            logging.info(message)
        elif kind == 'error':
            logging.error(message)

        f = open('latestlog.txt', 'r')
        self.console_data = f.read()
        self.console_output.setPlainText(self.console_data)
        f.close()

    def empty_log(self):
        file = open('latestlog.txt', 'w')
        file.write("")
        file.close()

app = QApplication(sys.argv)
RL = RLStatTracker()
sys.exit(app.exec())