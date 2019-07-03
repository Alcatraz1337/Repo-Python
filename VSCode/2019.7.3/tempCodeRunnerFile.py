stra = '3456'
i = 0
while True:
    try:
        i = int('str')
    except:
        print("invalid literal for int() with base 10: 'str'")
        if i != 3456:
            break
    finally:
        stra = '123456'
        print(int(stra),'over')

