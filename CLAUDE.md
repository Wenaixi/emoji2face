# emoji2face 记忆库

## 插件基本信息
- 插件 ID：`emoji2face`
- 官方作者：Wenaixi (https://github.com/Wenaixi)
- 性质：自研独立原生插件，无任何外部上游依赖
- 核心功能：通过 `send_service.before_send` Hook 拦截出站消息段，自动将 Unicode Emoji 切分为 QQ 原生小黄脸段
- 适配器要求：搭配官方原版纯净 `MaiBot-Napcat-Adapter` 即可完美运作
