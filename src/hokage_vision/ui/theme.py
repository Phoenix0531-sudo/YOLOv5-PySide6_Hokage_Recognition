DARK_STYLE = """
QWidget { background: #111827; color: #f3f4f6; font-size: 13px; }
QTabWidget::pane { border: 1px solid #374151; }
QPushButton { background: #2563eb; color: white; border: 0; padding: 8px 12px; border-radius: 4px; }
QPushButton:disabled { background: #4b5563; }
QLineEdit, QTextEdit, QPlainTextEdit, QComboBox, QDoubleSpinBox, QSpinBox {
  background: #1f2937; border: 1px solid #4b5563; padding: 6px; border-radius: 4px;
}
QTableWidget { background: #111827; gridline-color: #374151; }
"""

LIGHT_STYLE = """
QWidget { background: #f8fafc; color: #111827; font-size: 13px; }
QTabWidget::pane { border: 1px solid #cbd5e1; }
QPushButton { background: #2563eb; color: white; border: 0; padding: 8px 12px; border-radius: 4px; }
QLineEdit, QTextEdit, QPlainTextEdit, QComboBox, QDoubleSpinBox, QSpinBox {
  background: white; border: 1px solid #cbd5e1; padding: 6px; border-radius: 4px;
}
"""


def stylesheet(theme: str) -> str:
    return LIGHT_STYLE if theme == "light" else DARK_STYLE
