print("Nhập các dòng từ văn bản (Nhập 'Done' để kết thúc: ")
lines=[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
# Chuyển thành chữ in hoa
for line in lines:
    print(line.upper())