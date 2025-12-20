# Crop Manifest Schema

A crop manifest defines how `kt_cropper` extracts datacards from a PDF for a specific Kill Team.

---

## Top-Level Structure

```json
{
  "team_name": "string",
  "extractions": [ Extraction ]
}
```

### Fields

| Field         | Type   | Required | Description                                                                |
|---------------|--------|----------|----------------------------------------------------------------------------|
| `team_name`   | string | True     | Name of the Kill Team or faction. Used for organization and output naming. |
| `extractions` | array  | True     | List of extraction definitions describing what to crop and from where.     |

---

## Extraction Object

Each extraction defines **what type of datacards** to extract from a **specific page range**, using one or more crop regions.

```json
{
  "name": "string",
  "scope": Scope,
  "crop_boxes": [ CropBox ]
}
```

### Fields

| Field        | Type   | Required | Description                                                                               |
|--------------|--------|----------|-------------------------------------------------------------------------------------------|
| `name`       | string | True     | Logical name of the extracted content (e.g. `operatives`, `rules`, `ploys`, `equipment`). |
| `scope`      | object | True     | Page range in the PDF where this extraction applies.                                      |
| `crop_boxes` | array  | True     | List of rectangular regions to crop per page.                                             |

Multiple extractions may share the same `name` to handle layout changes across pages.

---

## Scope Object

Defines which pages of the PDF are processed for a given extraction.

```json
{
  "start_page": integer,
  "stop_page": integer
}
```

### Fields

| Field        | Type    | Required | Description                                                |
|--------------|---------|----------|------------------------------------------------------------|
| `start_page` | integer | True     | Zero-based index of the first page to process (inclusive). |
| `stop_page`  | integer | True     | Zero-based index of the page to stop at (exclusive).       |

Example:
```json
{
  "start_page": 3,
  "stop_page": 6
}
```
pages 3, 4, and 5, but not 6.

---

## Crop Box

Defines a rectangular region to extract from each page in the scope.

```json
[x1, y1, x2, y2]
```

### Values

| Index | Description                    |
|-------|--------------------------------|
| `x1`  | Left coordinate (PDF point)   |
| `y1`  | Top coordinate (PDF point)    |
| `x2`  | Right coordinate (PDF point)  |
| `y2`  | Bottom coordinate (PDF point) |

- Coordinates are specified in PDF points (1 point = 1/72 inch).
- Crop boxes are DPI-independent. During processing, coordinates are scaled to pixels using the selected DPI (dpi / 72).
- Each crop box produces one output image per page.
- Multiple crop boxes allow extracting multiple cards from a single page.

---

## Notes & Best Practices

- Page indexing is **zero-based**.
- Use **multiple extraction entries** when you want to extract cards under different name or the page layout changes.
- Keep crop boxes consistent across pages with identical layouts.
