# 图纸转白底图 Skill

从飞书产品 PIM 读取预览图、内部型号和 2D 工程图，以预览图锁定真实外观，以型号与2D图纸校验针数、间距、高度和具体变体，再调用 Image2 或同类图片模型生成自然真实的无水印白底产品图。

## 能处理的输入

- 飞书 Base URL + 当前视图行号
- 飞书内部型号或 record_id
- 必需的预览图或实物参考图
- 2D PDF 工程图
- 可选的 STEP/STP

没有预览图或实物参考图时停止生成，避免把图纸投影错误解释成真实接触件结构。2D图纸只用于核对具体型号的数量、间距和尺寸。

## 安装

把整个仓库复制到目标智能体的 Skills 目录，确保目录中保留 `SKILL.md`、`scripts/` 和 `references/`。支持标准 Agent Skills 的工具可直接调用：

```text
$drawing-to-white-background
读取这个飞书链接第 6 行，校验资料并生成无水印白底图。
```

## 环境要求

- Python 3
- 飞书工作流需要 `lark-cli`，并以用户身份登录
- PDF 渲染脚本需要 `PyMuPDF`
- Image2 或其他支持多参考图的高保真图像生成/编辑模型

## 默认规则

- 预览图锁定家族外观、结构方向和真实质感
- 内部型号与2D工程图锁定具体变体数量和尺寸
- 缺少预览图或实物参考图时不生成
- 精确保持针数、弹片、焊脚、孔位、槽位及关键尺寸
- 输出纯白背景、无 Logo、无水印、无参数文字
- 黑色塑胶使用自然炭黑哑光，金属使用低饱和浅金/香槟金，避免夸张CG质感
- 默认仅生成本地审核图，明确要求后才回填飞书

## 实用命令

读取飞书当前视图第 6 行：

```bash
python3 scripts/fetch_feishu_row.py \
  --url '<BASE_URL>' --row 6 --out-dir work/source
```

检测型号与附件名冲突：

```bash
python3 scripts/validate_record.py work/source/record.json
```

把 PDF 渲染成 PNG：

```bash
python3 scripts/render_pdf.py drawing.pdf --out-dir work/drawing-pages
```
