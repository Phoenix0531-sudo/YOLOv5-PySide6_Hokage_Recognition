from pathlib import Path

import pytest

from hokage_vision.ui.widgets.batch_detection_panel import BatchDetectionPanel

pytestmark = pytest.mark.gui


def test_batch_detection_panel_detects_sample_folder(qtbot) -> None:
    panel = BatchDetectionPanel()
    qtbot.addWidget(panel)

    results = panel.detect_folder(Path("examples/images"))

    assert len(results) == 1
    assert panel.table.rowCount() == 3
    assert "Success: 1" in panel.summary.text()
