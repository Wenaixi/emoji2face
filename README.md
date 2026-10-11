# Emoji 转 QQ 表情插件 (emoji2face)

MaiBot 纯原生独立扩展插件。通过系统级出站发送拦截钩子（`send_service.before_send`），全自动、无感地将机器人出站消息中的 Unicode Emoji 转换为 QQ 官方动态小黄脸表情段。

## 架构与核心特性

- 100% 官方适配器解耦：完全不修改 `MaiBot-Napcat-Adapter` 的任何代码，适配器保持 100% 官方原汁原味。
- 全量表情权威覆盖：内置 193+ 项官方 QQ 小黄脸 ID 映射，覆盖喜怒哀乐、动物手势、日常美食与活动符号。
- 无上限全量转换：单条消息内出现的表情全数转换为小黄脸，无表情数量截断。
- 零侵入即插即用：无需复杂配置，插件启用即生效，关闭即恢复纯文本。

## 配置指南

```toml
[plugin]
enabled = true          # 是否启用 Emoji 转 QQ 小黄脸功能
config_version = "1.0.0"
```

## 开源协议

本项目采用 MIT 许可证开源，详情请参阅 [LICENSE](LICENSE)。
