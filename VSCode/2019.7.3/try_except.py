stra = '3456'
i = 0
while True:
    try:
        i = int('str')
    except Exception as e:
        print(e)
        if i != 3456:
            break
    finally:
        stra = '123456'
        print(int(stra),'over')

