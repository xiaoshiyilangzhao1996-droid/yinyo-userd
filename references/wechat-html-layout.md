# 微信公众号 HTML 排版规范

> yinyo-writer 产出的推广文章，最终以带排版的 HTML 交付，方便直接复制到公众号编辑器。

---

## 配色方案

| 用途 | 色值 | 说明 |
|------|------|------|
| 主色 | `#D4A373` | 橙棕，标题装饰、引用左边框、强调色 |
| 辅色 | `#5B8C5A` | 森林绿，章节标题、成功/正面高亮 |
| 正文 | `#3F3F3F` | 深灰，正文文字 |
| 辅助文字 | `#888888` | 浅灰，次要说明、引用出处 |
| 警示 | `#C0392B` | 暗红，核心论断、警告块 |
| 链接 | `#5B8C5A` | 绿色，URL地址 |
| 背景暖白 | `#FFF8F0` | 页面底色 |
| 引用背景 | `#FFFBF0` | 淡黄底 |
| 正面块背景 | `#F0F5F0` | 淡绿底 |
| 信息块背景 | `#F0F0F8` | 淡蓝紫底 |
| 暖色块背景 | `#FFF8F0` | 淡橙底 |
| 灰底块 | `#F6F8F6` | 浅灰底，通用卡片 |
| 警示背景 | `#FFF5F5` | 淡红底 |

---

## 全局样式

```html
<section style="max-width:677px;margin:0 auto;padding:20px 16px;
  font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC',
  'Hiragino Sans GB','Microsoft YaHei UI','Microsoft YaHei',Arial,sans-serif;
  font-size:16px;color:#3f3f3f;line-height:1.8;letter-spacing:0.5px;">
  <!-- 所有内容包在这个 section 里 -->
</section>
```

---

## 组件模板

### 1. 品牌头标

```html
<section style="margin-bottom:30px;">
<p style="font-size:12px;color:#d4a373;letter-spacing:2px;text-align:center;">
YINYO · 隐曜杂货铺
</p>
</section>
```

### 2. 章节标题

```html
<section style="margin:30px 0 20px;text-align:center;">
<p style="display:inline-block;font-size:18px;font-weight:bold;
  color:#5b8c5a;letter-spacing:1px;border-bottom:2px solid #d4a373;
  padding-bottom:6px;margin:0;">
章节标题文字
</p>
</section>
```

### 3. 引用块（金句/用户评论）

```html
<section style="background:#fffbf0;border-radius:8px;padding:16px 20px;
  margin:20px 0;border-left:3px solid #d4a373;">
<p style="font-size:15px;color:#7c6f5b;line-height:1.8;margin:0;font-style:italic;">
引用内容
</p>
</section>
```

### 4. 正文段落

```html
<p style="font-size:16px;color:#3f3f3f;line-height:2;">
正文内容，<b style="color:#5b8c5a;">关键词高亮</b>
</p>
```

### 5. 信息卡片（多视角/多案例）

**绿色系**（正面/第一视角）：
```html
<section style="background:#f0f5f0;border-radius:8px;padding:18px 20px;margin:18px 0;">
<p style="font-size:14px;color:#5b8c5a;font-weight:bold;margin:0 0 8px;letter-spacing:1px;">
🪵 视角名称
</p>
<p style="font-size:15px;color:#3f3f3f;line-height:2;margin:0;">
内容
</p>
<p style="font-size:14px;color:#7c6f5b;line-height:1.8;margin:8px 0 0;font-style:italic;">
金句
</p>
</section>
```

**蓝紫系**（第二视角）：`background:#f0f0f8`，标题色 `#6a5acd`
**暖橙系**（第三视角）：`background:#fff8f0`，标题色 `#d4a373`

### 6. 列表卡片

```html
<section style="background:#f6f8f6;border-radius:8px;padding:18px 22px;margin:18px 0;">
<p style="font-size:15px;color:#3f3f3f;line-height:2;margin:0 0 4px;">
🌲 条目一 <b style="color:#5b8c5a;">关键词</b>——说明
</p>
<p style="font-size:15px;color:#3f3f3f;line-height:2;margin:0 0 4px;">
🌊 条目二 ...
</p>
</section>
```

### 7. 核心论断块（强调）

```html
<section style="background:#fff5f5;border-radius:8px;padding:18px 22px;margin:22px 0;">
<p style="font-size:15px;color:#c0392b;line-height:2;margin:0;font-weight:bold;">
核心论断文字
</p>
</section>
```

### 8. 正面高亮块

```html
<section style="background:#f6f8f6;border-radius:8px;padding:16px 22px;margin:22px 0;">
<p style="font-size:15px;color:#5b8c5a;line-height:2;margin:0;font-weight:bold;">
高亮结论
</p>
</section>
```

### 9. GitHub/链接卡片

```html
<section style="background:#f6f8f6;border-radius:10px;padding:22px 24px;margin:30px 0;">
<p style="font-size:15px;color:#5b8c5a;font-weight:bold;margin:0 0 14px;letter-spacing:1px;">
📎 标题
</p>
<p style="font-size:15px;line-height:2;margin:0 0 12px;">
<b style="color:#d4a373;">项目名</b><br/>
<span style="color:#888;">一句话描述</span><br/>
<span style="color:#5b8c5a;font-size:14px;">https://github.com/...</span>
</p>
</section>
```

### 10. 分割线

```html
<section style="margin:30px 0 20px;text-align:center;">
<p style="display:inline-block;width:60px;height:1px;
  background:linear-gradient(to right,#d4a373,#5b8c5a);"></p>
</section>
```

### 11. 尾注（每篇必加）

```html
<section style="text-align:center;margin-top:25px;">
<p style="font-size:14px;color:#888;line-height:2;margin:0;">
<span style="color:#d4a373;font-weight:bold;">yinyo 隐曜</span><br/>
一人AI实验室，真实评测 · 实用技能 · 自由探索。
</p>
</section>
```

---

## 排版规则

1. **所有样式内联**（微信不支持 `<style>` 标签和 class）
2. **不用 `<div>`**，全部用 `<section>` 和 `<p>`
3. **不用外部字体**，只用系统字体栈
4. **圆角统一 8px**（卡片），10px（链接卡片）
5. **间距统一**：章节标题上下 30px/20px，卡片上下 18-22px
6. **图片宽度 100%**，`border-radius: 8px`
7. **不用 JS**（微信编辑器会过滤）
8. **配色克制**：只用上表中的颜色，不临时加新色

---

## 交付方式

推广文章产出时，同时提供：
1. **Markdown 原文**（推广文章.md）
2. **排版 HTML**（嵌入邮件正文 + 作为 .html 附件）

邮件发送至作者邮箱，方便直接复制粘贴到公众号编辑器。
