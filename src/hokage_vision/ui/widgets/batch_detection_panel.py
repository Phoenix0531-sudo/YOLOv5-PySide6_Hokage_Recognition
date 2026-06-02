from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from hokage_vision.core.types import DetectionResult
from hokage_vision.ui.widgets.result_table import ResultTable
from hokage_vision.ui.widgets.statistics_panel import StatisticsPanel
from hokage_vision.vision.backends.mock import MockBackend
from hokage_vision.vision.inference import InferenceService


class BatchDetectionPanel(QWidget):
    def __init__(self, service: InferenceService | None = None) -> None:
        super().__init__()
        self.service = service or InferenceService(MockBackend())
        self.folder_input = QLineEdit("examples/images")
        self.progress = QProgressBar()
        self.summary = QLabel("Ready for batch detection.")
        self.table = ResultTable()
        self.stats = StatisticsPanel()
        self.select_button = QPushButton("Select Folder")
        self.start_button = QPushButton("Start Batch Detection")
        self.select_button.clicked.connect(self.select_folder)
        self.start_button.clicked.connect(self.run_detection)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Batch folder detection"))
        controls = QHBoxLayout()
        controls.addWidget(self.folder_input)
        controls.addWidget(self.select_button)
        controls.addWidget(self.start_button)
        layout.addLayout(controls)
        layout.addWidget(self.progress)
        layout.addWidget(self.summary)
        layout.addWidget(self.table)
        layout.addWidget(self.stats)
        layout.addWidget(QLabel("Reports are generated only when explicitly requested."))

    def select_folder(self) -> None:
        path = QFileDialog.getExistingDirectory(self, "Select folder", self.folder_input.text())
        if path:
            self.folder_input.setText(path)

    def run_detection(self) -> None:
        self.detect_folder(Path(self.folder_input.text()))

    def detect_folder(self, folder: Path) -> list[DetectionResult]:
        self.progress.setValue(0)
        try:
            results = self.service.detect_folder(
                folder,
                progress_callback=lambda done, total: self.progress.setValue(
                    int(done / total * 100) if total else 0
                ),
            )
        except Exception as exc:
            self.summary.setText(f"Batch detection failed: {exc}")
            return []

        success = [result for result in results if "error" not in result.metadata]
        failed = len(results) - len(success)
        detections = [detection for result in success for detection in result.detections]
        aggregate = DetectionResult(source=str(folder), detections=detections)
        self.table.set_result(aggregate)
        self.stats.set_result(aggregate)
        self.summary.setText(
            f"Images: {len(results)} | Success: {len(success)} | Failed: {failed} | "
            f"Detections: {len(detections)}"
        )
        return results
