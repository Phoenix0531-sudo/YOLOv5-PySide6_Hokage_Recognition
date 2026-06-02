from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from hokage_vision.core.types import DetectionResult
from hokage_vision.ui.widgets.result_table import ResultTable
from hokage_vision.ui.widgets.statistics_panel import StatisticsPanel
from hokage_vision.vision.backends.mock import MockBackend
from hokage_vision.vision.inference import InferenceService


class VideoDetectionPanel(QWidget):
    def __init__(self, service: InferenceService | None = None) -> None:
        super().__init__()
        self.service = service or InferenceService(MockBackend())
        self.video_input = QLineEdit()
        self.video_input.setPlaceholderText("Select a local video file")
        self.frame_stride = QSpinBox()
        self.frame_stride.setRange(1, 1000)
        self.frame_stride.setValue(30)
        self.status = QLabel("Video detection uses local files; camera input is not supported.")
        self.table = ResultTable()
        self.stats = StatisticsPanel()
        self.select_button = QPushButton("Select Video")
        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        self.select_button.clicked.connect(self.select_video)
        self.start_button.clicked.connect(self.run_detection)
        self.pause_button.clicked.connect(lambda: self.status.setText("Paused."))
        self.stop_button.clicked.connect(lambda: self.status.setText("Stopped."))

        layout = QVBoxLayout(self)
        layout.addWidget(self.status)
        path_row = QHBoxLayout()
        path_row.addWidget(self.video_input)
        path_row.addWidget(self.select_button)
        layout.addLayout(path_row)
        controls = QHBoxLayout()
        controls.addWidget(QLabel("Frame stride"))
        controls.addWidget(self.frame_stride)
        controls.addWidget(self.start_button)
        controls.addWidget(self.pause_button)
        controls.addWidget(self.stop_button)
        layout.addLayout(controls)
        layout.addWidget(self.table)
        layout.addWidget(self.stats)

    def select_video(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Select video", "examples/videos", "Videos (*.mp4 *.mov *.avi)"
        )
        if path:
            self.video_input.setText(path)

    def run_detection(self) -> None:
        if not self.video_input.text().strip():
            self.status.setText("Select a video before starting.")
            return
        self.detect_video(Path(self.video_input.text()))

    def detect_video(self, video_path: Path) -> None:
        try:
            summary = self.service.detect_video(video_path, frame_stride=self.frame_stride.value())
        except Exception as exc:
            self.status.setText(f"Video detection failed: {exc}")
            return

        detections = [
            detection
            for frame_result in summary.detections_by_frame
            for detection in frame_result.detections
        ]
        aggregate = DetectionResult(source=str(video_path), detections=detections)
        self.table.set_result(aggregate)
        self.stats.set_result(aggregate)
        self.status.setText(
            f"Frames: {summary.frame_count} | Processed: {summary.processed_frames} | "
            f"FPS: {summary.fps or 0:.2f} | Detections: {len(detections)}"
        )
