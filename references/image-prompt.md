# 白底产品图提示词模板

```text
Use case: product-mockup
Asset type: website white-background product image
Authoritative identity: <内部型号>, <间距> mm pitch, plastic housing height <高度> mm.
Input images:
- Image 1: family preview for general housing style and viewing angle only（没有预览图时省略）.
- Image 2: authoritative 2D engineering drawing for structure and dimensions.
- Image 3: matching STEP render, if and only if its model variant matches.

Primary request: Create a photorealistic studio product photograph of <内部型号>.
Geometry requirements: exactly <P_COUNT> positions — exactly <P_COUNT> raised spring contacts, exactly <P_COUNT> solder/contact tabs, and exactly <P_COUNT> repeated housing channels. Preserve the housing walls, cavities, cutouts, contact bends, pitch and key dimensions from the engineering drawing.
Known source conflict: <CONFLICT_OR_NONE>. Ignore the conflicting portion and follow the engineering drawing plus model fields.
Materials: <已确认材质与颜色；未知时写默认假设>.
Scene: seamless pure white catalog background with a soft neutral contact shadow.
Composition: centered three-quarter front/top view, generous margin, square crop.
Constraints: geometry fidelity takes priority over beautification; no extra or missing parts; no text, dimensions, logo, watermark, props, packaging or hands.
Avoid: altered pin count, duplicated contacts, warped housing, melted edges, fictional screws, holes or markings.
```

当前只交付无水印白底图。不得在生成结果中添加 Logo、品牌角标或其他文字。

## 仅图纸模式补充语句

```text
No product preview photo is available. Reconstruct only the geometry supported by the orthographic/isometric engineering views. Do not invent hidden holes, fasteners, latches, markings or additional metal parts. Treat all unspecified surface appearance as an explicit visual assumption, not an engineering fact.
```
