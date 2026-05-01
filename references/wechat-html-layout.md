# 微信公众号 HTML 花叔式极简长文排版规范

> yinyo-writer 产出的公众号推文，最终以带排版的 HTML 交付，方便直接复制到公众号编辑器。  
> v3.5 起，排版层升级为「花叔红色组件长文版」：以花叔原文为标尺，不再走米色高级极简；核心是微信原生发布感、红色强品牌锚点、红底白字标题块、红色表头、紧凑正文节奏。  
> 注意：这里只替换输出样式，不替换 yinyo-writer 的写作方法论、选题逻辑、质检体系和花叔 DNA。

---

## 0. 样式目标

这版的目标不是“高级极简”，而是“接近花叔原文观感”：红色锚点强、标题切段明确、正文紧凑、组件丰富但不花。

一句话：

> 像花叔那种能撑住 9000 字技术长文的公众号排版：干净、密集、能读下去，不像模板海报。

这套样式复刻的不是某个颜色，而是阅读体验：

1. **开头先给读者减负。** 长文必须有「超长预警 / 核心总结 / 先说结论」一类摘要区。
2. **正文靠短段落推进。** 一段一个意思，很多句子可以单独成段。
3. **小标题少，但要有力量（判断式标题）。** 标题像判断句，不像 PPT 栏目名。
4. **重点靠加粗，不靠彩色卡片。** 关键判断、数字、方法名可以加粗。
5. **表格可以用。** 涉及模型对比、评分、时间线、参数时，表格比散文清楚。
6. **代码/坐标/论文术语要轻量呈现。** 用等宽字体或浅灰代码块，不做炫技代码框。
7. **少 emoji。** 不用 emoji 当列表符号。
8. **广告感要低。** 尾注轻，CTA 轻，不要像知识星球海报。

---

## 1. 花叔红色组件参数

推荐固定参数：

- 外层容器：`max-width:700px; padding:16px 12px 36px;`
- 正文字号：`16px`
- 正文行高：`1.85`
- 正文字色：`#1A1A1A`
- 主品牌红：`#D32F2F`
- 标题块：红底白字，`font-size:20px; line-height:1.4; padding:12px 20px; border-radius:4px;`
- 正文段落：`margin:18px 0`，不要过松
- 表格表头：`background:#D32F2F; color:#FFFFFF; padding:10px 14px;`
- 强调：关键强判断可用红字浅红底，`rgba(211,47,47,0.08)`
- 摘要：优先普通正文连续段；如用摘要块，必须用红色左线，不用米色 Notion 感
- 代码/坐标块：浅灰底 + 红色左线，避免程序员文档感

舒服感不等于低饱和。花叔的舒服感来自：正文克制 + 红色组件做节奏锚点。

## 2. 全局容器

所有内容包在一个外层 `<section>` 中。

```html
<section style="background-color:#fff;padding:16px 12px 36px;max-width:700px;margin:0 auto;box-sizing:border-box;word-wrap:break-word;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC','Hiragino Sans GB','Microsoft YaHei UI','Microsoft YaHei',Arial,sans-serif;color:#1A1A1A;line-height:1.85;font-size:16px;letter-spacing:0.2px;">
  <!-- 正文 -->
</section>
```

规则：

- 不使用 `<style>`。
- 不使用 class。
- 不使用 `<div>`。
- 样式全部内联。
- 微信编辑器兼容优先。

---

## 3. 文章标题

标题左对齐，黑色，不居中，不加背景。

```html
<p style="margin:0 0 22px;font-size:24px;line-height:1.45;color:#111;font-weight:800;">
文章标题
</p>
```

标题规则：

- 一篇只出现一次。
- 不用 emoji 开头。
- 不加下划线。
- 不做居中大字报。

---

## 4. 开头摘要区

花叔式长文的关键是开头先帮读者抓重点。超过 2500 字的文章，必须有摘要区。

### 3.1 超长预警 + 核心总结

```html
<section style="margin:0 0 26px;padding:14px 16px 12px;background:rgba(211,47,47,0.05);border-left:4px solid #D32F2F;box-sizing:border-box;">
  <p style="margin:0 0 10px;font-size:15px;line-height:1.85;color:#555;">
  超长预警，这篇文章预计阅读时长 12 分钟。如果你只想看结论，先看这四条：
  </p>
  <p style="margin:0 0 8px;font-size:15px;line-height:1.85;color:#222;">
  <b style="font-weight:700;color:#111;">1、</b>第一条核心结论。
  </p>
  <p style="margin:0 0 8px;font-size:15px;line-height:1.85;color:#222;">
  <b style="font-weight:700;color:#111;">2、</b>第二条核心结论。
  </p>
  <p style="margin:0;font-size:15px;line-height:1.85;color:#222;">
  <b style="font-weight:700;color:#111;">3、</b>第三条核心结论。
  </p>
</section>
```

摘要区规则：

- 只用于开头，不要全文到处放卡片。
- 背景只用极浅灰。
- 左侧细线即可，不做大面积彩色块。
- 3-5 条为宜。
- 每条必须是真结论，不是目录。

### 3.2 短文不用摘要卡

如果文章少于 2000 字，可以直接开头：

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.85;color:#1A1A1A;">
先说结论。
</p>
```

---

## 5. 正文段落

### 4.1 普通段落

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.85;color:#1A1A1A;">
正文内容。
</p>
```

段落规则：

- 一段尽量 20-80 字。
- 一个段落只讲一个意思。
- 不要把多个判断塞进一段。
- 长句拆短。
- 关键转折可以单独成段。

### 4.2 独立判断句

适合放核心判断、反共识句、章节前的钩子。

```html
<p style="margin:26px 0 20px;font-size:17px;line-height:1.88;color:#111111;font-weight:800;">
真正的问题，不是看得清，而是指得准。
</p>
```

规则：

- 不要滥用。
- 每 800-1200 字出现 1 次左右。
- 必须像人话判断，不要像口号。

---

## 6. 小标题（红底判断式标题）

花叔式标题一般是红底白字块，短、有态度，承担长文切段功能，不是「一、背景介绍」这种公文标题。

```html
<h2 style="font-size:20px;font-weight:600;color:#fff;line-height:1.4;margin:32px 0 16px;padding:12px 20px;background-color:#D32F2F;border-radius:4px;box-sizing:border-box;">
主流派在解决「看得清」，DeepSeek 在解决「指得准」
</h2>
```

标题规则：

- 左对齐。
- 不编号也可以。
- 不居中。
- 不加 emoji。
- 不加背景。
- 不加下划线。
- 标题本身要有信息量。

差标题：

```text
一、项目背景
二、技术分析
三、总结
```

好标题：

```text
为什么 coding agent 必须有视觉
主流派在解决「看得清」，DeepSeek 在解决「指得准」
真正的差距出现在拓扑推理
这件事对普通用户意味着什么
```

---

## 7. 强调规则

### 6.1 默认黑色加粗

```html
<b style="font-weight:700;color:#111;">关键判断</b>
```

使用对象：

- 核心概念
- 关键数字
- 方法名
- 反共识判断
- 文章结论

### 6.2 品牌橙少量使用

```html
<b style="font-weight:700;color:#D32F2F;background-color:rgba(211,47,47,0.08);padding:2px 6px;border-radius:3px;">Skill Radar</b>
```

只用于：

- 自有产品名
- 核心方法名
- 文章最重要概念

每 800 字不超过 2-3 处。红色是节奏锚点，不是荧光笔。

### 6.3 警示暗红极少使用

```html
<b style="font-weight:700;color:#B42318;">不要伪造官方背书</b>
```

只用于风险、错误口径、强警示。

---

## 8. 列表写法

花叔式列表多数是自然段，不是 bullet 列表。

### 7.1 普通分条

```html
<p style="margin:0 0 12px;font-size:16px;line-height:1.9;color:#222;">
<b style="font-weight:700;color:#111;">第一，</b>它解决的是反复出现的问题。
</p>
<p style="margin:0 0 12px;font-size:16px;line-height:1.9;color:#222;">
<b style="font-weight:700;color:#111;">第二，</b>它有稳定流程，而不是靠灵感发挥。
</p>
```

规则：

- 不用 `<ul>`。
- 不用 emoji bullet。
- 不用一行一个彩色卡片。
- 分条之间间距比普通段落略小。

### 7.2 开头摘要可以用数字条

摘要区允许 `1、2、3、4、`，但仍然用 `<p>`。

---

## 9. 表格

技术对比、模型数据、版本时间线可以用表格。表格要有红色表头，这是花叔长文的重要视觉锚点。不要做彩色大杂烩，但表头必须有识别度。

```html
<table style="width:100%;border-collapse:collapse;margin:22px 0;font-size:14px;line-height:1.7;color:#222;">
  <thead>
    <tr>
      <th style="background-color:#D32F2F;color:#FFFFFF;padding:10px 14px;text-align:left;font-weight:600;border:none;">模型</th>
      <th style="background-color:#D32F2F;color:#FFFFFF;padding:10px 14px;text-align:left;font-weight:600;border:none;">KV cache 条目</th>
      <th style="background-color:#D32F2F;color:#FFFFFF;padding:10px 14px;text-align:left;font-weight:600;border:none;">平均分</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border-bottom:1px solid #F0F0F0;padding:8px 6px;">DeepSeek</td>
      <td style="border-bottom:1px solid #F0F0F0;padding:8px 6px;">~90</td>
      <td style="border-bottom:1px solid #F0F0F0;padding:8px 6px;">77.2%</td>
    </tr>
  </tbody>
</table>
```

表格规则：

- 正文只用浅灰边线。
- 表头红底白字。
- 不做多色表头。
- 不做复杂合并单元格。
- 移动端优先，列数不超过 4。

---

## 10. 代码、坐标、论文符号（轻量代码/坐标块）

### 9.1 行内代码

```html
<code style="font-family:Menlo,Consolas,monospace;font-size:14px;background:#F3F2EF;color:#333;padding:1px 4px;border-radius:3px;">prompt-master</code>
```

适合：仓库名、变量名、模型名、短代码。

### 9.2 代码块 / 坐标块

```html
<section style="margin:18px 0;padding:12px 14px;background:#F7F6F3;border-radius:6px;box-sizing:border-box;">
<p style="margin:0;font-family:Menlo,Consolas,monospace;font-size:13px;line-height:1.75;color:#333;white-space:pre-wrap;">
&lt;|point|&gt;[[357,369],[260,372]]&lt;|/point|&gt;
</p>
</section>
```

规则：

- 只用于必要的代码、坐标、论文格式示例。
- 不要把普通金句放进代码块。
- 背景浅灰即可。

---

## 11. 引用

引用论文原文、外部文档、用户原话时，用左线引用。

```html
<section style="margin:22px 0;padding:2px 0 2px 14px;border-left:3px solid #D9C2A0;box-sizing:border-box;">
<p style="margin:0;font-size:15px;line-height:1.9;color:#555;">
引用内容。
</p>
</section>
```

规则：

- 不加大背景。
- 不用引号图标。
- 引用之后必须用人话解释。

---

## 12. 图片

```html
<p style="margin:24px 0;text-align:center;">
<img src="图片地址" style="max-width:100%;border-radius:6px;display:block;margin:0 auto;" />
</p>
```

图片说明：

```html
<p style="margin:-8px 0 22px;font-size:13px;line-height:1.7;color:#999;text-align:center;">
图片说明
</p>
```

---

## 13. 分割线

```html
<section style="margin:34px 0;border-top:1px solid #EEE;"></section>
```

只用于明显转场或尾注前。

---

## 14. 尾注

尾注要轻，不要像广告牌。

```html
<section style="margin:36px 0 0;padding-top:18px;border-top:1px solid #EEE;">
<p style="margin:0;font-size:13px;line-height:1.8;color:#999;">
<span style="color:#B7793E;font-weight:700;">隐曜杂货铺</span><br/>
一人 AI 实验室，真实评测，实用技能，自由探索。
</p>
</section>
```

---

## 15. 禁止事项

禁止：

- 大面积彩色卡片。
- 彩色渐变背景。
- emoji 列表。
- 居中标题。
- 下划线标题。
- 一句话一个大卡片。
- 满屏橙色/红色高亮。
- PPT 式信息块堆叠。
- 使用 `<style>`、class、`<div>`。
- 把正文拆得过稀，读起来像广告落地页。

---

## 16. 交付前 L5 检查

排版完成后必须检查：

| 检查项 | 标准 |
|---|---|
| 长文摘要 | 超过 2500 字必须有开头摘要区 |
| 段落 | 80% 以上内容是普通 `<p>` 段落 |
| 标题 | 左对齐、无背景、无 emoji、标题本身有判断 |
| 强调 | 以黑色加粗为主，橙色极少 |
| 表格 | 数据对比优先用朴素表格 |
| 代码 | 仓库名/坐标/短代码用轻量 `code` 或浅灰代码块 |
| 卡片 | 除开头摘要外，全文卡片不超过 2 个 |
| 背景 | 全文白底为主，无大面积彩色背景 |
| 微信兼容 | 全部内联样式，无 `<style>`，无 class，无 `<div>` |
| 方法论保留 | 只改排版样式，不改变文章内容逻辑和写作质检 |

如果看起来像模板站、知识星球海报、PPT 信息卡，就失败。

目标观感：

> 一篇干净、有呼吸感、能撑住长文阅读的公众号文章。

---

## 17. 交付方式

公众号推文产出时，同时提供：

1. **Markdown 原文**，用于二次修改。
2. **花叔式极简排版 HTML**，嵌入邮件正文 + 作为 `.html` 附件。

HTML 只负责阅读体验，不负责炫技。
