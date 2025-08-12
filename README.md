A Python-based toolkit for georeferencing and rectifying aerial or satellite imagery using GDAL, OpenCV, and Ground Control Points (GCPs).
This project aligns raw raster images to real-world coordinates for accurate mapping and GIS analysis.
graph LR
    A[🖼 Raw Image] --> B[📍 GCP Collection]
    B --> C[⚙ Transformation Calculation]
    C --> D[🗺 Georeferenced Map]
✨ Features
📍 Georeferencing – Assigns spatial reference to raw imagery using GCPs.
🗺 Image Rectification – Warps images to match map projections.
⚙ GDAL & OpenCV – Combines GIS and computer vision capabilities.
🧮 Supports Affine and Homography-based transformations.
📂 Works with GeoTIFF and other raster formats

GeoRect/
│── main.py                # Main script for georeferencing & rectification
│── gcp_data.csv           # Ground Control Points (optional)
│── input_image.tif        # Sample raw image
│── output_image.tif       # Georeferenced image output
│── README.md              # Project documentation
