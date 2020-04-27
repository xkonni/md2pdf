#!/usr/bin/env python3
#
# md2pdf
#
# convert markdown into pdf, accepts optional css file
#
# Author: Konstantin Koslowski <konstantin.koslowski@gmail.com>
# based loosely on:
# - https://github.com/kxxoling/markdown2pdf
# - https://github.com/ljpengelen/markdown-to-pdf
#

import argparse
import os
import markdown
from markdown_include.include import MarkdownInclude
from weasyprint import HTML

MODULE_DIR=os.path.dirname(__file__)
CSS=f"{MODULE_DIR}/github.css"

def _html(markdown_file_name, css_file_name):
    with open(markdown_file_name, mode="r", encoding="utf-8") as markdown_file:
        with open(css_file_name, mode="r", encoding="utf-8") as css_file:
            markdown_input = markdown_file.read()
            css_input = css_file.read()

            markdown_path = os.path.dirname(markdown_file_name)
            markdown_include = MarkdownInclude(configs={"base_path": markdown_path})
            html = markdown.markdown(
                markdown_input, extensions=["extra", markdown_include, "meta", "tables"]
            )

            return f"""
            <html>
              <head>
                <style>{css_input}</style>
              </head>
              <body>{html}</body>
            </html>
            """


def convert(markdown_file_name, css_file_name):
    if not css_file_name:
        css_file_name = CSS
    file_name = os.path.splitext(markdown_file_name)[0]
    html_string = _html(markdown_file_name, css_file_name)

    markdown_path = os.path.dirname(markdown_file_name)
    html = HTML(string=html_string, base_url=markdown_path)
    html.write_pdf(file_name + ".pdf")


def main():
    parser = argparse.ArgumentParser(description="md2pdf")
    parser.add_argument("mdfile", metavar="file.md", type=str,
            help="markdown file to process")
    parser.add_argument("-c", "--css", dest="cssfile", metavar="style.css", type=str,
            help="custom css stylesheet, defaults to github")
    args = parser.parse_args()
    convert(args.mdfile, args.cssfile)


if __name__ == "__main__":
    main()
