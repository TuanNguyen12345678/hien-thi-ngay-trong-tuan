# Hiển thi ngày trong tuần:
import math
def ngaytrongtuan():
    try:
        a=float(input('nhap so tu ban phim: '))
        if a==1:
            print('CHỦ NHẬT')
        elif a==2:
            print(' THỨ HAI')
        elif a==3:
            print('THỨ BA')
        elif a==4:
            print('THỨ TƯ')
        elif a==5:
            print('THỨ NĂM')
        elif a==6:
            print('THỨ 6')
        elif a==7:
            print('THỨ BẢY')
        else:
            print('KHÔNG PHẢI CÁC NGÀY TRONG TUẦN')
    except:
        print('nhập đầu vào chưa đúng')
if __name__=="__main__":
    ngaytrongtuan()