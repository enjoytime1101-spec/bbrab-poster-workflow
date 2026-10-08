# 品牌交付 API / V7.19.0

所有请求使用现有账号鉴权；素材、档案、作品、下载均按所有者隔离。基础路径 `/api/create/aerospace`。

1. GET `/capabilities`，品牌导出须 `brand_render=true`；GET `/catalog` 读取当前真实范围。
2. GET `/assets`、`/companies` 复用已保存资料。POST `/assets`：`role` 为 product 或 logo，`industry` 为 satellite 或 rocket，`label`（32字内）、`source`（160字内）、`rights_confirmed:true`、PNG `image_base64`。产品长边≥1000、短边≥500；不接受外部素材 URL。响应 asset id。GET `/assets/{id}/image` 是私有图片。
3. POST `/companies`：`brand`（32字内）、`industry`、`color`（#RRGGBB）、`tagline`（40字内）、`blocked_words`（最多10项、每项16字）、`product_asset_id`、可选 `logo_asset_id`、`rights_confirmed:true`、`idempotency_key`。POST `/companies/{id}` 修改时带当前 `revision`；过期版本返回409。
4. POST `/briefs`：`company_id`、`revision`、`holiday:mid_autumn`、`idempotency_key`。返回3个含 SVG 的完整方案及 quality_report，资料、图片及版本冻结在作品中。一次请求后保存 brief id，轮询不重复提交图片。
5. 客户选择后 POST `/briefs/{id}/render`：`variant`（orbit / editorial / celebration）。它们在品牌版分别为产品主视觉、品牌编辑版、横幅问候版。重复提交复用任务；已有失败任务仅明确带 `retry:true` 重试，最多3次。
6. GET `/jobs/{id}`。仅 completed 后用账号鉴权下载 `/jobs/{id}/poster.png`、`/jobs/{id}/motion.mp4`；核对 receipt 哈希、1920×1080、约6秒，并查看实际成片。令牌不进入 URL。
7. POST `/briefs/{id}/decision`：`variant`、`decision`（adopted / rejected）、可选 `reason`（industry / style / brand / other）。完成导出才可采用。技术合格不会自动采用。

旧版直接提交 brand/industry/holiday 的接口保留，旧版输出仍为1280×720，不混淆两个版本。供应商模型调用数为0，CPU渲染和存储仍有成本。新生图服务、任意行业、任意节日不在该实现能力范围内。
