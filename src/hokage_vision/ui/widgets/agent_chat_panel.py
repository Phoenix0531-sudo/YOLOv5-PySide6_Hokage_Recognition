from __future__ import annotations

from PySide6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget

from hokage_vision.agents.providers.rule_based import RuleBasedAgent


class AgentChatPanel(QWidget):
    def __init__(self, agent: RuleBasedAgent | None = None) -> None:
        super().__init__()
        self.agent = agent or RuleBasedAgent()
        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.input = QLineEdit()
        self.input.setPlaceholderText("输入项目相关任务")
        self.run_button = QPushButton("Run Agent")
        self.run_button.clicked.connect(self.run_task)

        layout = QVBoxLayout(self)
        layout.addWidget(self.history)
        layout.addWidget(self.input)
        layout.addWidget(self.run_button)

    def run_task(self) -> None:
        task = self.input.text().strip()
        if not task:
            return
        response = self.agent.run(task)
        self.history.append(f"User: {task}")
        self.history.append(f"Agent: {response.message}")
