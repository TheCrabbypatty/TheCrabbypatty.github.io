from datetime import datetime, timezone

page_path = "index.html"

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

start = "<!-- TIMESTAMP_START -->"
end = "<!-- TIMESTAMP_END -->"

new_section = f"{start}\n  <p>Last updated: {now}</p>\n  {end}"

with open(page_path, "r", encoding="utf-8") as file:
    page = file.read()

if start in page and end in page:
    before, remainder = page.split(start, 1)
    _, after = remainder.split(end, 1)
    page = before + new_section + after
else:
    page = page.replace("</body>", f"{new_section}\n</body>", 1)

with open(page_path, "w", encoding="utf-8") as file:
    file.write(page)
