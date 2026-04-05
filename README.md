# Linkinator Rate Limit Test Generator

This repository provides a tool to generate static websites for testing rate limit handling in [linkinator](https://github.com/JustinBeckwith/linkinator).

## Purpose

The primary goal of this repository is to facilitate testing and reproducing issues related to server rate limits when using linkinator, specifically addressing [Issue #534](https://github.com/JustinBeckwith/linkinator/issues/534).

## Usage

Use the `create_website.py` script to generate a website with a specific number of pages.

```bash
python3 create_website.py -n 100
```

### Options

- `-n`, `--page-number`: (Required) The number of numbered HTML pages to be generated.
- `-c`, `--pages-content`: The content of the numbered HTML files (default: "hi").
- `-d`, `--description`: HTML content to be displayed above the list in `index.html`.
- `-t`, `--title`: The title of the `index.html` page (default: "linkinator test").

The generated website will be located in the `dist/` directory.
