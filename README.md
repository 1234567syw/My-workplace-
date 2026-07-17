<marquee direction="right" behavior="scroll" scrollamount="5" style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); padding: 10px; color: white; font-weight: bold; font-size: 16px; margin: 0;">
  🔥 Breaking News Updates | Latest Stories | Fact-Checking | Multi-Camera Coverage 🔥
</marquee>

<p align="center">
  <img src="logo newpaper.png" width="200">
</p>

<h1 align="center">NewsExplorerHindi</h1>

<p align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/1234567syw/My-workplace-?style=flat-square">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/1234567syw/My-workplace-?style=flat-square">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/1234567syw/My-workplace-?style=flat-square">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/1234567syw/My-workplace-?style=flat-square">
</p>

<p align="center"><b>Har khabar ko samajhna, har sach ko dhoondhna.</b></p>

---

## 📌 About This Channel
NewsExplorerHindi ek modern news‑explorer channel hai jahan har khabar ko analyse, question, understand ke approach se decode kiya jata hai. Hum breaking news, in-depth analysis aur fact-checking ke through authentic information provide karte hain.

---

## ✨ Features
- 📰 **Real-time News Updates**: Taze khabren har waqt par
- 🔍 **Fact Checking**: Khabron ki satyta ki gahrai se jaach
- 📊 **Data Analysis**: Informative charts aur statistics
- 🌐 **Multi-source Coverage**: Alag-alag sources se comparison
- 🎯 **Categorized News**: Politics, Technology, Sports, Business, Entertainment
- 💬 **User Comments**: Samaj se interact karein
- 📹 **Multi-Camera Capture**: Real-time video coverage se multiple sources
- 🏷️ **Dynamic Nameplates**: Live name & designation overlay on all frames

---

## 📦 Installation

### Step 1: Prerequisites Check
Make sure aapke paas following installed ho:
- Python 3.8 ya usse upar
- Node.js 14.0 ya usse upar
- Git
- pip (Python package manager)
- OpenCV (cv2) - Multi-camera support ke liye
- Pillow - Image processing ke liye

### Step 2: Repository Clone Kare
```bash
git clone https://github.com/1234567syw/My-workplace-.git
cd My-workplace-
```

### Step 3: Virtual Environment Setup
```bash
# Windows ke liye
python -m venv venv
venv\Scripts\activate

# Mac/Linux ke liye
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Dependencies Install Kare
```bash
pip install -r requirements.txt
```

### Step 5: Environment Variables Configure Kare
```bash
# .env file create kare
cp .env.example .env

# Apne API keys aur credentials add kare
nano .env
```

### Step 6: Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Step 7: Server Start Kare
```bash
python manage.py runserver
```

---

## 🚀 Usage

### Step 1: Home Page Visit Kare
Browser mein jaaye:
```
http://localhost:8000
```

### Step 2: News Explore Kare
- Homepage par breaking news aur trending stories dekh sakte ho
- Search bar use karke specific topics find kar sakte ho
- Categories se filter kare (Politics, Tech, Sports, etc.)

### Step 3: Article Padhen
- Kisi bhi article par click kare
- In-depth analysis aur source links dekhen
- Comments section mein apni raay share kare

### Step 4: Fact-Checking Tool Use Kare
```bash
# CLI se fact-check kare
python manage.py fact_check --query "khabar ka headline"
```

### Step 5: Subscribe To Updates
- Newsletter ke liye apna email register kare
- Daily news digest receive kare
- Push notifications enable kare

### Step 6: Admin Panel Access Kare
```
http://localhost:8000/admin
superuser credentials se login kare
```

---

## 📹 Multi-Camera Capture Frame with Nameplates

### Overview
Multi-Camera Capture Frame feature multiple video sources ko simultaneously capture aur display karta hai. Ye live events, conferences, aur breaking news coverage ke liye ideal hai. Ab har camera frame par dynamic nameplates (naam aur designation) automatically display hote hain.

### Features
- **Multi-Stream Support**: 2-4 camera feeds ko ek saath display kare
- **Real-time Processing**: Live video processing aur analysis
- **Frame Synchronization**: Sabhi cameras ke frames ko sync rahe
- **Quality Control**: Adjustable resolution aur bitrate
- **Recording**: Multi-stream recording aur playback
- **🏷️ Dynamic Nameplates**: Real-time name and designation overlay
- **Customizable Styles**: Font, color, position, aur transparency settings
- **Multi-Language Support**: Hindi aur English dono mein nameplates

### Setup Multi-Camera System

#### Step 1: Camera Configuration with Nameplate Settings
```bash
# config/camera_config.json banayein
{
  "cameras": [
    {
      "id": 0,
      "name": "Main Camera",
      "source": 0,
      "resolution": "1920x1080",
      "fps": 30,
      "nameplate": {
        "enabled": true,
        "name": "Rajesh Kumar",
        "designation": "Senior News Anchor",
        "position": "bottom-center",
        "style": "professional"
      }
    },
    {
      "id": 1,
      "name": "Side Camera",
      "source": 1,
      "resolution": "1280x720",
      "fps": 30,
      "nameplate": {
        "enabled": true,
        "name": "Priya Singh",
        "designation": "Field Correspondent",
        "position": "bottom-left",
        "style": "modern"
      }
    },
    {
      "id": 2,
      "name": "Wide Angle",
      "source": 2,
      "resolution": "1280x720",
      "fps": 30,
      "nameplate": {
        "enabled": true,
        "name": "Amit Verma",
        "designation": "Fact-Checker & Analyst",
        "position": "bottom-right",
        "style": "professional"
      }
    },
    {
      "id": 3,
      "name": "Desk Camera",
      "source": 3,
      "resolution": "1920x1080",
      "fps": 30,
      "nameplate": {
        "enabled": true,
        "name": "Neha Patel",
        "designation": "Production Manager",
        "position": "top-right",
        "style": "elegant"
      }
    }
  ],
  "nameplate_settings": {
    "global": {
      "font_family": "Arial",
      "font_size_name": 24,
      "font_size_designation": 16,
      "text_color": "#FFFFFF",
      "background_color": "#000000",
      "background_opacity": 0.8,
      "border_color": "#FFC107",
      "border_width": 2,
      "padding": 10,
      "animation": "fade",
      "update_interval": 1000
    },
    "styles": {
      "professional": {
        "font_family": "Courier New",
        "text_color": "#FFFFFF",
        "background_color": "#1A1A1A",
        "border_color": "#FFD700",
        "font_weight": "bold"
      },
      "modern": {
        "font_family": "Segoe UI",
        "text_color": "#E0E0E0",
        "background_color": "#2D2D2D",
        "border_color": "#FF6B6B",
        "background_opacity": 0.85
      },
      "elegant": {
        "font_family": "Georgia",
        "text_color": "#F5F5F5",
        "background_color": "#0D0D0D",
        "border_color": "#FFB700",
        "font_style": "italic"
      },
      "minimal": {
        "font_family": "Helvetica",
        "text_color": "#FFFFFF",
        "background_color": "transparent",
        "border_color": "#FFFFFF",
        "border_width": 1
      }
    }
  }
}
```

#### Step 2: Initialize Multi-Camera Capture with Nameplate Support
```bash
python manage.py init_camera_system --config config/camera_config.json
```

#### Step 3: Nameplate Configuration & Management
```bash
# Update nameplate information dynamically
python manage.py update_nameplate \
  --camera_id=0 \
  --name="Rajesh Kumar" \
  --designation="Senior News Anchor"

# Update multiple cameras at once
python manage.py batch_update_nameplates --config config/nameplate_batch.json

# Enable/Disable nameplate overlay
python manage.py toggle_nameplate --camera_id=0 --enable=true

# Change nameplate style
python manage.py set_nameplate_style --camera_id=1 --style=modern
```

#### Step 4: Start Live Stream with Nameplates
```bash
# Terminal se multi-camera stream start kare
python manage.py start_multicam_stream --config config/camera_config.json --enable_nameplates=true

# Ya admin panel se:
# Dashboard > Live Streams > Start Multi-Camera Capture > Enable Nameplates
```

#### Step 5: Monitoring with Nameplate Details
```bash
# Real-time monitoring dashboard
http://localhost:8000/camera/dashboard

# Individual camera feeds with nameplates
http://localhost:8000/camera/feed/0  # Main Camera - Rajesh Kumar
http://localhost:8000/camera/feed/1  # Side Camera - Priya Singh
http://localhost:8000/camera/feed/2  # Wide Angle - Amit Verma
http://localhost:8000/camera/feed/3  # Desk Camera - Neha Patel

# Nameplate management panel
http://localhost:8000/camera/nameplates
```

### Usage Examples

#### Python API Se Multi-Camera Control with Nameplates
```python
from camera.multi_capture import MultiCameraCapture
from camera.nameplate import NameplateManager

# Initialize multi-camera system
capture = MultiCameraCapture(config_path='config/camera_config.json')
nameplate_mgr = NameplateManager(config_path='config/camera_config.json')

# Start capturing with nameplate overlays
capture.start_all_cameras()
nameplate_mgr.enable_all_nameplates()

# Get frames from all cameras with nameplates
while True:
    frames = capture.get_frames()
    frames_with_nameplates = nameplate_mgr.apply_nameplates(frames)
    # Process frames with overlaid nameplates...
    
    # Update nameplate dynamically
    nameplate_mgr.update_nameplate(
        camera_id=0,
        name="Updated Name",
        designation="New Designation"
    )
    
# Stop capturing
capture.stop_all_cameras()
nameplate_mgr.disable_all_nameplates()
```

#### Nameplate Class Implementation
```python
# camera/nameplate.py

import cv2
from typing import Dict, Tuple
from PIL import Image, ImageDraw, ImageFont

class NameplateManager:
    """Manage nameplate overlays for multi-camera streams"""
    
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)
        self.nameplates = {}
        self.initialize_nameplates()
    
    def apply_nameplate(self, frame, camera_id: int, nameplate_data: Dict):
        """Apply nameplate overlay to a single frame"""
        
        name = nameplate_data.get('name', 'Unknown')
        designation = nameplate_data.get('designation', 'Staff')
        position = nameplate_data.get('position', 'bottom-center')
        style = nameplate_data.get('style', 'professional')
        
        # Get style configuration
        style_config = self.config['nameplate_settings']['styles'][style]
        
        # Create nameplate text
        nameplate_text = f"{name}\n{designation}"
        
        # Calculate position
        height, width = frame.shape[:2]
        x, y = self._calculate_position(position, width, height)
        
        # Apply nameplate using OpenCV
        frame = self._draw_nameplate(
            frame, 
            nameplate_text, 
            x, y, 
            style_config
        )
        
        return frame
    
    def _draw_nameplate(self, frame, text: str, x: int, y: int, style: Dict):
        """Draw nameplate on frame with specified style"""
        
        font_face = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = style.get('font_size', 1.0)
        font_color = self._hex_to_bgr(style.get('text_color', '#FFFFFF'))
        background_color = self._hex_to_bgr(style.get('background_color', '#000000'))
        
        # Draw background rectangle
        text_size = cv2.getTextSize(text, font_face, font_scale, 2)[0]
        padding = style.get('padding', 10)
        
        cv2.rectangle(
            frame,
            (x - padding, y - padding),
            (x + text_size[0] + padding, y + text_size[1] + padding),
            background_color,
            -1
        )
        
        # Draw border
        border_color = self._hex_to_bgr(style.get('border_color', '#FFD700'))
        border_width = style.get('border_width', 2)
        
        cv2.rectangle(
            frame,
            (x - padding, y - padding),
            (x + text_size[0] + padding, y + text_size[1] + padding),
            border_color,
            border_width
        )
        
        # Draw text
        cv2.putText(
            frame,
            text,
            (x, y + text_size[1]),
            font_face,
            font_scale,
            font_color,
            2
        )
        
        return frame
    
    def update_nameplate(self, camera_id: int, name: str, designation: str):
        """Update nameplate information for a camera"""
        if camera_id in self.nameplates:
            self.nameplates[camera_id]['name'] = name
            self.nameplates[camera_id]['designation'] = designation
    
    def apply_nameplates(self, frames: Dict) -> Dict:
        """Apply nameplates to all frames"""
        frames_with_nameplates = {}
        
        for camera_id, frame in frames.items():
            if camera_id in self.nameplates and self.nameplates[camera_id]['enabled']:
                frames_with_nameplates[camera_id] = self.apply_nameplate(
                    frame,
                    camera_id,
                    self.nameplates[camera_id]
                )
            else:
                frames_with_nameplates[camera_id] = frame
        
        return frames_with_nameplates
```

#### Web Interface Se Control
1. Dashboard mein jaaye: `http://localhost:8000/camera/dashboard`
2. "Start Multi-Camera" button click kare
3. Live preview dekhen with nameplates
4. "Manage Nameplates" section mein jaaye
5. Har camera ke liye name aur designation update kare
6. Style, position, aur colors customize kare
7. Recording start/stop kare

### Nameplate Customization Options

#### Available Positions
- `top-left` - Upper left corner
- `top-center` - Top middle
- `top-right` - Upper right corner
- `bottom-left` - Lower left corner
- `bottom-center` - Bottom middle (Default)
- `bottom-right` - Lower right corner
- `center-left` - Left side middle
- `center-right` - Right side middle
- `center` - Exact center

#### Available Styles
- `professional` - Corporate look with bold fonts
- `modern` - Contemporary design
- `elegant` - Sophisticated appearance
- `minimal` - Clean, simple design
- `neon` - Bright, colorful overlay
- `classic` - Traditional news style

#### Customization Example
```python
# Create custom nameplate style
custom_style = {
    "font_family": "Arial",
    "font_size_name": 28,
    "font_size_designation": 18,
    "text_color": "#00FF00",
    "background_color": "#001a00",
    "border_color": "#00FF00",
    "border_width": 3,
    "padding": 15,
    "background_opacity": 0.9,
    "shadow": True,
    "animation": "slide"
}

# Apply to camera
nameplate_mgr.set_custom_style(camera_id=0, style=custom_style)
```

### Advanced Features

#### Frame Synchronization
```bash
# Ensure all cameras capture frames at same time
python manage.py sync_camera_frames --method=hardware_trigger --apply_nameplates=true
```

#### Video Processing with Nameplates
```bash
# Real-time analysis aur nameplates add kare
python manage.py process_multicam_video \
  --effect=timestamp \
  --effect=watermark \
  --effect=nameplate \
  --nameplate_style=professional
```

#### Storage & Recording
```bash
# Multi-camera recording configure kare with nameplate data
python manage.py configure_recording \
  --output_path=/media/recordings \
  --format=mp4 \
  --quality=high \
  --embed_nameplates=true \
  --auto_cleanup=true
```

#### Nameplate Analytics & Logging
```bash
# Track all nameplate changes
python manage.py log_nameplate_changes --export=csv

# Generate nameplate usage report
python manage.py report_nameplate_usage --date_range=last_week
```

#### Playback with Nameplate Information
- Recorded multi-camera sessions dekhen with nameplate data
- Frame-by-frame comparison kare with person identification
- Export individual camera feeds with embedded nameplates
- Generate nameplate history reports

---

## 📚 Documentation
- [API Documentation](./docs/API.md)
- [Contributing Guide](./CONTRIBUTING.md)
- [FAQ](./docs/FAQ.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Multi-Camera Guide](./docs/MULTI_CAMERA.md)
- [Nameplate Guide](./docs/NAMEPLATE_GUIDE.md)

---

## 🤝 Contributing
Hume help karna chahte ho? Badhiya! Ye steps follow kare:

1. Fork the repository
2. Feature branch create kare (`git checkout -b feature/AmazingFeature`)
3. Changes commit kare (`git commit -m 'Add some AmazingFeature'`)
4. Branch push kare (`git push origin feature/AmazingFeature`)
5. Pull Request open kare

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Contact
- 📧 Email: support@newsexplorerhindi.com
- 🐦 Twitter: [@NewsExplorerHindi](https://twitter.com)
- 💬 Discord: [Join Community](https://discord.com)
- 📱 Instagram: [@newsexplorerhindi](https://instagram.com)

---

## 🙏 Acknowledgments
- Sabhi contributors ka shukriya
- Open source community ka support
- Users ka valuable feedback

---

<marquee direction="left" behavior="scroll" scrollamount="4" style="background: linear-gradient(90deg, #764ba2 0%, #667eea 100%); padding: 15px; color: white; font-weight: bold; font-size: 14px; margin: 0;">
  ✨ Made with ❤️ by NewsExplorerHindi Team | Spreading Truth Through Technology | Fact-Checking for Everyone | Stay Informed, Stay Updated ✨
</marquee>
