from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from hokage_vision.ui.main_window import MainWindow


def run_app() -> int:
    app = QApplication.instance() or QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()
