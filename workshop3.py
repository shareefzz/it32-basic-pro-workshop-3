num = int(input("บอสสั่งให้ไปเก็บส่วยกี่ร้าน? : "))
total = 0

for i in range(num):
    money = int(input(f"เก็บเงินจากร้านที่ {i+1} : "))
    total = money + total

print(f"สรุปมีร้าน {num} ร้านและยอดเงินทั้งหมด {total} บาท")