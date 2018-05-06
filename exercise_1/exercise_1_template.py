# Các thao tác trong file này đều có thể được thực hiện dễ dàng bằng thư viện pandas. Tuy nhiên
# để các bạn làm quen hơn với Python, hãy cố gắng sử dụng những lệnh căn bản nhất của Python. Từ đó
# hi vọng các bạn thấy được các thư viện như Pandas, Numpy giúp chúng ta tiết kiệm thời gian cho
# những thao tác quen thuộc này thế nào

# Trước tiên chúng ta hãy học đọc nội dung trong file .csv bằng Python. Trong Pandas việc này rất
# đơn giản, chỉ cần dùng pandas.read_csv("filename") là ta đã nhập dữ liệu trong filename.csv vào
# một dataframe. Tuy nhiên nếu chỉ sử dụng Python thuần tuý, ta cần đến module csv.
import csv

# Sau đây là các mở file Hanoi.csv bằng Python. Ta sẽ lưu dữ liệu của file này vào list
# monthly_weather
monthly_weather = []
with open('Hanoi.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        monthly_weather.append(row)

# Checkpoint 1: Hãy in monthly_weather ra và nhận xét về loại dữ liệu của các thành phần bên trong.
# (Tham khảo qua https://docs.python.org/3/library/collections.html#collections.OrderedDict).
# TODO


# Dùng for loop, ta có thể in ra từng row trong monthly_weather. (Hãy uncomment những dòng sau)
#for month in monthly_weather:
#    print(month)


    
# Checkpoint 2: Dùng for loop, với mỗi row trong monthly_weather, in ra các keys của row
# TODO

# Checkpoint 3: Tìm tháng có số ngày mưa (rainy days) lớn nhất trong năm.
# Các bạn chú ý đối chiếu lại với dữ liệu trong file csv ban đầu. Nếu cần, hàm int(string) sẽ giúp
# lấy giá trị số của một xâu.
# TODO

