for num in range(1, 101):
    string = ''

    # ここから記述
    
    # 現在走査している数字numが3の倍数なら，出力文字列stringの内容を'Fizz'とする．
    if num % 3 == 0:
        string = 'Fizz'
    
    # 現在走査している数字numが5の倍数なら，出力文字列stringの末尾に'Buzz'を追加する．
    if num % 5 == 0:
        string = string + 'Buzz'
    
    # 出力文字列stringが空文字列であれば，現在走査している数字numは3の倍数でも5の倍数でもない．
    # 故にnumをstringの内容とする．
    if string == '':
        string = num
    
    # ここまで記述

    print(string)