import argparse
import os

# To run the script, save it to a file (e.g., check_disk_space.py) and execute it using Python:
# python check_disk_space.py -p /mnt/data

def check_disk_space(path='/'):
    # Get disk space information
    disk_info = os.statvfs(path)
    block_size = disk_info.f_frsize
    total_space = disk_info.f_blocks * block_size
    free_space = disk_info.f_bavail * block_size
    used_space = (disk_info.f_blocks - disk_info.f_bfree) * block_size
    percent_used = (used_space / total_space) * 100

    # Convert bytes to GB
    total_space_gb = total_space / (1024 ** 3)
    free_space_gb = free_space / (1024 ** 3)
    used_space_gb = used_space / (1024 ** 3)

    # Print disk space information
    print(f"Disk space on {path}:")
    print(f"Total: {total_space_gb:.2f} GB")
    print(f"Used: {used_space_gb:.2f} GB")
    print(f"Free: {free_space_gb:.2f} GB")
    print(f"Percent used: {percent_used:.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check disk space')
    parser.add_argument('-p', '--path', type=str, default='/', help='Path to check disk space (default: /)')
    args = parser.parse_args()

    check_disk_space(args.path)
