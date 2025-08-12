import matplotlib.pyplot as plt
import cv2
import numpy as np
from osgeo import gdal

print("✅ Step 0: Libraries imported successfully")

# ----------------- Step 1: Load the image using GDAL -----------------
image_path = 'input_image.tif'
dataset = gdal.Open(image_path)

if dataset is None:
    print("❌ Failed to open input_image.tif. Check file existence and GDAL support.")
    exit()

print("✅ Step 1: Image loaded using GDAL")

band = dataset.GetRasterBand(1)
image = band.ReadAsArray()

# Normalize to 8-bit if needed
image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite("input_image_display.png", image)
print("✅ Debug: Saved input_image_display.png")

# Paste this:
print("✅ Debug: Image shape:", image.shape)
print("✅ Debug: Min pixel value:", np.min(image))
print("✅ Debug: Max pixel value:", np.max(image))
print("✅ Debug: Mean pixel value:", np.mean(image))
plt.imshow(image, cmap='gray')
plt.title("✅ Preview: Input image before rectification")
plt.show()

print("✅ Step 1b: Image normalized")

# ----------------- Step 2: Define Ground Control Points (GCPs) -----------------
h, w = image.shape  # Get the image height and width

src_points = np.array([
    [0, 0],           # top-left
    [w - 1, 0],       # top-right
    [0, h - 1],       # bottom-left
    [w - 1, h - 1]    # bottom-right
], dtype=np.float32)

dst_points = np.array([
    [10, 10],
    [w - 10, 10],
    [10, h - 10],
    [w - 10, h - 10]
], dtype=np.float32)

print("✅ Step 2: GCPs defined")

# ----------------- Step 3: Compute Homography -----------------

# Check if the source points are valid by visualizing them
plt.imshow(image, cmap='gray')
plt.scatter(src_points[:, 0], src_points[:, 1], c='red', marker='o')
plt.title("Check: Red dots = src_points")
plt.show()

H, status = cv2.findHomography(src_points, dst_points)
print("✅ Step 3: Homography computed")

# ----------------- Step 4: Warp the image -----------------
height, width = image.shape
warped_image = cv2.warpPerspective(image, H, (width, height))
cv2.imwrite("rectified_image_display.png", warped_image)
print("✅ Debug: Saved rectified_image_display.png")

print("✅ Step 4: Image warped")

# ----------------- Step 5: Save the rectified image using GDAL -----------------
driver = gdal.GetDriverByName('GTiff')
out_dataset = driver.Create('rectified_image.tif',
                            width, height, 1, gdal.GDT_Byte)

if out_dataset is None:
    print("❌ Failed to create rectified_image.tif. Check GDAL installation and write permissions.")
    exit()

out_band = out_dataset.GetRasterBand(1)
out_band.WriteArray(warped_image)
print("✅ Step 5a: Data written to TIFF")

# Optionally copy projection and geotransform from the source if applicable
if dataset.GetGeoTransform():
    out_dataset.SetGeoTransform(dataset.GetGeoTransform())
if dataset.GetProjection():
    out_dataset.SetProjection(dataset.GetProjection())

out_band.FlushCache()
out_dataset.FlushCache()

print("✅ Step 5b: rectified_image.tif saved successfully. Check your folder now.")
