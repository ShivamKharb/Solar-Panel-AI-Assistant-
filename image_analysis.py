# image_analysis.py

import numpy as np
import cv2

def analyze_rooftop(image_pil):
    import numpy as np

    image_np = np.array(image_pil)
    height, width, _ = image_np.shape

    # Assume 0.1 m² per pixel at 300 dpi → for real estimation you need scale metadata
    pixel_area = 0.05  # This is an assumption; you can calibrate this

    total_area = height * width * pixel_area
    usable_area = total_area * 0.6

    return {
        "total_area_m2": round(total_area, 2),
        "usable_area_m2": round(usable_area, 2),
        "obstacles": "Estimated heuristically"
    }

def generate_roi_mask(image_pil):
    import cv2
    import numpy as np

    image = np.array(image_pil.convert("L"))  # convert to grayscale
    image = cv2.GaussianBlur(image, (5, 5), 0)

    # Adaptive threshold for dynamic region extraction
    mask = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 3
    )

    # Optional: clean mask using morphological operations
    kernel = np.ones((5, 5), np.uint8)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return cleaned
