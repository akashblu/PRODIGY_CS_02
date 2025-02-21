# PRODIGY_CS_02


Image Encryption & Decryption using Pixel Manipulation:

This Python script allows you to encrypt and decrypt images using bitwise XOR operation. It provides a simple GUI for selecting images and entering an encryption key.

Features:
Symmetric Encryption: The same key is used for encryption and decryption.

Lightweight: Uses OpenCV and Tkinter.

User-friendly GUI: Select images and enter keys easily.
How It Works:

* The script prompts you to select an image.

* You enter a numeric key (0-255).

* The script applies a bitwise XOR operation on the image pixels.

* The encrypted image is saved as {original_name}_encrypted.png.

* To decrypt, run the script again, select the encrypted image, and enter the same key.

