#!/usr/bin/env python3
"""Builds the three pages from content/*.md. Run: python3 build.py"""
import markdown, pathlib

ROOT = pathlib.Path(__file__).parent
EMAIL = "support@getfirstthought.com"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header>
<a class="brand" href="/">First Thought</a>
<nav><a href="/support/">Support</a><a href="/privacy/">Privacy policy</a></nav>
</header>
<main>
{body}
</main>
<footer>
<p>First Thought &middot; <a href="mailto:{email}">{email}</a></p>
</footer>
</body>
</html>
"""

def render(md_name, out_dir, title, description):
    body = markdown.markdown((ROOT / "content" / md_name).read_text(), extensions=["sane_lists"])
    html = PAGE.format(title=title, description=description, body=body, email=EMAIL)
    target = ROOT / out_dir
    target.mkdir(exist_ok=True)
    (target / "index.html").write_text(html)

render("privacy.md", "privacy", "Privacy policy - First Thought",
       "What First Thought does with your information: it stays on your phone.")
render("support.md", "support", "Support - First Thought",
       "Help with First Thought: alarms, the wake-up challenge, Pro purchases and your data.")

home = """<h1>First Thought</h1>
<p class="lede">An alarm that wakes you with a tone, then asks for a few kind words before it lets you go.</p>
<p>To switch the alarm off you tap through a short run of affirmations and type one yourself, so the first thing you read each day is something kind. It works on a locked or silent phone, and the alarm itself is never locked behind a payment.</p>
<p>Everything stays on your phone. There are no accounts, no ads and no tracking.</p>
<p><a href="/support/">Help and support</a> &middot; <a href="/privacy/">Privacy policy</a></p>
"""
(ROOT / "index.html").write_text(PAGE.format(
    title="First Thought - an alarm that wakes you with affirmations",
    description="An alarm that wakes you with a tone, then asks for a few kind words before it lets you go.",
    body=home, email=EMAIL))
