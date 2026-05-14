"""
Script to create test image and video files for face detection
"""
import cv2
import numpy as np

def create_test_image():
    """Create a simple test image"""
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    img[:] = (200, 200, 200)  # Light gray background
    
    # Draw rectangles to simulate face regions
    cv2.rectangle(img, (100, 100), (300, 300), (100, 100, 100), -1)  # Face
    cv2.circle(img, (150, 150), 20, (50, 50, 50), -1)  # Left eye
    cv2.circle(img, (250, 150), 20, (50, 50, 50), -1)  # Right eye
    cv2.rectangle(img, (150, 250), (250, 280), (50, 50, 50), -1)  # Mouth
    
    cv2.imwrite('test_image.jpg', img)
    print("✓ Created: test_image.jpg")

def create_test_video():
    """Create a simple test video with moving rectangles"""
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('test_video.mp4', fourcc, 20.0, (640, 480))
    
    # Create 100 frames
    for frame_num in range(100):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        frame[:] = (200, 200, 200)  # Light gray background
        
        # Move a rectangle across the screen (to simulate face movement)
        x = 100 + (frame_num * 3)
        if x > 500:
            x = 100
        
        cv2.rectangle(frame, (x, 150), (x + 150, 300), (100, 100, 100), -1)
        cv2.circle(frame, (x + 40, 190), 15, (50, 50, 50), -1)
        cv2.circle(frame, (x + 110, 190), 15, (50, 50, 50), -1)
        
        out.write(frame)
    
    out.release()
    print("✓ Created: test_video.mp4")

if __name__ == "__main__":
    print("Creating test files...\n")
    create_test_image()
    create_test_video()
    print("\n✓ All test files created successfully!")
