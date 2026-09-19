# 飞书字段与读取方式

## 当前 PIM 常用字段

| 字段 | 用途 |
|---|---|
| 中文产品名称 | 产品变体描述与 P 数辅助校验 |
| 内部型号 | 具体变体主标识，如 BC-21-4P225 |
| 预览图 | 家族造型和视角参考，可能存在针数错误 |
| 2D图纸 | 工程结构和尺寸最高优先级真源 |
| 3D图 | 匹配型号时用于确定性渲染 |
| 替换图纸 | 新版图纸；存在时应与 2D 图纸比较版本 |
| 塑胶高度(mm) | 变体高度校验 |
| 间距mm | pitch 校验 |
| 实物原图 | 存在时用于真实材质和颜色参考 |

## URL 解析

```bash
lark-cli base +url-resolve --url '<BASE_URL>' --as user
```

保存返回的 `base_token`、`table_id` 和 `view_id`。

## 按视图行号读取

可见第 N 行对应 `offset=N-1`：

```bash
lark-cli base +record-list \
  --base-token <BASE_TOKEN> --table-id <TABLE_ID> --view-id <VIEW_ID> \
  --field-id '中文产品名称' --field-id '内部型号' \
  --field-id '预览图' --field-id '2D图纸' --field-id '3D图' \
  --field-id '替换图纸' --field-id '实物原图' \
  --field-id '塑胶高度(mm)' --field-id '间距mm' \
  --offset <N_MINUS_1> --limit 1 --format ndjson --output record.ndjson --as user
```

## 按型号搜索

```bash
lark-cli base +record-search \
  --base-token <BASE_TOKEN> --table-id <TABLE_ID> \
  --keyword '<MODEL>' --search-field '内部型号' --as user
```

## 下载附件

```bash
lark-cli base +record-download-attachment \
  --base-token <BASE_TOKEN> --table-id <TABLE_ID> \
  --record-id <RECORD_ID> --output <EXISTING_DIRECTORY> --as user
```

不传 `--file-token` 会下载该记录中的全部附件。
