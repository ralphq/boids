#!/bin/bash

# This script converts the generated frames to
# .mp4 and .gif files
# NOTE: This script is mostly AI-generated.

# exit immediately if a command exits with a non-zero status.
set -e

# variables (You can modify these as needed)
FRAME_RATE=30
SCALE_WIDTH=640
FRAMES_DIR="frames"  # directory containing the frames
IMAGE_PATTERN="frames/frame_%03d.png"  # adjust based on your file naming pattern
MP4_OUTPUT="boids.mp4"
GIF_OUTPUT="boids.gif"
PALETTE_FILE="palette.png"

# check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg is not installed. Please install ffmpeg to proceed."
    exit 1
fi

# convert frames to MP4 video
echo "Converting image frames to MP4 video..."
ffmpeg -y -framerate "$FRAME_RATE" -i "$IMAGE_PATTERN" -c:v libx264 -pix_fmt yuv420p "$MP4_OUTPUT"

# generate color palette for GIF optimization
echo "Generating color palette for GIF..."
ffmpeg -y -i "$MP4_OUTPUT" -vf "fps=$FRAME_RATE,scale=$SCALE_WIDTH:-1:flags=lanczos,palettegen" "$PALETTE_FILE"

# create looping GIF using the palette
echo "Creating looping GIF..."
ffmpeg -y -i "$MP4_OUTPUT" -i "$PALETTE_FILE" -filter_complex "fps=$FRAME_RATE,scale=$SCALE_WIDTH:-1:flags=lanczos[x];[x][1:v]paletteuse" -loop 0 "$GIF_OUTPUT"

# remove temporary palette file
rm "$PALETTE_FILE"

# safety check before deleting frames directory
if [ "$FRAMES_DIR" == "" ] || [ "$FRAMES_DIR" == "/" ]; then
    echo "Error: FRAMES_DIR is not set correctly. Aborting deletion."
    exit 1
fi

# delete the frames directory
echo "Deleting frames directory..."
rm -rf "$FRAMES_DIR"

echo "Conversion complete!"
echo "MP4 video saved as: $MP4_OUTPUT"
echo "Looping GIF saved as: $GIF_OUTPUT"
