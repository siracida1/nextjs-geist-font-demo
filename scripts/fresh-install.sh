#!/bin/bash
# Exit immediately if any command fails
set -e

echo "Starting fresh install procedure..."

# Check and remove the node_modules/.cache directory if it exists
if [ -d "node_modules/.cache" ]; then
    echo "Removing node_modules/.cache..."
    rm -rf node_modules/.cache
else
    echo "node_modules/.cache does not exist. Skipping."
fi

# Check and remove the node_modules directory if it exists
if [ -d "node_modules" ]; then
    echo "Removing node_modules directory..."
    rm -rf node_modules
else
    echo "node_modules directory does not exist. Skipping."
fi

# Install production dependencies only (omitting dev dependencies)
echo "Installing production dependencies..."
npm install --omit=dev --legacy-peer-deps

echo "Fresh install complete."
