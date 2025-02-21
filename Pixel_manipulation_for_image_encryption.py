import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def encrypt_decrypt_image(image_path, key):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        messagebox.showerror("Error", "Invalid image file")
        return
    
    # Convert the key into an 8-bit integer
    key = np.uint8(key)

    # Apply XOR operation to each pixel
    
    encrypted_image = cv2.bitwise_xor(image, np.full_like(image, key, dtype=np.uint8))


    # Save the encrypted image
    save_path = image_path.split('.')[0] + "_encrypted.png"
    cv2.imwrite(save_path, encrypted_image)

    messagebox.showinfo("Success", f"Image saved at {save_path}")
    cv2.imshow("Processed Image", encrypted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def select_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        key = simpledialog.askinteger("Input", "Enter a numeric key (0-255):", minvalue=0, maxvalue=255)
        if key is not None:
            encrypt_decrypt_image(file_path, key)

# GUI
root = tk.Tk()
root.withdraw()  # Hide the main window
select_image()
