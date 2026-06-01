from __future__ import annotations

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from hokage_vision.core.types import DetectionResult


class ResultTable(QTableWidget):
    def __init__(self) -> None:
        super().__init__(0, 6)
        self.setHorizontalHeaderLabels(["Label", "Confidence", "x1", "y1", "x2", "y2"])

    def set_result(self, result: DetectionResult) -> None:
        self.setRowCount(len(result.detections))
        for row, detection in enumerate(result.detections):
            values = [
                detection.label,
                f"{detection.confidence:.2f}",
                f"{detection.box.x1:.1f}",
                f"{detection.box.y1:.1f}",
                f"{detection.box.x2:.1f}",
                f"{detection.box.y2:.1f}",
            ]
            for column, value in enumerate(values):
                self.setItem(row, column, QTableWidgetItem(value))
