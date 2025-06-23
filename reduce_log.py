from pathlib import Path

# Get the directory of the current script
base_dir = Path(__file__).resolve().parent  # adjust as needed

# Construct the log file path relative to the script
log_dir = base_dir / 'logs'
log_dir.mkdir(parents=True, exist_ok=True)  # Ensure the logs directory exists
log_path = log_dir / 'spatial_functions.log'

with log_path.open('r', encoding='utf-8') as f:
    lines = f.readlines()

target_length = len("2025-06-21 10:19:11,982 INFO watchfiles.main 1 change detected")

with log_path.open('w', encoding='utf-8') as f:
    for line in lines:
        if len(line.rstrip('\n')) != target_length:
            f.write(line)