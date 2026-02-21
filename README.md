This is my CV.
To access the deployed page go to: https://lucastt.github.io/cv/

# CV PDF Generator

Generates a styled PDF from HTML file.

## Usage

```bash
python generate_cv.py <input.html> <output_dir>
```

**Example:**

```bash
python generate_cv.py index.html ~/Desktop
```

This will produce a file named `lucas-thiesen-cv-dd-mm-yyyy.pdf` in the specified output directory, where `dd-mm-yyyy` is today's date.

## How it works

The script parses the HTML file and maps its structure to a styled PDF. Content is read dynamically from the HTML — styles are hardcoded. To update the CV, edit `index.html` and rerun the script.

The parser distinguishes between two types of `h2` elements using their `id` attributes:

- **Section headers** (`SECTION_IDS`): `summary`, `skills`, `engineering-experience`, `education` — rendered as section dividers with a rule line.
- **Company headers** (`COMPANY_IDS`): all other experience blocks — rendered as company entries with roles, bullets, and tech lines.

## Adding a new experience block

1. Add the new experience block to `index.html` following the same format as existing company entries. Make sure the `h2` has an `id` attribute (GitHub Pages generates these automatically from the heading text).

2. Add the new `id` to `COMPANY_IDS` at the top of `generate_cv.py`:

```python
COMPANY_IDS = {"new-company", "delivery-hero", "zalando", "quinto-andar", "3778", "certi"}
```

3. Rerun the script. The new entry will appear in the PDF in the same order it appears in the HTML.

No other changes are needed — role parsing, bullet detection, tech line detection, and page layout are all driven by HTML structure.

## Expected HTML structure

Each company block should follow this structure:

```html
<h2 id="company-name"><a href="...">Company Name</a></h2>
<p>Company description.</p>

<p><strong>Role Title</strong> <em>(Date range)</em></p>
<p>Role context paragraph.</p>
<ul>
  <li>Bullet point.</li>
  <li><strong><em>Technologies:</em></strong> Go · Kubernetes · ...</li>
</ul>
```

Multiple roles under the same company are supported — just repeat the `<p><strong>...</strong></p>` + `<ul>` pattern.
