# TextExtraction
Lấy text từ hình ảnh
## Cài đặt

Để cài đặt EasyOCR trên môi trường anaconda python, hãy làm theo các bước sau: 

### Cài đặt Anaconda Python

1. Tải phiên bản anaconda mới nhất từ [trang web anaconda](https://www.anaconda.com/download).
2. Làm theo hướng dẫn cài đặt theo hệ điều hành của bạn (Windows, macOS, Linux).
3. Anaconda có bao gồm một phiên bản Python tích hợp
*Sau khi cài đặt, kiểm tra bằng cách chạy:
```bash
conda --version
python --version
```
4. [Hướng dẫn sử dụng](https://tuananalytic.com/tu-hoc-python-10-phut-gioi-thieu-nhanh-pandas-va-anaconda/)


### Cài đặt EasyOCR

Cài đặt **PyTorch** để thực hiện các tính toán học sâu:
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
reader = easyocr.Reader(['en', 'vi'])  # Hỗ trợ Tiếng Anh và Tiếng Việt
result = reader.readtext('sample_image.jpg')
print(result)
```
Hãy thay thế `'sample_image.jpg'` bằng một tệp ảnh hợp lệ.

## Cách Sử Dụng
- Đặt các hình ảnh chứa văn bản vào thư mục của dự án.
- Chạy OCR trên một hình ảnh bằng đoạn mã trên.
- Chỉnh sửa mã để trích xuất và xử lý văn bản theo nhu cầu.
