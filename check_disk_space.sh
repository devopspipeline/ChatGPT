#!/bin/bash

# You can specify the path to check disk space using the -p option. If no path is specified, it defaults to /.
# For example: ./check_disk_space.sh -p /mnt/data

# Function to print usage information
usage() {
    echo "Usage: $0 [-h] [-p PATH]"
    echo "  -h              Display this help message"
    echo "  -p PATH         Specify the path to check disk space (default: /)"
    exit 1
}

# Parse command-line options
while getopts ":hp:" opt; do
    case ${opt} in
        h )
            usage
            ;;
        p )
            PATH_TO_CHECK=$OPTARG
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            usage
            ;;
        : )
            echo "Option -$OPTARG requires an argument." 1>&2
            usage
            ;;
    esac
done
shift $((OPTIND -1))

# If no path is specified, default to /
if [ -z "$PATH_TO_CHECK" ]; then
    PATH_TO_CHECK="/"
fi

# Check disk space
echo "Disk space on $PATH_TO_CHECK:"
df -h $PATH_TO_CHECK
