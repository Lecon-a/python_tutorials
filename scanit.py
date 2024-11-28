import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

def capture_image():
    """Capture an image from the webcam and process it."""
    try:
        # Open webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Cannot access the webcam.")
            return

        # Read the first frame
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture an image.")
            cap.release()
            return

        # Release the camera after capturing
        cap.release()

        # Convert the frame to PIL Image
        cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(cv2_image)

        # Display the captured image in the GUI
        img_display = ImageTk.PhotoImage(image.resize((250, 250)))
        qr_code_label.config(image=img_display)
        qr_code_label.image = img_display

        # Decode the QR code
        decoded_data = decode(image)
        if decoded_data:
            result = "\n".join([obj.data.decode("utf-8") for obj in decoded_data])
            result_label.config(text=f"Decoded Data:\n{result}")
        else:
            result_label.config(text="No QR code detected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("QR Code Scanner")
root.geometry("400x500")
root.resizable(False, False)

# Widgets for GUI
snap_button = tk.Button(root, text="Snap QR Code", command=capture_image, font=("Arial", 14))
snap_button.pack(pady=10)

qr_code_label = tk.Label(root, text="Captured QR Code Image", bg="lightgrey", width=40, height=10)
qr_code_label.pack(pady=10)

result_label = tk.Label(root, text="Decoded Data will appear here.", wraplength=350, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
