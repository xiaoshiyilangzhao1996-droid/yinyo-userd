#!/usr/bin/env python3
"""Convert agent-guide markdown to WeChat HTML - v4 card footer."""
import re, sys

with open('/root/.openclaw/workspace/outputs/agent-guide-2026-05-05/公众号推文.md', 'r') as f:
    md = f.read()

cover_img = '<p style="margin:20px 0;text-align:center;"><img src="https://placeholder-for-wechat-upload/cover.png" alt="Agent怎么选" style="max-width:100%;height:auto;border-radius:4px;"/></p>'
compare_img = '<p style="margin:22px 0;text-align:center;"><img src="https://placeholder-for-wechat-upload/compare.png" alt="五款Agent横向对比" style="max-width:100%;height:auto;border-radius:4px;"/></p><p style="margin:4px 0 18px;font-size:13px;color:#999;text-align:center;">▲ 五款Agent产品横向对比</p>'
tier_img = '<p style="margin:22px 0;text-align:center;"><img src="https://placeholder-for-wechat-upload/tier.png" alt="用户分层决策指南" style="max-width:100%;height:auto;border-radius:4px;"/></p><p style="margin:4px 0 18px;font-size:13px;color:#999;text-align:center;">▲ 按Agent融入程度分层选型指南</p>'

def wrap(body):
    return f'<section style="background-color:#fff;padding:16px 12px 36px;max-width:700px;margin:0 auto;box-sizing:border-box;word-wrap:break-word;font-family:-apple-system,BlinkMacSystemFont,\'Helvetica Neue\',\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei UI\',\'Microsoft YaHei\',Arial,sans-serif;color:#1A1A1A;line-height:1.85;font-size:16px;letter-spacing:0.2px;">\n{body}\n{footer_html()}\n</section>'

def title_html(t):
    return f'<p style="margin:0 0 22px;font-size:24px;line-height:1.45;color:#111;font-weight:800;">{t}</p>'

def summary_html(lines):
    h = '<section style="margin:0 0 26px;padding:14px 16px 12px;background:rgba(211,47,47,0.05);border-left:4px solid #D32F2F;box-sizing:border-box;">\n'
    h += f'<p style="margin:0 0 10px;font-size:15px;line-height:1.85;color:#555;">{lines[0]}</p>\n'
    for line in lines[1:]:
        line = re.sub(r'^\*\*(\d+)、\*\*', r'<b style="font-weight:700;color:#111;">\1、</b>', line)
        line = line.replace('**', '')
        h += f'<p style="margin:0 0 8px;font-size:15px;line-height:1.85;color:#222;">{line}</p>\n'
    h += '</section>'
    return h

def h2_html(t):
    return f'<h2 style="font-size:20px;font-weight:600;color:#fff;line-height:1.4;margin:32px 0 16px;padding:11px 18px;background-color:#D32F2F;border-radius:4px;box-sizing:border-box;">{t}</h2>'

def h3_html(t):
    return f'<h3 style="font-size:18px;font-weight:700;color:#1a1a1a;margin:26px 0 12px;line-height:1.5;">{t}</h3>'

def p_html(t):
    parts = re.split(r'(\*\*.+?\*\*)', t)
    result = []
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            result.append(f'<b style="font-weight:700;color:#111;">{part[2:-2]}</b>')
        else:
            result.append(part)
    return f'<p style="margin:18px 0;font-size:16px;line-height:1.85;color:#1a1a1a;">{"".join(result)}</p>'

def strong_p_html(t):
    t = t.replace('**', '')
    return f'<p style="margin:20px 0;font-size:17px;line-height:1.75;color:#111;font-weight:800;">{t}</p>'

def table_html(rows):
    h = '<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:14px;line-height:1.7;">\n'
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row.split('|') if c.strip()]
        if i == 1:
            continue
        h += '<tr>\n'
        is_header = (i == 0)
        for j, cell in enumerate(cells):
            c = cell
            if is_header:
                c = re.sub(r'\*\*(.+?)\*\*', r'<b style="color:#fff;">\1</b>', c)
                h += f'<td style="padding:10px 12px;background:#D32F2F;color:#fff;font-weight:600;border:1px solid #e0e0e0;text-align:center;">{c}</td>\n'
            else:
                c = re.sub(r'\*\*(.+?)\*\*', r'<b style="color:#D32F2F;font-weight:700;">\1</b>', c)
                c = c.replace('✅', '<span style="color:#2e7d32;">✅</span>')
                c = c.replace('❌', '<span style="color:#c0392b;">❌</span>')
                c = c.replace('⚠️', '<span style="color:#e67e22;">⚠️</span>')
                if j == 0:
                    c = f'<b style="color:#333;">{c}</b>'
                h += f'<td style="padding:8px 10px;border:1px solid #e0e0e0;text-align:center;background:#fff;font-size:13px;line-height:1.65;">{c}</td>\n'
        h += '</tr>\n'
    h += '</table>'
    return h

def footer_html():
    # Card-style author footer (v3.14 — 暖金渐隐方案A)
    return (
        '<section style="text-align:center;color:#C9A96E;font-size:14px;letter-spacing:16px;margin:2.8em auto 1.6em;padding-left:16px;">\u00b7\u00b7\u00b7</section>\n'
        '<section style="display:flex;align-items:center;gap:14px;padding:18px 16px;background:linear-gradient(135deg,#1a1a2e 0%,#12101f 40%,#0d0c17 100%);border-radius:10px;color:#e0e0e0;overflow:hidden;">\n'
        '  <section style="width:72px;height:72px;border-radius:50%;overflow:hidden;flex:0 0 72px;border:2px solid #C9A96E;">\n'
        '    <img src="https://placeholder-for-wechat-upload/avatar.png" alt="\u9690\u66dc" style="width:100%;display:block;" />\n'
        '  </section>\n'
        '  <section style="flex:1;">\n'
        '    <section style="display:flex;align-items:baseline;gap:10px;margin-bottom:6px;">\n'
        '      <section style="font-size:18px;font-weight:700;color:#ffffff;letter-spacing:0.04em;">\u9690\u66dc yinyo</section>\n'
        '      <section style="font-family:&apos;SF Mono&apos;,Menlo,monospace;font-size:10px;color:#C9A96E;letter-spacing:0.18em;">AUTHOR</section>\n'
        '    </section>\n'
        '    <section style="font-size:12px;color:#bbb;line-height:1.65;">\n'
        '      \u4e00\u4ebaAI\u5b9e\u9a8c\u5ba4<br/>\n'
        '      \u771f\u5b9e\u8bc4\u6d4b \u00b7 \u5b9e\u7528\u6280\u80fd \u00b7 \u81ea\u7531\u63a2\u7d22\n'
        '    </section>\n'
        '  </section>\n'
        '</section>'
    )

lines = md.split('\n')
blocks = []
i = 0
title_text = ''
summary_parts = []
in_summary = False
in_table = False
table_rows = []
h2c = 0

while i < len(lines):
    line = lines[i]
    
    if line.startswith('# ') and not title_text:
        title_text = line[2:]
        blocks.append(title_html(title_text))
        blocks.append(cover_img)
        i += 1
        continue
    
    if line.startswith('## '):
        h2c += 1
        blocks.append(h2_html(line[3:]))
        i += 1
        continue
    
    if line.startswith('### '):
        blocks.append(h3_html(line[4:]))
        i += 1
        continue
    
    if line.strip() == '---':
        i += 1
        continue
    
    if line.startswith('!['):
        i += 1
        continue
    
    # Summary section
    if line.startswith('**超长预警'):
        in_summary = True
        summary_parts = [line.replace('**', '')]
        i += 1
        continue
    
    if in_summary:
        if line.startswith('**') and line.strip().endswith('**') and len(line) < 200 and '、' not in line:
            blocks.append(summary_html(summary_parts))
            in_summary = False
            blocks.append(strong_p_html(line))
            i += 1
            continue
        if line.strip() == '':
            i += 1
            continue
        if line.startswith('**') and ('、' in line):
            summary_parts.append(line)
            i += 1
            continue
        else:
            blocks.append(summary_html(summary_parts))
            in_summary = False
            continue
    
    # Table
    if line.strip().startswith('|'):
        if not in_table:
            in_table = True
            table_rows = []
        table_rows.append(line)
        if i + 1 < len(lines) and lines[i+1].strip().startswith('|'):
            i += 1
            continue
        else:
            blocks.append(table_html(table_rows))
            table_rows = []
            in_table = False
            i += 1
            continue
    
    # Footer lines (old plain text footer - skip, replaced by card)
    if line.strip() in ('yinyo 隐曜', '一人AI实验室，真实评测 · 实用技能 · 自由探索。'):
        i += 1
        continue
    
    # Strong standalone bold line
    if line.startswith('**') and line.endswith('**') and len(line) < 120:
        blocks.append(strong_p_html(line))
        i += 1
        continue
    
    # Empty
    if line.strip() == '':
        i += 1
        continue
    
    # Bullet list items
    if line.strip().startswith('- '):
        text = line.strip()[2:]
        parts = re.split(r'(\*\*.+?\*\*)', text)
        result = []
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                result.append(f'<b style="font-weight:700;color:#111;">{part[2:-2]}</b>')
            else:
                result.append(part)
        blocks.append(f'<p style="margin:8px 0 8px 16px;font-size:16px;line-height:1.85;color:#1a1a1a;">{"".join(result)}</p>')
        i += 1
        continue
    
    # Regular paragraph
    blocks.append(p_html(line))
    i += 1

# Insert images at strategic positions
final = []
for block in blocks:
    final.append(block)
    if '五款产品横向对比' in block and 'h2' in block:
        final.append(compare_img)
    if '你现在该怎么选' in block and 'h2' in block:
        final.append(tier_img)

output = wrap('\n'.join(final))

outpath = '/root/.openclaw/workspace/outputs/agent-guide-2026-05-05/公众号推文.html'
with open(outpath, 'w') as f:
    f.write(output)

print(f'HTML: {len(output)} chars -> {outpath}')
# Quick validation
nested_b = 0
pos = 0
depth = 0
while True:
    ob = output.find('<b ', pos)
    cb = output.find('</b>', pos)
    if ob >= 0 and (cb < 0 or ob < cb):
        depth += 1
        pos = ob + 1
        if depth > 1:
            nested_b += 1
    elif cb >= 0:
        depth -= 1
        pos = cb + 1
    else:
        break
    if depth < 0:
        depth = 0
print(f'Nested <b> tags: {nested_b}')
print(f'Has <style>: {"<style" in output}')
print(f'Has class=: {"class=" in output}')
print(f'Has <div>: {"<div" in output}')
print(f'Has card footer: {"一人AI" in output and "border-radius:10px" in output}')
