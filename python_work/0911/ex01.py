st = "1234"
st1 = "1234-1234"
print(st.isdigit())

if st.isdigit():
    print('숫자로만 이루어져 있습니다.')

if st1.isdigit():
    print('숫자로만 이루어져 있습니다.')
else:
    print('문자와 숫자로 이루어져 있습니다.')