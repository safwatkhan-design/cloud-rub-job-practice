from datetime import datetime, timezone

print("Cloud Run Job started")
print(f"Current UTC time: {datetime.now(timezone.utc).isoformat()}")
print("Cloud Run Job finished successfully")