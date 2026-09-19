# 图纸转白底图 Skill

从飞书产品 PIM 或本地 2D 工程图读取产品资料，校验型号、针数、间距、高度和附件冲突，再调用 Image2 或同类图片模型生成结构一致的无水印白底产品图。

## 能处理的输入

- 飞书 Base URL + 当前视图行号
- 飞书内部型号或 record_id
- 本地 2D PDF 工程图
- 可选的预览图、STEP/STP 和实物参考图

没有预览图也可以工作。2D 图纸需要包含足够的轴测图或互补正投影视图；只有单一投影且隐藏结构不明确时，Skill 会要求补充资料，而不是编造结构。

## 安装

把整个仓库复制到目标智能体的 Skills 目录，确保目录中保留 `SKILL.md`、`scripts/` 和 `references/`。支持标准 Agent Skills 的工具可直接调用：

```text
$drawing-to-white-background
读取这个飞书链接第 6 行，校验资料并生成无水印白底图。
```

仅使用本地 PDF：

```text
$drawing-to-white-background
根据这份 2D PDF 生成白底实物图。没有预览图，以图纸结构和尺寸为准。
```

## 环境要求

- Python 3
- 飞书工作流需要 `lark-cli`，并以用户身份登录
- PDF 渲染脚本需要 `PyMuPDF`
- Image2 或其他支持多参考图的高保真图像生成/编辑模型

## 默认规则

- 2D 工程图优先于预览图和文件名不匹配的 STEP/STP
- 精确保持针数、弹片、焊脚、孔位、槽位及关键尺寸
- 输出纯白背景、无 Logo、无水印、无参数文字
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
