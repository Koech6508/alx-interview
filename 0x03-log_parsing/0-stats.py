#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''
import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    try:
        parts = line.strip().split()
        ip_address = parts[0]
        date = parts[1][1:-1]
        request = parts[2][1:]
        status_code = int(parts[3])
        file_size = int(parts[4])

        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for code in sorted(status_code_counts):
                if status_code_counts[code] > 0:
                    print(f'{code}: {status_code_counts[code]}')

    except:
        continue

    # handle keyboard interrupt (CTRL + C)
    except KeyboardInterrupt:
        print(f'Total file size: {total_file_size}')
        for code in sorted(status_code_counts):
            if status_code_counts[code] > 0:
                print(f'{code}: {status_code_counts[code]}')
        sys.exit(0)

# print final statistics when stdin is closed
print(f'Total file size: {total_file_size}')
for code in sorted(status_code_counts):
    if status_code_counts[code] > 0:
        print(f'{code}: {status_code_counts[code]}')
