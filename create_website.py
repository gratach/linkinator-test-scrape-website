from pathlib import Path
import argparse
import os
import sys
import shutil

defaultDescription = "This is a test scrape website for linkinator to test the <a href='https://github.com/JustinBeckwith/linkinator/issues/534'>rate limit handling issue</a>.<br>The website was generated using  <a href='https://github.com/gratach/linkinator-test-scrape-website'>this repository</a>."

def main():
    parser = argparse.ArgumentParser(description="Generate a simple website with a list of links.")
    parser.add_argument("-c", "--pages-content", default="hi", help="The content of the numbered html files (default: hi)")
    parser.add_argument("-d", "--description", default=defaultDescription,help="HTML content to be displayed above the list in index.html")
    parser.add_argument("-n", "--page-number", type=int, required=True, help="The number of numbered html pages to be generated")
    parser.add_argument("-t", "--title", default="Linkinator Test", help="The title of the index.html page (default: Linkinator Test)")

    args = parser.parse_args()

    # Create directories
    dist_dir = (Path(__file__).parent / "dist").resolve()
    # Remove existing dist directory if it exists
    if dist_dir.exists():
        shutil.rmtree(str(dist_dir))
    dist_dir.mkdir(exist_ok=True)
    pages_dir = dist_dir / "pages"
    pages_dir.mkdir(exist_ok=True)

    # Generate numbered pages
    for i in range(1, args.page_number + 1):
        page_filename = f"{i}.html"
        page_path = pages_dir / page_filename
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(args.pages_content)

    # Generate index.html
    index_path = dist_dir / "index.html"

    links_html = "\n".join([f'        <li><a href="pages/{i}.html">Page {i}</a></li>' for i in range(1, args.page_number + 1)])

    description_html = f"    <div>{args.description}</div>" if args.description else ""

    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{args.title}</title>
</head>
<body>
    <h1>{args.title}</h1>
{description_html}
    <ul>
{links_html}
    </ul>
</body>
</html>
"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"Website generated in {dist_dir}/")

if __name__ == "__main__":
    main()
