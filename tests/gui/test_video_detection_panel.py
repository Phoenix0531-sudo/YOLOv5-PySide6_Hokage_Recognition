from pathlib import Path

import pytest

from hokage_vision.ui.widgets.video_detection_panel import VideoDetectionPanel

pytestmark = pytest.mark.gui


def test_video_detection_panel_reports_missing_video_dependency(qtbot) -> None:
    panel = VideoDetectionPanel()
    qtbot.addWidget(panel)

    panel.detect_video(Path("examples/videos/missing.mp4"))

    assert "Video detection failed" in panel.status.text()
