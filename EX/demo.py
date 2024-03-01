import numpy as np
# Sử dụng hàm linspace() trong module numpy
arr = np.linspace(0, 1, 5)
print(arr)  # Kết quả: [0.   0.25 0.5  0.75 1.  ]


from random import randint
# Sử dụng hàm randint() từ module random
num = randint(1, 10)
print(num)  # Kết quả: một số ngẫu nhiên từ 1 đến 10

from statistics import *

# Sử dụng các hàm tính toán thống kê từ module statistics
data = [1, 2, 3, 4, 5]
mean_value = mean(data)
median_value = median(data)
print(mean_value)   # Kết quả: 3.0
print(median_value) # Kết quả: 3


import turtle

# Khởi tạo Turtle
t = turtle.Turtle()

# Vẽ hình chữ nhật
width = 200
height = 100

t.forward(width)  # Di chuyển về phía trước theo chiều rộng
t.right(90)  # Quay sang phải 90 độ
t.forward(height)  # Di chuyển về phía trước theo chiều cao
t.right(90)  # Quay sang phải 90 độ
t.forward(width)  # Di chuyển về phía trước theo chiều rộng
t.right(90)  # Quay sang phải 90 độ
t.forward(height)  # Di chuyển về phía trước theo chiều cao

# Kết thúc chương trình
turtle.done()

# số nguyên dương 
year = 2017
# số thập phân 
dollarExchangeRate = 22727.50
