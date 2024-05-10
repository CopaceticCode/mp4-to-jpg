import tkinter as tk
from tkinter import filedialog, messagebox
import os
import cv2

# Define color palette
BG_COLOR = "#2c2f33"
FG_COLOR = "#f0f0f0"
ACCENT_COLOR = "#0097e6"

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    # Initialize frame count
    frame_count = 0

    while cap.isOpened():
        # Read a frame from the video file
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame as JPEG file
        frame_filename = f"{output_folder}/frame_{frame_count:04d}.jpg"
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the VideoCapture object
    cap.release()

def select_video_file():
    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        video_entry.delete(0, tk.END)
        video_entry.insert(0, file_path)

def extract_frames_gui():
    video_path = video_entry.get()
    if not os.path.exists(video_path):
        messagebox.showerror("Error", "Video file not found!")
        return

    output_folder = os.path.join(os.path.dirname(__file__), "output_frames")
    os.makedirs(output_folder, exist_ok=True)

    extract_frames(video_path, output_folder)
    messagebox.showinfo("Success", "Frames extracted successfully!")

# Create the main window
root = tk.Tk()
root.title("Video Frame Extractor")
root.geometry("400x200")
root.configure(bg=BG_COLOR)
root.attributes("-topmost", True)  # Keep the window on top

# Create a label and entry for video file selection
video_label = tk.Label(root, text="Select a video file:", fg=FG_COLOR, bg=BG_COLOR)
video_label.pack(pady=10)
video_entry = tk.Entry(root, width=50, font=("Arial", 12), fg=FG_COLOR, bg=BG_COLOR)
video_entry.pack()
video_button = tk.Button(root, text="Browse", font=("Arial", 12), bg=ACCENT_COLOR, fg=FG_COLOR, command=select_video_file)
video_button.pack(pady=5)

# Create a button to start frame extraction
extract_button = tk.Button(root, text="Extract Frames", font=("Arial", 12), bg=ACCENT_COLOR, fg=FG_COLOR, command=extract_frames_gui)
extract_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
