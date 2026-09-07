
print("=================================================")
print("Question 4")
print("=================================================")

from datetime import datetime
from collections import Counter


def find_peak_usage(logs):
    # Return an appropriate result if the list is empty
    if not logs:
        return None

    hours = []

    # Convert each timestamp and extract its hour
    for timestamp in logs:
        login_time = datetime.fromisoformat(timestamp)
        hours.append(login_time.hour)

    # Count the number of logins in each hour
    hour_counts = Counter(hours)

    # Find the highest number of logins
    highest_count = max(hour_counts.values())

    # Find all hours that have the highest number of logins
    peak_hours = [
        hour for hour, count in hour_counts.items()
        if count == highest_count]

    # Return the earliest hour if there is a tie
    return min(peak_hours)


# Example login timestamps
logs = ["2026-08-04T13:21:18","2026-08-04T13:45:10","2026-08-04T09:15:20","2026-08-04T13:55:30",
    "2026-08-04T09:35:40","2026-08-04T16:10:00"]

peak_hour = find_peak_usage(logs)

print("Peak login hour:", peak_hour)
