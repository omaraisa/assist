import os
import datetime
from pathlib import Path


def clean_old_logs(log_file_path, days=3):
    """Clean log entries older than the specified number of days."""
    if not os.path.exists(log_file_path):
        return

    cutoff = datetime.datetime.now() - datetime.timedelta(days=days)
    with open(log_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    found_recent = False
    for line in lines:
        try:
            timestamp_str = line[:19]  # First 19 characters
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            if timestamp >= cutoff:
                found_recent = True
                new_lines.append(line)
            elif found_recent:
                # Keep lines after the first recent date, even if no date
                new_lines.append(line)
            # else skip old lines
        except ValueError:
            if found_recent:
                # Keep lines without dates if after the first recent date
                new_lines.append(line)
            # else skip

    with open(log_file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    log_file_path = Path(__file__).parent.parent / "logs" / "system.log"
    clean_old_logs(log_file_path, days=3)
    print("Old logs cleaned successfully.")
