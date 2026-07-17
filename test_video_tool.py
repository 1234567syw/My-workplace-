#!/usr/bin/env python3
"""
Video Testing Script for NewsExplorerHindi
Test and validate video files for the project
"""

import cv2
import os
import json
import sys
from pathlib import Path

class VideoTester:
    """Test and validate video files"""
    
    def __init__(self):
        self.results = []
        self.config = self.load_config()
    
    def load_config(self):
        """Load video configuration"""
        config_path = 'config/video_config.json'
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        return None
    
    def test_video_file(self, video_path):
        """Test a single video file"""
        
        result = {
            'path': video_path,
            'exists': False,
            'valid': False,
            'details': {}
        }
        
        # Check if file exists
        if not os.path.exists(video_path):
            print(f"❌ FILE NOT FOUND: {video_path}")
            self.results.append(result)
            return False
        
        result['exists'] = True
        file_size = os.path.getsize(video_path) / (1024 * 1024)  # Convert to MB
        
        try:
            # Try to open with OpenCV
            cap = cv2.VideoCapture(video_path)
            
            if not cap.isOpened():
                print(f"❌ CANNOT OPEN: {video_path}")
                self.results.append(result)
                return False
            
            # Get video properties
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            duration = frame_count / fps if fps > 0 else 0
            
            # Read first frame to validate
            ret, frame = cap.read()
            cap.release()
            
            if not ret:
                print(f"⚠️  CANNOT READ FRAMES: {video_path}")
                self.results.append(result)
                return False
            
            result['valid'] = True
            result['details'] = {
                'file_size_mb': round(file_size, 2),
                'resolution': f"{width}x{height}",
                'fps': fps,
                'total_frames': frame_count,
                'duration_seconds': round(duration, 2),
                'bitrate_approx': 'unknown'
            }
            
            print(f"✅ VALID: {video_path}")
            print(f"   📊 Resolution: {width}x{height}")
            print(f"   ⏱️  FPS: {fps}")
            print(f"   📹 Frames: {frame_count}")
            print(f"   ⏳ Duration: {duration:.2f} seconds")
            print(f"   💾 File Size: {file_size:.2f} MB")
            print()
            
            return True
            
        except Exception as e:
            print(f"❌ ERROR: {video_path} - {str(e)}")
            self.results.append(result)
            return False
    
    def test_all_videos(self):
        """Test all videos in the config"""
        
        if not self.config:
            print("⚠️  No config/video_config.json found")
            print("Testing common video directories...\n")
            
            # Test default directories
            test_dirs = ['test_videos', 'camera_feeds', 'recordings']
            for dir_name in test_dirs:
                if os.path.isdir(dir_name):
                    print(f"\n📁 Testing {dir_name}/ directory:")
                    for file in os.listdir(dir_name):
                        if file.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                            self.test_video_file(os.path.join(dir_name, file))
            return
        
        # Test videos from config
        print("🎬 Testing Videos from Config\n")
        
        if 'test_videos' in self.config:
            print("📝 Test Videos:")
            for video in self.config['test_videos']:
                self.test_video_file(video['path'])
        
        if 'camera_feeds' in self.config:
            print("\n📷 Camera Feeds:")
            for camera in self.config['camera_feeds']:
                self.test_video_file(camera['path'])
    
    def generate_test_video(self, output_path='test_videos/sample_test.mp4', 
                           duration=10, resolution=(1280, 720), fps=30):
        """Generate a simple test video"""
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        print(f"🎬 Generating test video: {output_path}")
        print(f"   Duration: {duration}s, Resolution: {resolution}, FPS: {fps}")
        
        try:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, float(fps), resolution)
            
            total_frames = duration * fps
            
            for frame_idx in range(int(total_frames)):
                # Create a test frame
                frame = cv2.cvtColor(
                    cv2.imread(cv2.samples.findFile('')) 
                    if cv2.samples.findFile('') else None,
                    cv2.COLOR_BGR2RGB
                ) if cv2.samples.findFile('') else None
                
                if frame is None:
                    frame = (128 + (frame_idx % 128)) * \
                            (cv2.UMat(resolution[::-1] + (3,), cv2.CV_8U) / 256).get()
                
                # Create frame manually
                frame = ((frame_idx // fps) % 2) * 255 * \
                        cv2.UMat((resolution[1], resolution[0], 3), cv2.CV_8U).get()
                
                # Simpler approach
                frame = cv2.cvtColor(
                    cv2.createTrackbar('', '', 0, 0) or 
                    cv2.imread('logo newpaper.png', 0) or
                    cv2.UMat((resolution[1], resolution[0]), cv2.CV_8U).get(),
                    cv2.COLOR_GRAY2BGR
                ) if os.path.exists('logo newpaper.png') else \
                    cv2.UMat((resolution[1], resolution[0], 3), cv2.CV_8U).get()
                
                # Proper frame generation
                frame = (128 + 64 * ((frame_idx // 30) % 2)) * \
                        (cv2.Mat((resolution[1], resolution[0], 3), cv2.CV_8U) / 256).get() \
                        if hasattr(cv2, 'Mat') else \
                        cv2.cvtColor(
                            cv2.imread('logo newpaper.png') or 
                            cv2.imread('logo newpaper.png'),
                            cv2.COLOR_BGR2RGB
                        ).reshape(resolution[1], resolution[0], 3)
                
                # Simple frame creation
                import numpy as np
                frame = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
                frame[:, :] = [100 + (frame_idx % 155), 
                               100 + ((frame_idx * 2) % 155), 
                               100 + ((frame_idx * 3) % 155)]
                
                # Add text
                cv2.putText(frame, f'Frame {frame_idx}/{int(total_frames)}', 
                           (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                cv2.putText(frame, 'NewsExplorerHindi Test Video', 
                           (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                
                out.write(frame)
                
                # Progress
                if (frame_idx + 1) % (fps * 5) == 0:
                    print(f"   ⏳ Generated {frame_idx + 1}/{int(total_frames)} frames")
            
            out.release()
            print(f"✅ Test video created: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error generating video: {str(e)}")
            return False
    
    def create_sample_config(self):
        """Create a sample video_config.json"""
        
        os.makedirs('config', exist_ok=True)
        config_path = 'config/video_config.json'
        
        if os.path.exists(config_path):
            print(f"ℹ️  Config already exists: {config_path}")
            return
        
        sample_config = {
            "test_videos": [
                {
                    "id": 1,
                    "name": "sample_test",
                    "path": "test_videos/sample_test.mp4",
                    "description": "Auto-generated test video",
                    "duration": "10 seconds",
                    "resolution": "1280x720",
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
        
        with open(config_path, 'w') as f:
            json.dump(sample_config, f, indent=2)
        
        print(f"✅ Sample config created: {config_path}")
    
    def create_directories(self):
        """Create necessary directories"""
        
        dirs = ['test_videos', 'camera_feeds', 'recordings', 'config']
        for dir_name in dirs:
            os.makedirs(dir_name, exist_ok=True)
            # Create README in each directory
            readme_path = os.path.join(dir_name, 'README.txt')
            if not os.path.exists(readme_path):
                with open(readme_path, 'w') as f:
                    f.write(f"{dir_name.upper()} Directory\n")
                    f.write("Add your video files here\n")
        
        print("✅ Directory structure created")
    
    def print_summary(self):
        """Print test summary"""
        
        if not self.results:
            return
        
        print("\n" + "="*60)
        print("📊 TEST SUMMARY")
        print("="*60)
        
        valid_count = sum(1 for r in self.results if r['valid'])
        total_count = len(self.results)
        
        print(f"✅ Valid Videos: {valid_count}/{total_count}")
        
        for result in self.results:
            status = "✅" if result['valid'] else "❌"
            print(f"{status} {result['path']}")
            if result['details']:
                for key, value in result['details'].items():
                    print(f"   - {key}: {value}")

def main():
    """Main function"""
    
    print("🎬 NewsExplorerHindi - Video Testing Tool\n")
    print("="*60)
    
    tester = VideoTester()
    
    # Create directories
    tester.create_directories()
    print()
    
    # Create sample config
    tester.create_sample_config()
    print()
    
    # Generate test video if no videos exist
    test_video_path = 'test_videos/sample_test.mp4'
    if not os.path.exists(test_video_path):
        print("No test videos found. Generating one...\n")
        tester.generate_test_video()
        print()
    
    # Test all videos
    tester.test_all_videos()
    
    # Print summary
    tester.print_summary()
    
    print("\n" + "="*60)
    print("✨ Testing Complete!")
    print("="*60)

if __name__ == '__main__':
    main()
