"""Emoji2Face 插件配置模型。"""

from __future__ import annotations

from typing import ClassVar

from maibot_sdk import Field, PluginConfigBase


class PluginSectionConfig(PluginConfigBase):
    """插件级基础配置。"""

    __ui_label__: ClassVar[str] = "基础设置"
    __ui_order__: ClassVar[int] = 0

    enabled: bool = Field(
        default=True,
        description="是否启用 Emoji 自动转 QQ 原生小黄脸表情功能。",
        json_schema_extra={
            "hint": "开启后，出站消息中的所有常见 Emoji（如 😂、😊、👍、🥺 等）会自动转换为原生的 QQ 动态小黄脸。",
            "label": "启用 Emoji 转换",
            "order": 0,
        },
    )
    config_version: str = Field(
        default="1.0.0",
        description="当前配置结构版本。",
        json_schema_extra={
            "disabled": True,
            "hidden": True,
            "label": "配置版本",
            "order": 99,
        },
    )


class Emoji2FaceConfig(PluginConfigBase):
    """Emoji2Face 插件主配置。"""

    plugin: PluginSectionConfig = Field(default_factory=PluginSectionConfig)
