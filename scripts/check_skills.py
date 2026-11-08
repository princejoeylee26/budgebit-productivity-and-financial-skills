#!/usr/bin/env python3
"""Repository checks for the hachibu skills. Run: python3 scripts/check_skills.py

1. Frontmatter: every SKILL.md has a valid name and description.
2. Links: every relative Markdown link resolves.
3. Shared files: copies match shared/ (run scripts/sync-shared.sh to fix).
4. Personal data: no emails, phone numbers, long digit runs, or blocked terms.
5. Size: SKILL.md bodies stay under 500 lines.
Exit code 1 on any failure.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
SHARED = ROOT / "shared"
errors = []

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<![\w.])\+?\d[\d \-]{9,}\d(?![\w.])")
SCAN_EXT = {".md", ".py", ".sh", ".json", ".yml", ".yaml", ".txt"}
SKIP_DIRS = {".git", "node_modules"}
ALLOWED_EMAILS = {"noreply@anthropic.com"}


def frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[end + 5:]


def check_skills():
    found = sorted(SKILLS.glob("*/SKILL.md"))
    if not found:
        errors.append("no skills found under .claude/skills")
    for path in found:
        rel = path.relative_to(ROOT)
        meta, body = frontmatter(path.read_text(encoding="utf-8"))
        if meta is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        name, desc = meta.get("name", ""), meta.get("description", "")
        if not NAME_RE.match(name):
            errors.append(f"{rel}: name must be lowercase letters, digits, hyphens, ≤64 chars")
        if "claude" in name or "anthropic" in name:
            errors.append(f"{rel}: name must not contain 'claude' or 'anthropic'")
        if name != path.parent.name:
            errors.append(f"{rel}: name '{name}' must match folder '{path.parent.name}'")
        if not desc or len(desc) > 1024:
            errors.append(f"{rel}: description must be 1–1024 chars (is {len(desc)})")
        if "<" in desc or ">" in desc:
            errors.append(f"{rel}: description must not contain angle brackets")
        if len(body.splitlines()) > 500:
            errors.append(f"{rel}: body over 500 lines")


def check_links():
    for path in ROOT.rglob("*.md"):
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (path.parent / file_part).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")


def check_shared():
    for shared in SHARED.glob("*.md"):
        for copy in SKILLS.glob(f"*/references/{shared.name}"):
            if copy.read_bytes() != shared.read_bytes():
                errors.append(f"{copy.relative_to(ROOT)}: out of sync with shared/ (run scripts/sync-shared.sh)")


def load_terms(name):
    f = ROOT / "scripts" / name
    if not f.exists():
        return []
    return [t.strip().lower() for t in f.read_text(encoding="utf-8").splitlines()
            if t.strip() and not t.startswith("#")]


def check_personal_data():
    terms = load_terms("blocklist.txt") + load_terms("blocklist.local.txt")
    skip = {ROOT / "scripts" / "blocklist.txt", ROOT / "scripts" / "blocklist.local.txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in SCAN_EXT or path in skip:
            continue
        if any(p in SKIP_DIRS for p in path.parts) or "memory" in path.relative_to(ROOT).parts[:1]:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for email in EMAIL_RE.findall(text):
            if email.lower() not in ALLOWED_EMAILS and not email.lower().endswith("@example.com"):
                errors.append(f"{rel}: email address found ({email})")
        for phone in PHONE_RE.findall(text):
            digits = re.sub(r"\D", "", phone)
            if len(digits) >= 10:
                errors.append(f"{rel}: possible phone or account number ({phone.strip()})")
        low = text.lower()
        for term in terms:
            if re.search(r"\b" + re.escape(term) + r"\b", low):
                errors.append(f"{rel}: blocked term found ('{term}')")


def main():
    check_skills()
    check_links()
    check_shared()
    check_personal_data()
    if errors:
        print("✗ checks failed:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"✓ all checks passed ({len(list(SKILLS.glob('*/SKILL.md')))} skills)")


if __name__ == "__main__":
    main()
