def markdown_to_blocks(markdown: str) -> list[str]:
    md_blocks = []
    for string in markdown.split("\n\n"):
        if string == "":
            continue
        block = string.strip()
        md_blocks.append(block)
    return md_blocks