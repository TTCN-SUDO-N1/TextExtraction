# TextExtraction

Lấy text từ hình ảnh

## Cài đặt

Để cài đặt EasyOCR trên môi trường anaconda python, hãy làm theo các bước sau: 

### Cài đặt Anaconda Python

1. Tải phiên bản anaconda mới nhất từ [trang web anaconda](https://www.anaconda.com/download).
2. Làm theo hướng dẫn cài đặt theo hệ điều hành của bạn (Windows, macOS, Linux).
3. Anaconda có bao gồm một phiên bản Python tích hợp
4. Tạo và kích hoạt môi trường ảo
Vì easyocr cần pytorch mà pytorch chỉ đang hỗ trợ phiên bản python 3.11 trở xuống trên conda nên ta sẽ cài bản python 3.11

```bash
conda create -n text_extraction_env python=3.11 -y
conda activate text_extraction_env
```

### Cài đặt EasyOCR

Để sử dụng Easy OCR, trước tiên chúng ta cần cài đặt PyTorch. PyTorch là một thư viện deep learning, và Easy OCR được xây dựng trên nền tảng này. Cài đặt PyTorch trên hệ điều hành của bạn và kiểm tra xem máy tính có hỗ trợ GPU hay không.

1. Cài đặt để chạy

```bash 
conda install opencv-python easyocr pytorch torchvision torchaudio tensorflow pillow=9.4 -c pytorch --name text_extraction_env
```
Lưu ý, nếu các bước sau bị lỗi thì chạy lại lệnh dưới để chạy trên cpu
- Cài đặt để chạy trên cpu (Terminal,Command Promp, Powershell)
  
```bash
conda install tensorflow-cpu cpuonly -c pytorch --name text_extraction_env
```

Sau khi cài đặt xong, chúng ta có thể import Easy OCR vào dự án Python của mình bằng cách sử dụng:

```python
import easyocr
```

## Cách Sử Dụng
- Đặt các hình ảnh chứa văn bản vào thư mục của dự án.
- Chạy OCR trên một hình ảnh bằng đoạn mã trên.
- Chỉnh sửa mã để trích xuất và xử lý văn bản theo nhu cầu.

### Trích xuất văn bản từ hình ảnh

Để trích xuất văn bản từ hình ảnh bằng Easy OCR, chúng ta cần đầu vào một hình ảnh và sử dụng mã sau:
```python
import easyocr
reader = easyocr.Reader(['en']) # Khai báo ngôn ngữ để trích xuất văn bản (trong trường hợp này là tiếng Anh)
result = reader.readtext('path/to/image.jpg') # Đường dẫn đến hình ảnh cần trích xuất
print(result) # Hiển thị kết quả trích xuất văn bản từ hình ảnh
```
### Hiển thị kết quả bằng OpenCV

Sau khi trích xuất văn bản từ hình ảnh, chúng ta có thể sử dụng OpenCV để hiển thị kết quả trích xuất lên hình ảnh gốc. Để làm điều này, chúng ta cần sử dụng mã sau:

```python
import cv2

image = cv2.imread('path/to/image.jpg') # Đọc hình ảnh
for detection in result:
top_left = tuple(detection[0][0]) # Tọa độ góc trên bên trái
bottom_right = tuple(detection[0][2]) # Tọa độ góc dưới bên phải
text = detection[1] # Văn bản đã trích xuất

cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1) # Vẽ đường viền xung quanh văn bản
cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1) # Hiển thị văn bản

cv2.imshow('Result', image) # Hiển thị hình ảnh kết quả
cv2.waitKey(0) # Đợi người dùng nhấn phím bất kỳ để đóng cửa sổ
```
### Xử lý hình ảnh có nhiều dòng văn bản

Khi xử lý hình ảnh có nhiều dòng văn bản, chúng ta cần duyệt qua từng dòng và hiển thị kết quả trích xuất trên từng dòng. Để làm điều này, chúng ta có thể sử dụng mã sau:

```python
import cv2

image = cv2.imread('path/to/image.jpg') # Đọc hình ảnh
for detection in result:
for line in detection:
top_left = tuple(line[0]) # Tọa độ góc trên bên trái
bottom_right = tuple(line[2]) # Tọa độ góc dưới bên phải
text = line[1] # Văn bản đã trích xuất

cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1) # Vẽ đường viền xung quanh văn bản
cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1) # Hiển thị văn bản

cv2.imshow('Result', image) # Hiển thị hình ảnh kết quả
cv2.waitKey(0) # Đợi người dùng nhấn phím bất kỳ để đóng cửa sổ
```

- Chạy OCR trên một hình ảnh bằng đoạn mã trên.
- Chỉnh sửa mã để trích xuất và xử lý văn bản theo nhu cầu.
