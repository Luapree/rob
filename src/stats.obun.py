guild_daily_stats = defaultdict(int)
stats_day = datetime.utcnow().date()

def reset_stats():
    global stats_day, guild_daily_stats

    today = datetime.utcnow().date()

    if today != stats_day:
        guild_daily_stats.clear()
        stats_day = today
