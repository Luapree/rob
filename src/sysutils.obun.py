def apply_dialect(text: str) -> str:
    for original, replacement in dialect_map.items():
        pattern = r'\b' + re.escape(original) + r'\b'
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def guild_address(guild):
    slug = re.sub(r"[^a-z0-9]+", "-", guild.name.lower())
    slug = slug.strip("-")
    return f"{slug}-{str(guild.id)[-2:]}"
