# 🎥 Video Testing Guide - NewsExplorerHindi

Welcome! This guide will help you add and test videos in the NewsExplorerHindi project.

---

## 📁 Directory Structure for Videos

Create this folder structure in your local repository:

```
My-workplace-/
├── test_videos/
│   ├── sample_news.mp4
│   ├── breaking_news.mp4
│   ├── press_conference.mp4
│   └── interview.mp4
├── camera_feeds/
│   ├── camera_1.mp4
│   ├── camera_2.mp4
│   ├── camera_3.mp4
│   └── camera_4.mp4
├── recordings/
│   ├── multi_cam_session_001.mp4
│   └── live_broadcast_001.mp4
└── README.md
```

---

## 🚀 Quick Start Steps

### Step 1: Create Video Directories
```bash
# Navigate to your repository
cd My-workplace-

# Create necessary folders
mkdir -p test_videos
mkdir -p camera_feeds
mkdir -p recordings
mkdir -p config

echo "Test videos directory" > test_videos/README.txt
echo "Camera feeds directory" > camera_feeds/README.txt
```

### Step 2: Add Your Video Files

You can add videos in multiple ways:

#### **Method A: From Local Files**
```bash
# Copy your video files to test_videos folder
cp /path/to/your/video.mp4 test_videos/

# Or directly add files to camera_feeds
cp /path/to/camera1.mp4 camera_feeds/camera_1.mp4
cp /path/to/camera2.mp4 camera_feeds/camera_2.mp4
```

#### **Method B: Generate Test Videos (Python)**
```bash
# Create a simple test video generator script
python -c "
import cv2
import numpy as np

# Create a test video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test_videos/sample_news.mp4', fourcc, 30.0, (1280, 720))

for i in range(300):  # 10 seconds at 30fps
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    cv2.putText(frame, f'Test Video Frame {i}', (50, 360), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    out.write(frame)

out.release()
print('Test video created: test_videos/sample_news.mp4')
"
```

### Step 3: Configure Video Settings

Create a configuration file `config/video_config.json`:

```json
{
  "test_videos": [
    {
      "id": 1,
      "name": "sample_news",
      "path": "test_videos/sample_news.mp4",
      "description": "Sample news video for testing",
      "duration": "10 seconds",
      "resolution": "1280x720",
      "fps": 30
    },
    {
      "id": 2,
      "name": "breaking_news",
      "path": "test_videos/breaking_news.mp4",
      "description": "Breaking news test video",
      "duration": "30 seconds",
      "resolution": "1920x1080",
      "fps": 30
    }
  ],
  "camera_feeds": [
    {
      "id": 1,
      "name": "Main Camera",
      "path": "camera_feeds/camera_1.mp4",
      "resolution": "1920x1080",
      "fps": 30
    },
    {
      "id": 2,
      "name": "Side Camera",
      "path": "camera_feeds/camera_2.mp4",
      "resolution": "1280x720",
      "fps": 30
    }
  ]
}
```

### Step 4: Test Video Playback (Python)

Create `test_video_player.py`:

```python
import cv2
import os

def test_video_playback(video_path):
    """Test if video can be played"""
    
    if not os.path.exists(video_path):
        print(f"❌ Video not found: {video_path}")
        return False
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"❌ Cannot open video: {video_path}")
        return False
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    
    print(f"✅ Video loaded: {video_path}")
    print(f"   Resolution: {width}x{height}")
    print(f"   FPS: {fps}")
    print(f"   Frames: {frame_count}")
    print(f"   Duration: {duration:.2f} seconds")
    
    cap.release()
    return True

# Test all videos
videos_to_test = [
    "test_videos/sample_news.mp4",
    "camera_feeds/camera_1.mp4",
    "camera_feeds/camera_2.mp4"
]

print("🎬 Testing Video Files...\n")
for video in videos_to_test:
    test_video_playback(video)
    print()
```

Run it:
```bash
python test_video_player.py
```

### Step 5: Upload to GitHub

```bash
# Check git status
git status

# Add all new files
git add test_videos/
git add camera_feeds/
git add config/
git add VIDEO_TESTING_GUIDE.md
git add test_video_player.py

# Commit changes
git commit -m "Add video testing directories and configuration"

# Push to repository
git push origin main
```

---

## 📊 Video Requirements for Different Use Cases

### For News Articles
- **Format:** MP4
- **Resolution:** 1280x720 or 1920x1080
- **Duration:** 30 seconds to 5 minutes
- **File Size:** 10-50 MB

### For Multi-Camera Setup
- **Format:** MP4
- **Resolution:** 1920x1080 (Main), 1280x720 (Secondary)
- **Duration:** Any
- **Sync:** Ensure frame synchronization
- **File Size:** Depends on duration

### For Live Stream Testing
- **Format:** MP4 or RTMP stream
- **Resolution:** 1920x1080 (recommended)
- **FPS:** 30 or 60
- **Bitrate:** 5-10 Mbps

---

## 🔧 Using Videos in Your Project

### Load Video in Python
```python
import cv2

# Load video
cap = cv2.VideoCapture('test_videos/sample_news.mp4')

# Read frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Process frame (add nameplate, effects, etc.)
    # cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### With Multi-Camera System
```python
from camera.multi_capture import MultiCameraCapture

# Use video files as camera sources
sources = [
    'camera_feeds/camera_1.mp4',
    'camera_feeds/camera_2.mp4',
    'camera_feeds/camera_3.mp4',
    'camera_feeds/camera_4.mp4'
]

capture = MultiCameraCapture(camera_sources=sources)
frames = capture.get_frames()
```

---

## 🎯 Next Steps

1. ✅ Create video directories
2. ✅ Add your test video files
3. ✅ Create `video_config.json`
4. ✅ Test video playback with Python script
5. ✅ Push to GitHub
6. ✅ Test multi-camera functionality
7. ✅ Add nameplates to videos
8. ✅ Record and save processed videos

---

## 📝 Troubleshooting

### Video Won't Play
```bash
# Check if file exists
ls -lh test_videos/

# Verify video format
file test_videos/sample_news.mp4

# Check with ffprobe
ffprobe -v error -show_format -show_streams test_videos/sample_news.mp4
```

### Large File Size
```bash
# Compress video before uploading
ffmpeg -i input.mp4 -vcodec h264 -acodec mp2 output.mp4

# Or use GitHub Large File Storage (LFS)
git lfs install
git lfs track "*.mp4"
```

### OpenCV Can't Read Video
```bash
# Ensure FFmpeg is installed
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

---

## 💡 Tips

- Use **short test videos (10-30 seconds)** for quick testing
- Keep **original quality** for important recordings
- Use **compression** before pushing large files
- Create **separate folders** for different video types
- Document **video metadata** in config files
- Test **across different resolutions**

---

Happy testing! 🚀

For more help, check the [Multi-Camera Guide](./README.md#-multi-camera-capture-frame-with-nameplates)
