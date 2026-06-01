LABELS = {
    "zh-CN": {
        "home": "概览",
        "image": "图片检测",
        "video": "视频检测",
        "batch": "批量检测",
        "agent": "Agent 助手",
        "settings": "设置",
        "about": "关于",
    },
    "en-US": {
        "home": "Overview",
        "image": "Image Detection",
        "video": "Video Detection",
        "batch": "Batch Detection",
        "agent": "Agent Assistant",
        "settings": "Settings",
        "about": "About",
    },
}


def label(key: str, language: str = "zh-CN") -> str:
    return LABELS.get(language, LABELS["zh-CN"]).get(key, key)
