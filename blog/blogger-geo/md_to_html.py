"""Convert the 5 GEO blog articles (markdown) to Blogger-ready HTML body snippets."""
import os, re, glob

SRC = r"C:\Users\Saladin\Desktop\yominelectric-main\blog\blogger-geo"
OUT = os.path.join(SRC, "html")
os.makedirs(OUT, exist_ok=True)

def inline(text):
    # links
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
                  r'<a href="\2" rel="noopener" target="_blank">\1</a>', text)
    # bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text

def table_to_html(rows):
    # rows: list of list of cells
    html = ["<table>"]
    for i, row in enumerate(rows):
        tag = "th" if i == 0 else "td"
        cells = "".join(f"<{tag}>{inline(c.strip())}</{tag}>" for c in row)
        html.append(f"<tr>{cells}</tr>")
    html.append("</table>")
    return "\n".join(html)

def convert(md):
    out = []
    para = []
    table_rows = []
    in_list = False

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def flush_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        # table row?
        if line.strip().startswith("|") and line.strip().endswith("|"):
            flush_para(); flush_list()
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # separator row like |---|---|
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                i += 1; continue
            table_rows.append(cells)
            # peek next: if next is also table row keep collecting; else emit
            if i + 1 >= len(lines) or not (lines[i+1].strip().startswith("|") and lines[i+1].strip().endswith("|")):
                out.append(table_to_html(table_rows))
                table_rows = []
            i += 1; continue
        if line.startswith("### "):
            flush_para(); flush_list()
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush_para(); flush_list()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush_para(); flush_list()
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("- "):
            flush_para()
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append("<li>" + inline(line[2:]) + "</li>")
        elif line.startswith("> "):
            flush_para(); flush_list()
            out.append("<blockquote>" + inline(line[2:]) + "</blockquote>")
        elif line.strip() == "":
            flush_para(); flush_list()
        else:
            flush_list()
            para.append(line.strip())
        i += 1
    flush_para(); flush_list()
    return "\n".join(out)

for md_path in sorted(glob.glob(os.path.join(SRC, "*.md"))):
    with open(md_path, encoding="utf-8") as f:
        md = f.read()
    # first line = title
    first_newline = md.find("\n")
    title = md[:first_newline].lstrip("# ").strip()
    body = convert(md[first_newline:])
    html = f"<h1>{title}</h1>\n{body}"
    name = os.path.splitext(os.path.basename(md_path))[0]
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK  {name}.html  ({len(html)} chars)  TITLE: {title}")
