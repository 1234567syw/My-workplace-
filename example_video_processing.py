#!/usr/bin/env python3
"""
Example: Multi-Camera Video Processing with Nameplates
Demonstrates how to load videos and add nameplate overlays
"""

import cv2
import json
import os
from pathlib import Path

class VideoProcessor:
    """Process videos with nameplate overlays"""
    
    def __init__(self, config_path='config/video_config.json'):
        self.config = self.load_config(config_path)
        self.nameplate_settings = self.config.get('nameplate_settings', {}) if self.config else {}
    
    def load_config(self, config_path):
        """Load video configuration"""
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        print(f"⚠️  Config not found: {config_path}")
        return None
    
    def hex_to_bgr(self, hex_color):
        """Convert hex color to BGR format for OpenCV"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))
    
    def draw_nameplate(self, frame, name, designation, position='bottom-center', style='professional'):
        """Draw nameplate on frame"""
        
        if not self.nameplate_settings:
            return frame
        
        # Get style configuration
        styles = self.nameplate_settings.get('styles', {})
        style_config = styles.get(style, {})
        
        # Get global settings
        global_settings = self.nameplate_settings.get('global', {})
        
        # Merge settings
        font_size_name = style_config.get('font_size', global_settings.get('font_size_name', 24))
        font_size_designation = global_settings.get('font_size_designation', 16)
        text_color = self.hex_to_bgr(style_config.get('text_color', '#FFFFFF'))
        background_color = self.hex_to_bgr(style_config.get('background_color', '#000000'))
        border_color = self.hex_to_bgr(style_config.get('border_color', '#FFD700'))
        border_width = style_config.get('border_width', 2)
        padding = global_settings.get('padding', 10)
        
        height, width = frame.shape[:2]
        font_face = cv2.FONT_HERSHEY_SIMPLEX
        
        # Create nameplate text
        nameplate_lines = [name, designation]
        
        # Calculate position
        x, y = self._calculate_position(position, width, height, font_size_name)
        
        # Draw background rectangle
        text_size = cv2.getTextSize(name, font_face, font_size_name / 10, 2)[0]
        
        rect_x1 = x - padding
        rect_y1 = y - padding - text_size[1] - 20
        rect_x2 = x + text_size[0] + padding
        rect_y2 = y + padding + text_size[1]
        
        # Draw semi-transparent background
        cv2.rectangle(frame, (rect_x1, rect_y1), (rect_x2, rect_y2), background_color, -1)
        
        # Draw border
        cv2.rectangle(frame, (rect_x1, rect_y1), (rect_x2, rect_y2), border_color, border_width)
        
        # Draw text
        cv2.putText(frame, name, (x, y), font_face, font_size_name / 10, text_color, 2)
        cv2.putText(frame, designation, (x, y + 25), font_face, font_size_designation / 10, text_color, 1)
        
        return frame
    
    def _calculate_position(self, position, width, height, font_size):
        """Calculate nameplate position"""
        
        padding = 20
        
        positions = {
            'top-left': (padding, padding + 30),
            'top-center': (width // 2 - 100, padding + 30),
            'top-right': (width - 200, padding + 30),
            'bottom-left': (padding, height - padding),
            'bottom-center': (width // 2 - 100, height - padding),
            'bottom-right': (width - 200, height - padding),
            'center-left': (padding, height // 2),
            'center-right': (width - 200, height // 2),
            'center': (width // 2 - 100, height // 2)
        }
        
        return positions.get(position, positions['bottom-center'])
    
    def process_single_video(self, video_path, output_path=None, nameplate_data=None):
        """
        Process a single video with nameplate overlay
        
        Args:
            video_path: Path to input video
            output_path: Path to save processed video (optional)
            nameplate_data: Dict with 'name', 'designation', 'position', 'style'
        """
        
        if not os.path.exists(video_path):
            print(f"❌ Video not found: {video_path}")
            return False
        
        print(f"\n🎬 Processing: {video_path}")
        
        # Open video
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"❌ Cannot open video: {video_path}")
            return False
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"   📊 Resolution: {width}x{height}")
        print(f"   ⏱️  FPS: {fps}")
        print(f"   📹 Total Frames: {total_frames}")
        
        # Setup video writer if output path provided
        out = None
        if output_path:
            os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            print(f"   💾 Output: {output_path}")
        
        # Default nameplate
        if not nameplate_data:
            nameplate_data = {
                'name': 'NewsExplorer',
                'designation': 'Test Video',
                'position': 'bottom-center',
                'style': 'professional'
            }
        
        frame_count = 0
        
        # Process frames
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Add nameplate
            frame = self.draw_nameplate(
                frame,
                nameplate_data.get('name', 'Unknown'),
                nameplate_data.get('designation', 'Staff'),
                nameplate_data.get('position', 'bottom-center'),
                nameplate_data.get('style', 'professional')
            )
            
            # Write to output
            if out:
                out.write(frame)
            
            frame_count += 1
            
            # Progress update every 30 frames
            if frame_count % 30 == 0:
                percent = (frame_count / total_frames) * 100
                print(f"   ⏳ Progress: {frame_count}/{total_frames} ({percent:.1f}%)")
        
        cap.release()
        if out:
            out.release()
        
        print(f"✅ Processing complete: {frame_count} frames")
        return True
    
    def process_multi_camera(self, camera_list, display=False):
        """
        Process multiple camera feeds simultaneously
        
        Args:
            camera_list: List of dicts with 'path', 'name', 'designation'
            display: Whether to display frames
        """
        
        print(f"\n📷 Multi-Camera Processing: {len(camera_list)} cameras")
        
        # Open all cameras
        captures = {}
        for camera in camera_list:
            path = camera.get('path')
            if os.path.exists(path):
                cap = cv2.VideoCapture(path)
                if cap.isOpened():
                    captures[path] = {
                        'capture': cap,
                        'name': camera.get('name', 'Camera'),
                        'designation': camera.get('designation', 'Feed'),
                        'frame_count': 0
                    }
                    print(f"   ✅ Loaded: {camera.get('name')}")
                else:
                    print(f"   ❌ Cannot open: {path}")
            else:
                print(f"   ❌ Not found: {path}")
        
        if not captures:
            print("❌ No cameras loaded")
            return False
        
        print(f"   📊 Processing {len(captures)} cameras...")
        
        # Process frames
        frame_index = 0
        while True:
            all_frames = {}
            any_opened = False
            
            for path, data in captures.items():
                ret, frame = data['capture'].read()
                
                if ret:
                    any_opened = True
                    
                    # Add nameplate
                    frame = self.draw_nameplate(
                        frame,
                        data['name'],
                        data['designation'],
                        'bottom-center',
                        'professional'
                    )
                    
                    all_frames[path] = frame
                    data['frame_count'] += 1
            
            if not any_opened:
                break
            
            # Optional: Display frames
            if display and all_frames:
                # Create a grid of frames (optional)
                # For now just print progress
                pass
            
            frame_index += 1
            
            if frame_index % 30 == 0:
                avg_frames = sum(d['frame_count'] for d in captures.values()) / len(captures)
                print(f"   ⏳ Frame: {frame_index} (avg per camera: {avg_frames:.0f})")
        
        # Release all cameras
        for data in captures.values():
            data['capture'].release()
        
        print(f"✅ Multi-camera processing complete")
        return True

def main():
    """Main example"""
    
    print("="*60)
    print("🎬 Multi-Camera Video Processing Example")
    print("="*60)
    
    processor = VideoProcessor()
    
    # Example 1: Process single video with nameplate
    print("\n📝 Example 1: Single Video with Nameplate")
    print("-" * 60)
    
    video_path = 'test_videos/sample_test.mp4'
    if os.path.exists(video_path):
        processor.process_single_video(
            video_path,
            output_path='recordings/processed_video.mp4',
            nameplate_data={
                'name': 'Rajesh Kumar',
                'designation': 'Senior News Anchor',
                'position': 'bottom-center',
                'style': 'professional'
            }
        )
    else:
        print(f"ℹ️  Sample video not found: {video_path}")
        print("   Run: python test_video_tool.py")
    
    # Example 2: Multi-camera processing
    print("\n📝 Example 2: Multi-Camera Processing")
    print("-" * 60)
    
    # Check if camera feeds exist
    cameras = [
        {
            'path': 'camera_feeds/camera_1.mp4',
            'name': 'Main Camera',
            'designation': 'Primary Feed'
        },
        {
            'path': 'camera_feeds/camera_2.mp4',
            'name': 'Side Camera',
            'designation': 'Secondary Feed'
        }
    ]
    
    existing_cameras = [c for c in cameras if os.path.exists(c['path'])]
    
    if existing_cameras:
        processor.process_multi_camera(existing_cameras)
    else:
        print("ℹ️  Camera feeds not found in camera_feeds/")
        print("   Add your video files to camera_feeds/ directory")
    
    print("\n" + "="*60)
    print("✨ Examples Complete!")
    print("="*60)
    print("\n💡 Next Steps:")
    print("   1. Add your video files to test_videos/ or camera_feeds/")
    print("   2. Run: python test_video_tool.py")
    print("   3. Customize nameplate settings in config/video_config.json")
    print("   4. Run: python example_video_processing.py")

if __name__ == '__main__':
    main()
