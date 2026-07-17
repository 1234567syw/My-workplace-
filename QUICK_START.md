# 🎥 Quick Start Guide - Adding & Testing Videos

Welcome to NewsExplorerHindi! Here's your step-by-step guide to add and test videos.

---

## 📋 What You Have Now

✅ **VIDEO_TESTING_GUIDE.md** - Complete documentation  
✅ **test_video_tool.py** - Python testing script  
✅ **Directory structure** - Ready for your videos  

---

## 🚀 Get Started in 5 Minutes

### **Step 1: Run the Setup Script** (2 mins)

```bash
# Navigate to your repository
cd My-workplace-

# Run the video testing tool
python test_video_tool.py
```

**What this does:**
- ✅ Creates `test_videos/`, `camera_feeds/`, `recordings/`, `config/` folders
- ✅ Generates a sample test video automatically
- ✅ Creates `config/video_config.json`
- ✅ Tests all videos and shows results

### **Step 2: Add Your Own Videos** (1 min)

Copy your video files to the appropriate folders:

```bash
# Add test videos
cp your_video.mp4 test_videos/

# Add camera feeds
cp camera1.mp4 camera_feeds/camera_1.mp4
cp camera2.mp4 camera_feeds/camera_2.mp4

# Add recordings
cp recording.mp4 recordings/
```

**Supported Formats:** `.mp4`, `.avi`, `.mov`, `.mkv`

### **Step 3: Test Your Videos** (1 min)

```bash
# Test all videos again
python test_video_tool.py
```

You'll see:
```
✅ VALID: test_videos/your_video.mp4
   📊 Resolution: 1920x1080
   ⏱️  FPS: 30
   📹 Frames: 900
   ⏳ Duration: 30.00 seconds
   💾 File Size: 45.32 MB
```

### **Step 4: Update Configuration** (1 min)

Edit `config/video_config.json` to add your videos:

```json
{
  "test_videos": [
    {
      "id": 1,
      "name": "breaking_news",
      "path": "test_videos/your_video.mp4",
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
    }
  ]
}
```

---

## 📤 Push to GitHub

```bash
# Check what changed
git status

# Add all files
git add test_videos/
git add camera_feeds/
git add config/
git add QUICK_START.md

# Commit with message
git commit -m "Add video testing setup and sample videos"

# Push to GitHub
git push origin main
```

---

## ✨ Next Steps

### **Option A: Test Multi-Camera Setup**
```bash
python -c "
from camera.multi_capture import MultiCameraCapture
capture = MultiCameraCapture(
    camera_sources=['camera_feeds/camera_1.mp4', 'camera_feeds/camera_2.mp4']
)
frames = capture.get_frames()
print(f'Captured {len(frames)} frames from {len(frames)} cameras')
"
```

### **Option B: Add Nameplates to Videos**
Check [README.md](./README.md#-multi-camera-capture-frame-with-nameplates) for nameplate overlay instructions.

### **Option C: Create Your Own Script**
```python
import cv2

# Load your video
cap = cv2.VideoCapture('test_videos/your_video.mp4')

# Read and process frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Your processing here
    # Add nameplates, effects, analysis, etc.
    
    # Save or display
    # cv2.imshow('Frame', frame)

cap.release()
```

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Video file not found" | Check file path: `ls test_videos/` |
| "Cannot open video" | Ensure OpenCV is installed: `pip install opencv-python` |
| "Codec error" | Install FFmpeg: `sudo apt-get install ffmpeg` |
| "Large file size" | Compress: `ffmpeg -i input.mp4 -vcodec h264 output.mp4` |

---

## 📚 Learn More

- **[Full Testing Guide](./VIDEO_TESTING_GUIDE.md)** - Detailed documentation
- **[Multi-Camera Setup](./README.md#-multi-camera-capture-frame-with-nameplates)** - Camera configuration
- **[Nameplate Guide](./README.md#-multi-camera-capture-frame-with-nameplates)** - Add names/titles to videos

---

## 🎯 Your Video Testing Checklist

- [ ] Run `python test_video_tool.py`
- [ ] Verify directories are created
- [ ] Add your video files
- [ ] Run test tool again to validate
- [ ] Update `config/video_config.json`
- [ ] Commit and push to GitHub
- [ ] Test multi-camera functionality (optional)
- [ ] Add nameplates (optional)

---

## 💡 Pro Tips

✨ **Keep it simple** - Start with 1-2 videos  
✨ **Use short clips** - 10-30 seconds for quick testing  
✨ **Standard resolution** - 1280x720 or 1920x1080  
✨ **30 FPS** - Standard frame rate for news video  
✨ **Document everything** - Update config.json as you add videos  

---

**Ready to add videos? Run this now:**
```bash
python test_video_tool.py
```

Happy testing! 🚀
