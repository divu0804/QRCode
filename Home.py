import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(
    page_icon="🤳",
    page_title="QR Code Gen",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={'About': "## An application to generate QR Codes using Python"}
)

def main():
    st.title("QR Code Generator")
    data_in = st.text_input(label="Enter URL or text")
    col1, col2 = st.columns(2)
    with col1:
        fill_color = st.color_picker('Pick Fill Color', '#000000')
    with col2:
        back_color = st.color_picker('Pick Background Color', '#ffffff')

    qr = qrcode.QRCode(version=4, box_size=10, border=4)
    qr.add_data(data_in)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    img.save("./assets/qrcode.png")

    with open('./assets/qrcode.png', "rb") as file:
        image = Image.open(file)
        st.image(image, caption="Result")
        st.download_button(
            label="Download image",
            data=file,
            file_name="fantasticqrcode.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
