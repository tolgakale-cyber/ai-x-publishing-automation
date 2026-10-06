import os
import uuid
from datetime import datetime

from src.x_connector import XConnector


def publish_post(post):
    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"

    connector = XConnector()
    connection = connector.connection_status()

    if dry_run:
        post_id = f"DEMO-{uuid.uuid4().hex[:8].upper()}"

        return {
            "platform": connection["platform"],
            "connection_status": connection["status"],
            "status": "SIMULATED",
            "post_id": post_id,
            "content": post,
            "published": False,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

    live_result = connector.publish(post)

    return {
        "platform": connection["platform"],
        "connection_status": connection["status"],
        "status": "LIVE_REQUEST_BLOCKED",
        "post_id": None,
        "content": post,
        "published": live_result["success"],
        "reason": live_result["reason"],
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
    }