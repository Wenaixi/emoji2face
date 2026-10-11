"""Emoji 转 QQ 表情 (Emoji to Face) 核心插件。"""

from __future__ import annotations

from typing import Any, Dict

from maibot_sdk import HookHandler, MaiBotPlugin

from .config import Emoji2FaceConfig
from .converter import convert_message_segments


class Emoji2FacePlugin(MaiBotPlugin):
    """自动将出站文本中的 Emoji 转换为 QQ 原生小黄脸表情段的独立插件。"""

    config_model = Emoji2FaceConfig

    async def on_load(self) -> None:
        """插件加载生命周期。"""
        self.ctx.logger.info("Emoji 转 QQ 表情插件已成功加载")

    async def on_unload(self) -> None:
        """插件卸载生命周期。"""
        pass

    async def on_config_update(self, scope: str, config_data: dict, version: str) -> None:
        """配置热更新生命周期。"""
        pass

    @HookHandler(
        "send_service.before_send",
        name="convert_emoji_to_qq_face",
        description="出站发送前将 Unicode Emoji 转换为 QQ 原生小黄脸表情段",
    )
    async def on_before_send(self, **kwargs: Any) -> Dict[str, Any]:
        """出站发送前拦截改写消息段。"""
        if not getattr(self.config.plugin, "enabled", True):
            return {"action": "continue", "modified_kwargs": kwargs}

        message_dict = kwargs.get("message")
        if not isinstance(message_dict, dict):
            return {"action": "continue", "modified_kwargs": kwargs}

        raw_message_data = message_dict.get("raw_message")
        if not isinstance(raw_message_data, list):
            return {"action": "continue", "modified_kwargs": kwargs}

        # 扫描并切分文本消息段
        new_segments = convert_message_segments(raw_message_data)
        if new_segments != raw_message_data:
            message_dict["raw_message"] = new_segments
            kwargs["message"] = message_dict

        return {"action": "continue", "modified_kwargs": kwargs}


def create_plugin() -> Emoji2FacePlugin:
    """创建并返回插件实例。"""
    return Emoji2FacePlugin()
