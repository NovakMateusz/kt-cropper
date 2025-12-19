# Examples 

Extracts operative datacards from pages 1–3 of a PDF, using predefined crop regions to capture multiple cards per page.
```bash
kt_cropper document.pdf -m crop-manifest-1.json
```


---
Extracts rule datacards from pages 3–11 of the PDF. Each page is divided into four fixed crop regions, allowing the tool to capture up to four cards per page and save them as individual image files.
```bash
kt_cropper document.pdf -m crop-manifest-2.json
```


---
Extracts all datacards from pages 0–11 of the PDF, including operatives, rules, ploys, and equipment. Each section uses predefined crop layouts to save multiple cards per page as individual image files.
```bash
kt_cropper document.pdf -m crop-manifest-3.json
```


---
Extracts all datacards across pages 0–11, handling multiple layout changes. It extracts operatives, operative selection cards, rules, tokens, ploys, faction equipment, and equipment using page-specific crop regions, saving every card as an individual image file.
```bash
kt_cropper document.pdf -m crop-manifest-4.json
```


---
Renders each page at 500 DPI, producing higher-resolution images.
```bash
kt_cropper document.pdf -m crop-manifest-4.json -d 500
```
