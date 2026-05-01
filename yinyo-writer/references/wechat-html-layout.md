# 微信公众号 HTML 极简排版规范

> yinyo-writer 产出的推广文章，最终以带排版的 HTML 交付，方便直接复制到公众号编辑器。  
> v3.2 起，排版层切换为「卡兹克式极简阅读样式」：少装饰、少卡片、少颜色，靠短段落、留白、少量加粗和自然节奏完成阅读体验。  
> 注意：这里只替换输出样式，不替换 yinyo-writer 的写作方法论、选题逻辑、质检体系和花叔 DNA。

---

## 0. 排版总原则

一句话：

> 像一篇真人写的公众号长文，不像一张花里胡哨的信息海报。

执行原则：

1. **白底黑字为主。** 不使用大面积彩色背景，不做渐变，不做装饰性头图块。
2. **段落就是主要组件。** 80% 以上内容用普通 `<p>` 承载。
3. **少用卡片。** 卡片只用于引用、关键结论、链接信息；普通列表不进卡片。
4. **少用颜色。** 只保留黑、灰、品牌橙、暗红四类颜色。
5. **少用 emoji。** 不把 emoji 当行首符号，不用 `🌲/✅/📌/🔥` 做列表装饰。
6. **少用小标题。** 长文优先靠自然转场和短段落推进；如果必须分节，用极简数字标题。
7. **不做稀疏大块。** 不把一句话撑成一个大色块。
8. **强调只服务阅读。** 加粗和变色只给关键词、数字、方法名、核心判断。

---

## 1. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 正文 | `#222222` | 主体文字，接近黑色 |
| 次级文字 | `#666666` | 注释、说明、链接前后辅助文字 |
| 弱文字 | `#999999` | 尾注、时间、署名 |
| 品牌橙 | `#D4A373` | 少量关键词、链接、尾注品牌名 |
| 暗红 | `#C0392B` | 警示、反例、强判断，慎用 |
| 引用线 | `#E6D3BD` | 引用左边线 |
| 分割线 | `#EEEEEE` | 极浅灰分割线 |
| 引用背景 | `#FAFAFA` | 只用于引用块，极浅灰 |

禁止临时新增饱和色。禁止大面积绿色、蓝紫、粉色、渐变。

---

## 2. 全局容器

所有内容包在一个外层 `<section>` 中。

```html
<section style="max-width:677px;margin:0 auto;padding:8px 16px 40px;
  box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',
  'PingFang SC','Hiragino Sans GB','Microsoft YaHei UI','Microsoft YaHei',Arial,sans-serif;
  font-size:16px;color:#222;line-height:1.9;letter-spacing:0.2px;background:#fff;">
  <!-- 正文 -->
</section>
```

规则：

- 不使用 `<style>`。
- 不使用 class。
- 不使用 `<div>`。
- 只用 `<section>`、`<p>`、`span`、`b`、`a`、`img`。
- 微信编辑器兼容优先。

---

## 3. 基础组件

### 3.1 普通段落，默认组件

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.95;color:#222;">
正文内容。
</p>
```

要求：

- 一段只讲一个意思。
- 多用短段落。
- 关键句可以单独成段。
- 不要为了排版把短句塞进卡片。

### 3.2 关键短句，独立成段

```html
<p style="margin:26px 0 22px;font-size:17px;line-height:1.9;color:#222;font-weight:700;">
真正的问题，不是会不会安装。
</p>
```

适合：转折、核心判断、段落钩子。

不要滥用。每 800-1000 字出现 1-2 次即可。

### 3.3 行内强调

```html
<b style="color:#222;font-weight:700;">关键词</b>
```

默认加粗只用黑色。不要每个关键词都染色。

### 3.4 品牌橙强调，慎用

```html
<b style="color:#D4A373;font-weight:700;">王正元 AI 生产系统实践</b>
```

适合：

- 方法名
- 产品名
- 项目名
- 文章最核心概念

每 500 字不超过 2-3 处。

### 3.5 暗红警示，极少用

```html
<b style="color:#C0392B;font-weight:700;">不要伪造官方背书</b>
```

只用于风险、反例、强警示。

---

## 4. 标题与分节

### 4.1 文章标题

```html
<p style="margin:0 0 24px;font-size:24px;line-height:1.45;color:#111;font-weight:800;">
文章标题
</p>
```

标题只出现一次。

### 4.2 极简分节标题

如果文章必须分节，用这种：

```html
<p style="margin:34px 0 16px;font-size:18px;line-height:1.6;color:#111;font-weight:800;">
1、先说结论
</p>
```

规则：

- 不居中。
- 不加下划线。
- 不加背景色。
- 不加 emoji。
- 不用 `##` 的视觉效果。

### 4.3 自然转场优先

如果不是方法论/清单文，优先不用分节标题，用普通段落自然转场：

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.95;color:#222;">
说到这里，我想先把一个误区拆掉。
</p>
```

---

## 5. 引用与重点块

### 5.1 极简引用块

```html
<section style="margin:24px 0;padding:2px 0 2px 16px;border-left:3px solid #E6D3BD;">
<p style="margin:0;font-size:16px;line-height:1.9;color:#555;">
引用内容或金句。
</p>
</section>
```

引用块不加大背景。最多用极浅灰。

### 5.2 轻提示块，少用

```html
<section style="margin:24px 0;padding:16px 18px;background:#FAFAFA;border-radius:6px;">
<p style="margin:0;font-size:15px;line-height:1.9;color:#333;">
这里放一个高密度总结，不放普通列表。
</p>
</section>
```

只用于：总结、关键提醒、链接说明。

禁止：一行一个卡片、emoji 列表卡片、彩色多卡片。

---

## 6. 列表处理

### 6.1 普通并列，用正文写

不要这样：

```html
<section>✅ 第一项</section>
<section>✅ 第二项</section>
<section>✅ 第三项</section>
```

应该这样：

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.95;color:#222;">
这里面至少包括 <b style="font-weight:700;color:#222;">记忆</b>、Skill、工具编排、多 Agent 协作、验收和沉淀。
</p>
```

### 6.2 必须分条时，用普通段落

```html
<p style="margin:0 0 12px;font-size:16px;line-height:1.9;color:#222;">
<b style="font-weight:700;color:#222;">第一，工具使用。</b>解决的是怎么跑起来。
</p>
<p style="margin:0 0 12px;font-size:16px;line-height:1.9;color:#222;">
<b style="font-weight:700;color:#222;">第二，Skill 开发。</b>解决的是怎么把经验复用起来。
</p>
```

规则：

- 不用 `<ul>`。
- 不用 emoji bullet。
- 不用大色块包裹普通列表。

---

## 7. 链接处理

### 7.1 普通链接

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.9;color:#666;">
公开资料，<span style="color:#D4A373;">https://example.com</span>
</p>
```

微信里链接不一定可点，重点是可读、可复制。

### 7.2 链接信息块，少用

```html
<section style="margin:26px 0;padding:16px 18px;background:#FAFAFA;border-radius:6px;">
<p style="margin:0 0 8px;font-size:15px;line-height:1.8;color:#222;font-weight:700;">
公开资料
</p>
<p style="margin:0;font-size:14px;line-height:1.8;color:#D4A373;">
https://example.com
</p>
</section>
```

只在文章末尾或项目介绍处使用。

---

## 8. 图片

```html
<p style="margin:24px 0;text-align:center;">
<img src="图片地址" style="max-width:100%;border-radius:6px;display:block;margin:0 auto;" />
</p>
```

图片说明：

```html
<p style="margin:-10px 0 22px;font-size:13px;line-height:1.7;color:#999;text-align:center;">
图片说明
</p>
```

---

## 9. 分割线

```html
<section style="margin:34px 0;border-top:1px solid #EEE;"></section>
```

只用于明显章节转折或尾注前。

---

## 10. 尾注

```html
<section style="margin:34px 0 0;padding-top:18px;border-top:1px solid #EEE;">
<p style="margin:0;font-size:13px;line-height:1.8;color:#999;">
<span style="color:#D4A373;font-weight:700;">yinyo 隐曜</span><br/>
一人AI实验室，真实评测，实用技能，自由探索。
</p>
</section>
```

尾注要轻，不要像广告牌。

---

## 11. 交付前 L5 检查

排版完成后必须检查：

| 检查项 | 标准 |
|---|---|
| 极简程度 | 80% 以上内容是普通段落，不是卡片 |
| 背景 | 全文白底为主，无大面积彩色背景 |
| 颜色 | 只使用黑、灰、品牌橙、暗红、极浅灰 |
| 卡片 | 不超过 3 个，且只用于引用、总结、链接 |
| 标题 | 不居中、不下划线、不 emoji 装饰 |
| 列表 | 无 emoji 行首列表，无一行一个大块 |
| 强调 | 加粗服务阅读，不满屏彩色高亮 |
| 微信兼容 | 全部内联样式，无 `<style>`，无 class，无 `<div>` |
| 方法论保留 | 只改排版样式，不改变文章内容逻辑和写作质检 |

如果看起来像模板站、知识星球海报、PPT 信息卡，就失败。

目标观感：

> 一篇干净、有呼吸感、像真人认真写出来的公众号长文。

---

## 12. 交付方式

推广文章产出时，同时提供：

1. **Markdown 原文**，用于二次修改。
2. **极简排版 HTML**，嵌入邮件正文 + 作为 `.html` 附件。

HTML 只负责阅读体验，不负责炫技。
