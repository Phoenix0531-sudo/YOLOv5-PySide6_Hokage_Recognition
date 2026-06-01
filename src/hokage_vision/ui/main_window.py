from PySide6.QtWidgets import QLabel, QMainWindow, QTabWidget

from hokage_vision.ui.i18n import label
from hokage_vision.ui.theme import stylesheet
from hokage_vision.ui.widgets.agent_chat_panel import AgentChatPanel
from hokage_vision.ui.widgets.batch_detection_panel import BatchDetectionPanel
from hokage_vision.ui.widgets.image_detection_panel import ImageDetectionPanel
from hokage_vision.ui.widgets.settings_panel import SettingsPanel
from hokage_vision.ui.widgets.video_detection_panel import VideoDetectionPanel


class MainWindow(QMainWindow):
    def __init__(self, language: str = "zh-CN", theme: str = "dark") -> None:
        super().__init__()
        self.setWindowTitle("Hokage Vision Agent")
        self.resize(1280, 860)
        self.setStyleSheet(stylesheet(theme))
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.addTab(QLabel("Hokage Vision Agent\nMock backend ready."), label("home", language))
        self.tabs.addTab(ImageDetectionPanel(), label("image", language))
        self.tabs.addTab(VideoDetectionPanel(), label("video", language))
        self.tabs.addTab(BatchDetectionPanel(), label("batch", language))
        self.tabs.addTab(AgentChatPanel(), label("agent", language))
        self.tabs.addTab(SettingsPanel(), label("settings", language))
        self.tabs.addTab(QLabel("Fan-made research and portfolio project."), label("about", language))
