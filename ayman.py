# برنامج للتحقق إذا كان العدد المدخل زوجي أو فردي
def check_number(number):
    if number % 2 == 0:
        print(f"{number} هو عدد زوجي.")
    else:
        print("Yes") # yes اذا كان فردي

# طلب إدخال العدد من المستخدم
try:
    num = int(input("أدخل عددًا صحيحًا: "))
    check_number(num)
except ValueError:
    print("الرجاء إدخال عدد صحيح.")
