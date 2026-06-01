from PySide6.QtWidgets import QLabel, QProgressBar, QPushButton, QVBoxLayout, QWidget


class BatchDetectionPanel(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.progress = QProgressBar()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Batch folder detection"))
        layout.addWidget(QPushButton("Select Folder"))
        layout.addWidget(QPushButton("Start Batch Detection"))
        layout.addWidget(self.progress)
        layout.addWidget(QLabel("Reports are generated only when explicitly requested."))
