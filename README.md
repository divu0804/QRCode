# QR Code Generator

This Streamlit application allows users to generate QR codes from URLs or text inputs. Users can customize the QR code's fill and background colors before generating and downloading the QR code image.

## Features

- Input field to enter URL or text for generating QR codes.
- Color pickers for customizing the QR code's fill and background colors.
- Download button to save the generated QR code image.

## Usage

1. **Input Field:**
   - Enter the URL or text for which you want to generate the QR code.

2. **Color Pickers:**
   - Use the color pickers to select the fill and background colors for the QR code.

3. **Generate QR Code:**
   - Once input and colors are selected, click on the "Download image" button to generate and download the QR code image.

## Installation

To run this application locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/qr-code-generator.git
    ```

2. Navigate to the directory:

    ```bash
    cd qr-code-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Requirements

- Python 3.6+
- Streamlit
- qrcode
- Pillow (PIL)

## About

This application was created using Streamlit, a popular framework for building interactive web applications with Python. It leverages the `qrcode` library to generate QR codes and the `PIL` library for image processing.

