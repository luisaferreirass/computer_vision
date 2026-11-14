# Computer Vision

Hands-on assignments from the **Computer Vision** course (UFRN), implemented in Python with OpenCV, NumPy and Matplotlib. The repository covers everything from basic image generation and manipulation to noise filtering, edge detection and circle detection with the Hough Transform (including a custom implementation).

## Structure

```
computer_vision/
├── tarefa1/                 # Image generation and display, webcam + Canny
├── tarefa2/                 # Point operators and geometric transformations
├── tarefa3/                 # Edge detection and chessboard rotation
├── tarefa4/                 # Noise reduction (assignment: "Task 5")
├── tarefa6/                 # Counting colored discs with Hough
└── remocao_ruido_circulo/   # Center and radius estimation of noisy circles
```

Each folder contains the scripts, the test images (`imgs/`) and, when available, the assignment statement in `docs/`.

## Tasks

### Task 1 — Fundamentals
- **1A:** generates and displays 6 images of 280x200 in a grid (gray, white, vertical/horizontal stripes, checkerboard and random noise).
- **1B:** concatenates several image patches side by side.
- **1C:** webcam capture with the Canny filter applied, taking both thresholds as command-line arguments.

### Task 2 — Point operators and geometry
- **2A:** thresholding implemented pixel by pixel (no built-in function or matrix operation).
- **2B:** logarithmic and inverse logarithmic transformations for contrast enhancement.
- **2C:** histogram equalization.
- **2D:** reconstruction of an image from resized and rotated pieces (`resize`, `rotate`, `warpAffine`).
- **2E:** perspective correction to extract a book cover (`getPerspectiveTransform`, `warpPerspective`).

### Task 3 — Edges and gradient
- **3A:** Laplacian, Sobel in x and y, thresholded gradient magnitude and Canny with hysteresis.
- **3B:** estimates the rotation angle of a chessboard in [0, π/2) from the gradient direction (Sobel + `arctan2`).

### Task 4 / 5 — Noise reduction
- `gerarRuido.py` generates 6 noisy versions of an image (salt and pepper, Gaussian, salt, pepper, at different intensities).
- `atenuarRuido.py` applies the best filter found for each type of noise and displays the PSNR (`cv2.PSNR`) relative to the original image.

### Task 6 — Counting colored discs
Counts the red, yellow, green and blue discs in 8 images and compares the result with the answer key.
- Color segmentation in the **HSV** color space (one mask per color).
- Images 1–5: `cv2.HoughCircles` + grouping of the inner/outer circles of the same disc + ring validation on the mask to eliminate false positives.
- Images 6–8 (heavy overlap): **Hough Transform implemented from scratch**, exploiting the fact that each disc has an inner and an outer circle with a constant radius ratio (≈ 0.55). Each edge point votes for the center along the gradient direction, followed by non-maximum suppression.
- Output: count per color in the terminal/title and an image with the detected circles drawn, saved in `resultados/`.

### Noise removal and circle detection
Synthetic images of a circle with different kinds of noise (no noise, salt, pepper, salt and pepper, Gaussian) and `ground_truth.csv` with the true values. The scripts filter the image (Gaussian/median), estimate the circle's center and radius and draw the detected contour.

## How to run

Requirements: Python 3 and the libraries below.

```bash
pip install opencv-python numpy matplotlib
```

The scripts are run from inside each task's folder, for example:

```bash
cd tarefa1 && python 1C.py 100 200                 # Canny thresholds
cd tarefa4 && python atenuarRuido.py cristo.jpg 3  # reference image and noise index (0–5)
cd tarefa6 && python main.py imgs/7.jpg            # image to analyze
cd remocao_ruido_circulo && python ruido_gaussiano.py C_gaussiano_r060.png <cx> <cy> <r>
```

## Stack

Python · OpenCV · NumPy · Matplotlib
