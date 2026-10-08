# 私有接口契约 v1

API 根路径 `/api/create/aerospace`，除 GET `/capabilities` 外均需平台现有 Bearer 会话。不要创建或公开新访问密钥。

- POST `/briefs`：`brand`（1–32 字）、`industry`（satellite / rocket）、`holiday`（space_day / mid_autumn / national_day / new_year / spring_festival）、`rights_confirmed: true`、`idempotency_key`（8–100 位字母数字下划线短横线）；可选 `image_base64` 为纯 base64 PNG，正规化后不超过 2 MB。前端可将 JPEG 转为 PNG。只有用户已有授权才将 rights_confirmed 设为 true。
- GET `/briefs`：账户自己的最近 30 份资料。
- GET `/briefs/{id}`：企业资料、三个 `options`（含 SVG）及关联 `jobs`。
- GET `/briefs/{id}/svg?variant=orbit`：私有 SVG。方案值为 orbit / editorial / celebration。
- POST `/briefs/{id}/render`：仅 `{ "variant": "orbit" }`。同一账户、资料、方案去重。失败后重复调用为明确重试，最多三个尝试。
- GET `/jobs/{id}`：queued / running / completed / failed；`error` 为客户可读失败信息，`receipt` 为实际导出证据。
- GET `/jobs/{id}/poster.png`、`/motion.mp4`：完成后鉴权下载，不是公共链接。

首版为固定 16:9 模板与 6 秒无声轻动效，不含模型生图、复杂视频生成、品牌视觉规范自动识别、多尺寸或自动发布。未提供企业实拍则使用概念图形。

`receipt.files` 提供 sha256 与 bytes。服务端验证实际 PNG 格式、尺寸和 MP4 探测结果后才变更为 completed。页面刷新用 `?aerospace={brief_id}` 恢复；换账号后必须清除旧预览和对象 URL。
