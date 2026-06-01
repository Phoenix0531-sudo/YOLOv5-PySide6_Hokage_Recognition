from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, Signal

from hokage_vision.core.types import DetectionResult
from hokage_vision.vision.inference import InferenceService


class ImageDetectionWorker(QObject):
    finished = Signal(object)
    failed = Signal(str)

    def __init__(self, service: InferenceService, image_path: Path) -> None:
        super().__init__()
        self.service = service
        self.image_path = image_path

    def run(self) -> None:
        try:
            result: DetectionResult = self.service.detect_image(self.image_path)
        except Exception as exc:  # pragma: no cover
            self.failed.emit(str(exc))
            return
        self.finished.emit(result)
