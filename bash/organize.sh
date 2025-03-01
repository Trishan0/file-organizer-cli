#!/bin/bash

echo "Hello, this is a simple file organizer!"

log_file="file_organizer.log"
script_dir="$(dirname "$(realpath "$0")")"
config_file="$script_dir/categories.conf"

# Get directory from user or use the current directory
read -p "Enter directory path (leave empty for current directory): " target_dir
target_dir="${target_dir:-.}"

# Check if directory exists
if [ ! -d "$target_dir" ]; then
    echo "[$(date)] ERROR: Directory '$target_dir' does not exist." | tee -a "$log_file"
    exit 1
fi

# Check if the config file exists
if [ ! -f "$config_file" ]; then
    echo "[$(date)] ERROR: Config file '$config_file' not found!" | tee -a "$log_file"
    exit 1
fi

# Declare associative array
declare -A categories

# Read categories from config file
while IFS='=' read -r category exts; do
    categories["$category"]="$exts"
done < "$config_file"

echo "[$(date)] Organizing files in: $target_dir" > "$log_file"

# Process each category
for category in "${!categories[@]}"; do
    category_dir="$target_dir/$category"

    # Create directory if it does not exist
    [ ! -d "$category_dir" ] && mkdir -p "$category_dir"

    # Move files based on extensions
    for ext in ${categories[$category]}; do
        for file in "$target_dir"/*"$ext"; do
            if [ -e "$file" ]; then
                mv "$file" "$category_dir/"
                echo "[$(date)] Moved $file to $category_dir/" | tee -a "$log_file"
            fi
        done
    done
done

echo "[$(date)] Script completed." | tee -a "$log_file"

