from datetime import datetime


def schedule_post(post, scheduled_time):
    try:
        run_at = datetime.strptime(
            scheduled_time,
            "%Y-%m-%d %H:%M",
        )
    except ValueError:
        return {
            "scheduled": False,
            "error": "Invalid date format. Use YYYY-MM-DD HH:MM.",
        }

    if run_at <= datetime.now():
        return {
            "scheduled": False,
            "error": "Scheduled time must be in the future.",
        }

    return {
        "scheduled": True,
        "content": post,
        "scheduled_time": run_at.isoformat(timespec="minutes"),
        "status": "QUEUED",
    }