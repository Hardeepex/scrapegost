from selectolax.parser import HTMLParser


def extract_css_selectors(html_content):
    parser = HTMLParser(html_content)

    def get_css_selector(node):
        parts = []
        while node:
            parts.insert(0, node.tag)
            node = node.parent
        return ' '.join(parts)

    css_selectors = set()
    for node in parser.root.iter():
        if node.tag:
            css_selector = get_css_selector(node)
            css_selectors.add(css_selector)

    return list(css_selectors)

if __name__ == "__main__":
    html_content = "<div><span class='test'>Hello, world!</span></div>"
    css_selectors = extract_css_selectors(html_content)
    print(css_selectors)
