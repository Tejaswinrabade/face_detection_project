"""
Diagnostic script to test webcam access and find available cameras
Enhanced with DirectShow backend for Windows
"""
import cv2
import sys

def test_webcam():
    """Test different camera indices to find working webcams"""
    
    print("Testing webcam access...")
    print("=" * 60)
    print("\n🔍 Checking available cameras in system...")
    
    found_camera = False
    
    # Test with different backends on Windows
    backends = [
        (cv2.CAP_DSHOW, "DirectShow (Recommended for Windows)"),
        (cv2.CAP_MSMF, "Windows Media Foundation"),
        (cv2.CAP_ANY, "Auto-detect"),
    ]
    
    for backend, backend_name in backends:
        print(f"\n📡 Testing {backend_name}...")
        
        for i in range(3):
            print(f"  Camera index {i}...", end=" ")
            
            try:
                cap = cv2.VideoCapture(i, backend)
                
                if cap.isOpened():
                    ret, frame = cap.read()
                    
                    if ret and frame is not None:
                        print(f"✓ WORKS!")
                        print(f"    Resolution: {frame.shape[1]}x{frame.shape[0]}")
                        cap.release()
                        found_camera = True
                        print(f"\n✅ SUCCESS! Use camera index {i}")
                        return i
                    else:
                        print("✗ Can't read frames")
                        cap.release()
                else:
                    print("✗ Can't open")
            except Exception as e:
                print(f"✗ Error: {str(e)[:30]}")
    
    print("\n" + "=" * 60)
    if not found_camera:
        print("\n❌ No working cameras found!\n")
        print("TROUBLESHOOTING STEPS (try in order):\n")
        print("1️⃣  Close apps using camera:")
        print("   - Teams, Zoom, Discord, OBS, browser camera")
        print("   - Completely quit them (not just minimize)")
        print("   - Then run this script again\n")
        print("2️⃣  Check Windows Camera Permissions:")
        print("   - Settings > Privacy & Security > Camera")
        print("   - Enable 'Camera access'")
        print("   - Allow Python to access camera\n")
        print("3️⃣  Check Device Manager:")
        print("   - Right-click Windows Start > Device Manager")
        print("   - Look for 'Cameras' section")
        print("   - Check for warning icons (yellow ⚠ or red ❌)")
        print("   - If warning: right-click > Update driver\n")
        print("4️⃣  Update Camera Drivers:")
        print("   - Go to manufacturer's website")
        print("   - Download latest camera drivers\n")
        print("5️⃣  Allow Through Firewall/Antivirus:")
        print("   - Check if firewall/antivirus blocks Python\n")
        print("6️⃣  Restart Computer:")
        print("   - Windows sometimes locks camera resources\n")
        print("=" * 60)
        sys.exit(1)
    else:
        print("\n✅ Camera found and working!")
        sys.exit(0)

if __name__ == "__main__":
    test_webcam()
