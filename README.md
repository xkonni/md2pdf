# md2pdf

## description

convert markdown into pdf, accepts optional css file

based loosely on:
- https://github.com/kxxoling/markdown2pdf
- https://github.com/ljpengelen/markdown-to-pdf

## installation

```bash
$ git clone https://github.com/xkonni/md2pdf
$ cd md2pdf
$ pip3 install .
```

## usage

show help

```bash
$ md2pdf -h

usage: md2pdf [-h] [-c style.css] file.md

md2pdf

positional arguments:
  file.md               markdown file to process

optional arguments:
  -h, --help            show this help message and exit
  -c style.css, --css style.css
                        custom css stylesheet, defaults to github
```

run

```bash
$ md2pdf -c /path/to/style.css /path/to/file.md
```

results in `/path/to/file.pdf`
