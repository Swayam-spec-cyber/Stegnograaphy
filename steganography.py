import cv2
import os
import numpy as np

# Load Image (Change filename here)
img = cv2.imread("000000013597.jpg")  # Make sure this file exists in the directory
if img is None:
    print("Error: Image not found!")
    exit()

height, width, _ = img.shape  # Get image dimensions

# Convert message to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Convert binary to text
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)

# Message Input
msg = input("Enter secret message: ") + "###"  # '###' acts as a stopping indicator
password = input("Enter a passcode: ")

binary_msg = text_to_binary(msg)

if len(binary_msg) > height * width * 3:
    print("Error: Message is too large for this image!")
    exit()

# Encoding the Message in the Image
binary_index = 0
for row in range(height):
    for col in range(width):
        for channel in range(3):  # Iterate over RGB
            if binary_index < len(binary_msg):
                img[row, col, channel] = (img[row, col, channel] & 254) | int(binary_msg[binary_index])
                binary_index += 1

# ✅ Save as PNG (No Compression)
cv2.imwrite("encryptedImage.png", img)
print("Message successfully encoded in 'encryptedImage.png'!")

# Decryption Process
img = cv2.imread("encryptedImage.png")
pas = input("Enter passcode for decryption: ")

if password == pas:
    binary_msg = ""
    for row in range(height):
        for col in range(width):
            for channel in range(3):
                binary_msg += str(img[row, col, channel] & 1)

    # Print binary output for debugging
    print("\nExtracted Binary Message:", binary_msg[:100], "...")  # Print first 100 bits

    extracted_msg = binary_to_text(binary_msg)
    
    if "###" in extracted_msg:
        extracted_msg = extracted_msg[:extracted_msg.index("###")]
        print("Decrypted Message:", extracted_msg)
    else:
        print("Error: No valid message found!")
else:
    print("YOU ARE NOT AUTHORIZED!")
