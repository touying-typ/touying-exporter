# Touying Exporter

Export presentation slides in various formats for Touying.


## HTML Export

We generate SVG image files and package them with impress.js into an HTML file. This way, you can open and present it using a browser, and it supports GIF animations and speaker notes.

![image](https://github.com/touying-typ/touying-exporter/assets/34951714/207ddffc-87c8-4976-9bf4-4c6c5e2573ea)

![image](https://github.com/touying-typ/touying-exporter/assets/34951714/eac4976b-7d5d-40b6-8827-88c9a024b89a)


## PPTX Export

We generate PNG image files and package them into a PPTX file. This way, you can open and present it using PowerPoint, and it supports speaker notes.

![image](https://github.com/touying-typ/touying-exporter/assets/34951714/3d547c74-fb4b-4c31-81e5-5138a5d727c9)

## Install

```sh
pip install touying
```


## CLI

```text
usage: touying compile [-h] [--output OUTPUT] [--root ROOT] [--font-paths [FONT_PATHS ...]] [--start-page START_PAGE] [--count COUNT] [--ppi PPI] [--silent SILENT] [--format {html,pptx,pdf,pdfpc}] input

positional arguments:
  input                 Input file

options:
  -h, --help            show this help message and exit
  --output OUTPUT       Output file
  --root ROOT           Root directory for typst file
  --font-paths [FONT_PATHS ...]
                        Paths to custom fonts
  --start-page START_PAGE
                        Page to start from
  --count COUNT         Number of pages to convert
  --ppi PPI             Pixels per inch for PPTX format
  --silent SILENT       Run silently
  --format {html,pptx,pdf,pdfpc}
                        Output format
```

For example:

```sh
touying compile example.typ
```

You will get a `example.html` file. Open it with your browser and start your presentation :-)


## Use it as a python package

```python
import touying

touying.to_html("example.typ")
```

