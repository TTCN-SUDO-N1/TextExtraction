import streamlit as st
from PIL import Image
import easyocr

# đổi ngôn ngữ
if "language" not in st.session_state:
    st.session_state.language = "EN"

language = st.session_state.language
if st.button("EN" if language == "VI" else "VI"):
    st.session_state.language = "VI" if language == "EN" else "EN"
    st.experimental_set_query_params()  # Refresh the page by setting query parameters

language = st.session_state.language
st.info(f"Switched to {'Vietnamese' if language == 'VI' else 'English'}")

st.title("Text Extraction" if language == "EN" else "Trích Xuất Văn Bản")

st.header("Hello, this is where you can extract text from image" if language == "EN" else "Xin chào, đây là nơi bạn có thể trích xuất văn bản từ hình ảnh")

# đăng ảnh
uploaded_file = st.file_uploader(
    "Choose an image to extract..." if language == "EN" else "Chọn một hình ảnh để trích xuất...",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    # mở chọn hình a ảnh
    image = Image.open(uploaded_file)

    # hiển thị hình ảnh
    st.image(image, caption='Uploaded Image.' if language == "EN" else 'Hình ảnh đã tải lên.', use_container_width=True)

    # trích xuất văn bản
    st.write("Extracting text from the image..." if language == "EN" else "Đang trích xuất văn bản từ hình ảnh...")
    try:
        reader = easyocr.Reader(['en', 'vi'])  # hỗ trợ anh, tiếng Việt
        text = reader.readtext(image, detail=0)
        # hiển thị văn bản đã trích xuất
        st.write("Extracted Text:" if language == "EN" else "Văn bản đã trích xuất:")
        st.write("\n".join(text))
    except Exception as e:
        st.error(f"An error occurred while extracting text: {e}" if language == "EN" else f"Đã xảy ra lỗi khi trích xuất văn bản: {e}")

st.sidebar.header("Guide to Using the Text Extract Function" if language == "EN" else "Hướng dẫn sử dụng chức năng trích xuất văn bản")
st.sidebar.write("""
1. Upload an image by clicking on the 'Browse files' button.
2. Supported image formats are jpg, png, and jpeg.
3. Once the image is uploaded, it will be displayed on the screen.
4. The text extracted from the image will be shown below the image.
""" if language == "EN" else """
1. Tải lên một hình ảnh bằng cách nhấn nút 'Browse files'.
2. Các định dạng hình ảnh được hỗ trợ: jpg, png, jpeg.
3. Sau khi tải lên, hình ảnh sẽ được hiển thị trên màn hình.
4. Văn bản trích xuất từ hình ảnh sẽ được hiển thị bên dưới hình ảnh.
""")

