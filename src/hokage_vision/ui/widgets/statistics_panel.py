from __future__ import annotations

from collections import Counter

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from hokage_vision.core.types import DetectionResult


class StatisticsPanel(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.summary = QLabel("No detections")
        layout = QVBoxLayout(self)
        layout.addWidget(self.summary)

    def set_result(self, result: DetectionResult) -> None:
        counts = Counter(detection.label for detection in result.detections)
        average = (
            sum(detection.confidence for detection in result.detections) / len(result.detections)
            if result.detections
            else 0
        )
        self.summary.setText(f"Classes: {dict(counts)} | Average confidence: {average:.2f}")
