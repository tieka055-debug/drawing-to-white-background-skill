# 白底产品图提示词模板

```text
Use case: product-mockup
Asset type: website white-background product image
Authoritative identity: <内部型号>, <间距> mm pitch, plastic housing height <高度> mm.
Input images:
- Image 1: required family preview or real product reference; authoritative for product family shape, contact orientation, viewing angle, color and material appearance.
- Image 2: 2D engineering drawing; authoritative for the exact variant's count and dimensions.
- Image 3: matching STEP render, if and only if its model variant matches.

Primary request: Create a photorealistic studio product photograph of <内部型号>.
Geometry requirements: exactly <P_COUNT> positions — exactly <P_COUNT> raised spring contacts, exactly <P_COUNT> solder/contact tabs, and exactly <P_COUNT> repeated housing channels. Preserve the housing walls, cavities, cutouts, contact bends, pitch and key dimensions from the engineering drawing.
Known source conflict: <CONFLICT_OR_NONE>. Ignore the conflicting portion and follow the engineering drawing plus model fields.
Materials: realistic charcoal-black matte engineering plastic, not crushed black; restrained low-saturation pale gold/champagne plated metal with natural brushed texture and minor real-world wear, not orange-gold or mirror-polished.
Scene: seamless pure white catalog background with a soft neutral contact shadow.
Composition: centered three-quarter front/top view, generous margin, square crop.
Constraints: geometry fidelity takes priority over beautification; no extra or missing parts; no text, dimensions, logo, watermark, props, packaging or hands.
Avoid: altered pin count, wrong contact orientation, duplicated contacts, warped housing, melted edges, fictional screws, holes or markings, saturated orange gold, mirror-gold, plastic-looking metal, dramatic CGI highlights.
```

当前只交付无水印白底图。不得在生成结果中添加 Logo、品牌角标或其他文字。

没有预览图或实物参考图时停止，不调用图像生成模型。
