with open(r'E:\GISApp\AI\Smart Assistant\assist\logs\spatial_functions.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()

target_length = len("2025-06-21 10:19:11,982 INFO watchfiles.main 1 change detected")

with open(r'E:\GISApp\AI\Smart Assistant\assist\logs\spatial_functions.log', 'w', encoding='utf-8') as f:
    for line in lines:
        if len(line.rstrip('\n')) != target_length:
            f.write(line)