# Stegnography
Hiding Text Under Image
📌 Project Overview
This project focuses on hiding secret messages within images using high-capacity steganography techniques. It modifies the Least Significant Bits (LSB) of pixel values to embed messages securely while maintaining image quality. The system ensures secure data transmission and privacy protection against unauthorized access.

📂 Features
✅ High-Capacity Embedding – Supports embedding larger messages without noticeable distortions.
✅ Password-Protected Encryption – Ensures only authorized users can decrypt hidden messages.
✅ Stealthy Data Hiding – Uses LSB-based steganography to avoid detection.
✅ Efficient Message Recovery – Accurately extracts and reconstructs hidden messages.
✅ Supports Various Image Formats – Works with JPG, PNG, BMP, etc.
✅ Cross-Platform Compatibility – Can be run on Windows, Linux, and Mac.

📌 Tech Stack
Programming Language: Python 🐍
Libraries Used:
OpenCV – Image processing
NumPy – Efficient array operations
OS – File handling
📜 Installation & Usage
🔹 Prerequisites
Ensure you have Python installed. You can install the required libraries using:

bash
Copy
Edit
pip install opencv-python numpy
🔹 How to Run
Place your secret image in the project folder.
Run the script:
bash
Copy
Edit
python steganography.py
Enter your secret message and passcode.
The encoded image will be saved as encryptedImage.jpg.
To decrypt, enter the correct passcode when prompted.
🎯 Unique Features
Higher Message Capacity compared to traditional LSB methods.
Password Protection prevents unauthorized access.
Supports Different Image Sizes for flexible use cases.
Maintains Image Quality while embedding messages securely.
🛠️ Applications
✔ Secure Communication – Hide sensitive data in images.
✔ Forensics & Intelligence – Securely transmit classified information.
✔ Watermarking & Copyright Protection – Embed digital signatures in images.
✔ Cybersecurity & Data Privacy – Prevent unauthorized data access.

🔮 Future Scope
🚀 AI-Based Steganalysis Resistance – Improve security against detection.
🚀 Mobile & Web-Based Implementation – Create a user-friendly tool for broader adoption.
🚀 Multi-Format Support – Extend to video, audio, and document steganography.
🚀 Cloud-Based API – Enable seamless integration with other security applications.
