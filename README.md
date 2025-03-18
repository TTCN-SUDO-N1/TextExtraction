# TextExtraction
Lấy text từ hình ảnh
## Cài đặt

Để cài đặt EasyOCR trên môi trường anaconda python, hãy làm theo các bước sau: 

### Cài đặt Anaconda Python

1. Tải phiên bản anaconda mới nhất từ [trang web anaconda](https://www.anaconda.com/download).
2. Làm theo hướng dẫn cài đặt theo hệ điều hành của bạn (Windows, macOS, Linux).
3. Anaconda có bao gồm một phiên bản Python tích hợp
4. Tạo và kích hoạt môi trường ảo
```bash
conda create -n text_extraction_env python=3.12.7 -y
conda activate text_extraction_env
```

### Cài đặt EasyOCR

Cài đặt **PyTorch** trước EasyOCR:
```bash
pip install torch torchvision torchaudio
```

Cài đặt **EasyOCR**:
```bash
conda install anaconda::easyocr
```

Cài đặt OpenCV để xử lý hình ảnh:
```bash
pip install opencv-python
```

Chạy đoạn mã sau để kiểm tra xem EasyOCR có hoạt động chính xác hay không:
```python
import easyocr
reader = easyocr.Reader(['en', 'vi']) # Khai báo ngôn ngữ để trích xuất văn bản
result = reader.readtext('path/to/image.jpg')
print(result)
```
Hãy thay thế `'sample_image.jpg'` bằng một tệp ảnh hợp lệ.

## Cách Sử Dụng
- Đặt các hình ảnh chứa văn bản vào thư mục của dự án.
- Chạy OCR trên một hình ảnh bằng đoạn mã trên.
- Chỉnh sửa mã để trích xuất và xử lý văn bản theo nhu cầu.
