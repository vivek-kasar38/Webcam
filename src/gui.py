from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
import sys
import threading
import schedule
import time
from capture_photo import capture_photo

class WebcamApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.save_dir = None

    def initUI(self):
        self.setWindowTitle("Webcam Memory App")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Click to start capturing", self)
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.start_capturing)

        self.choose_dir_button = QPushButton("Choose Save Directory", self)
        self.choose_dir_button.clicked.connect(self.choose_directory)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.choose_dir_button)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def choose_directory(self):
        self.save_dir = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.save_dir:
            self.label.setText(f"Save Directory: {self.save_dir}")

    def start_capturing(self):
        if not self.save_dir:
            self.label.setText("Please choose a save directory first.")
            return
        self.label.setText("Capturing photos every 10 seconds...")
        self.hide()  # Minimize the dialog box
        schedule.every(10).seconds.do(lambda: capture_photo(self.save_dir))
        thread = threading.Thread(target=self.run_scheduler, daemon=True)
        thread.start()

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

app = QApplication(sys.argv)
window = WebcamApp()
window.show()
sys.exit(app.exec())