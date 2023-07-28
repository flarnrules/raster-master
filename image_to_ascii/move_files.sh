
# Define the source and destination directories
src="/mnt/c/Users/breif/Pictures/ASCII"
dst="/home/flarnrules/repos/raster-master/image_to_ascii/images/"

# Use rsync to copy the files
rsync -a "$src" "$dst"