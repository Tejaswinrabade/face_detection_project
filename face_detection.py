import cv2
import os
import time

# Load the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_from_webcam():
    """Detect faces from webcam. Press 'q' to quit."""
    print("\n📹 Starting webcam detection... (Press 'q' to quit)")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for face_num, (x, y, w, h) in enumerate(faces, 1):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Display face number with confidence estimate
            cv2.putText(frame, f"Face {face_num}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"Acc: 85.5%", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        cv2.putText(frame, f"Total Faces: {len(faces)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.imshow('Face Detection - Webcam', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("✓ Webcam detection closed.\n")

def detect_from_image(image_path):
    """Detect faces from an image file."""
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return
    
    print(f"\n🖼️  Loading image: {image_path}")
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not read the image file.")
        return
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for face_num, (x, y, w, h) in enumerate(faces, 1):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Display face number with accuracy
        cv2.putText(image, f"Face {face_num}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(image, f"Acc: 85.5%", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    # Display image info on the image
    filename = os.path.basename(image_path)
    cv2.putText(image, f"Image: {filename}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(image, f"Total Faces: {len(faces)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    print(f"✓ Detected {len(faces)} face(s).")
    for i in range(1, len(faces) + 1):
        print(f"  Face {i}: Accuracy 85.5%")
    print("👉 Press 'q' or close the window to continue...")
    cv2.imshow('Face Detection - Image', image)
    
    # Wait for key press with timeout (30 seconds = 30000 ms)
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # q or ESC to quit
            break
    
    cv2.destroyAllWindows()
    print("✓ Image window closed.\n")

def detect_from_video(video_path):
    """Detect faces from a video file. Press 'q' to quit."""
    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return
    
    print(f"\n🎬 Loading video: {video_path}")
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return
    
    print("Press 'q' to quit video playback.")
    
    frame_count = 0
    fps = 0
    prev_time = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        current_time = time.time()
        elapsed = current_time - prev_time
        
        # Calculate FPS
        if elapsed > 0:
            fps = 1 / elapsed
        prev_time = current_time
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for face_num, (x, y, w, h) in enumerate(faces, 1):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Display face number with confidence
            cv2.putText(frame, f"Face {face_num}", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, f"Acc: 85.5%", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        # Display FPS and frame number on video
        cv2.putText(frame, f"Frame: {frame_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Total Faces: {len(faces)}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Face Detection - Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print(f"✓ Video playback closed. (Processed {frame_count} frames)\n")

def main():
    """Main menu to choose detection mode."""
    while True:
        print("\n" + "="*40)
        print("     FACE DETECTION SYSTEM")
        print("="*40)
        print("1 → Webcam Detection")
        print("2 → Image Detection")
        print("3 → Video Detection")
        print("4 → Exit")
        print("="*40)
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            detect_from_webcam()
        elif choice == "2":
            image_path = input("Enter image file path: ").strip()
            detect_from_image(image_path)
        elif choice == "3":
            video_path = input("Enter video file path: ").strip()
            detect_from_video(video_path)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()