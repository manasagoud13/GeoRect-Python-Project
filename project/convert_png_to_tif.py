from PIL import Image

# Open your PNG image
img = Image.open('input_image.png')

# Convert to grayscale if needed
img = img.convert('L')

# Save as TIFF
img.save('input_image.tif', format='TIFF')

print("✅ Conversion complete. 'input_image.tif' is ready.")
