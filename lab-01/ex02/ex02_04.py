# Tạo một danh sách rỗng
j=[]
# Duyệt từ 2000->3200, kiểm tra xem i có chia hết cho 7 và không phải là bội số của 5 không
for i in range(2000,3200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(', '.join(j))