import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np

dataset = gdal.Open('rectified_image.tif')
band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()

plt.imshow(arr, cmap='gray')
plt.title('Rectified Image')
plt.axis('off')
plt.savefig('rectified_image_display.png', bbox_inches='tight', dpi=300)
print("✅ Saved 'rectified_image_display.png'. Open it to view the rectified output.")
