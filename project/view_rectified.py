import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np

# Open your rectified image
dataset = gdal.Open('rectified_image.tif')
if dataset is None:
    print("❌ Could not open 'rectified_image.tif'. Check if it exists.")
    exit()

band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()

# Plot and save instead of show
plt.imshow(arr, cmap='gray')
plt.title('Rectified Image')
plt.axis('off')

# Save the output
plt.savefig('rectified_image_display.png', bbox_inches='tight', dpi=300)
print("✅ Saved 'rectified_image_display.png'. You can double-click to view your rectified image.")
