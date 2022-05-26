def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    # 探索範囲の先頭のインデックスtopを初期化
    top = 0
    # 探索範囲の終端のインデックスlastを初期化
    last = len(sorted_array) - 1
    
    
    while top <= last:
        
        # 探索範囲の中間のインデックスmiddleを求める
        middle = int((top + last) / 2)

        # 探索対象の番号が探索範囲の中間の番号より大きければ，中間の番号より大きい範囲を探索する.
        # よって，探索範囲の先頭のインデックスを中間のインデックスより1高い値とする，
        if target_number > sorted_array[middle]:
            top = middle + 1
            
        # 探索対象の番号が探索範囲の中間の番号より小さければ，中間の番号より小さい範囲を探索する.
        # よって，探索範囲の末尾のインデックスlastを中間のインデックスより1低い値とする，
        elif target_number < sorted_array[middle]:
            last = middle - 1
            
        # 探索対象の番号が探索範囲の中間の番号と等しければ，そのインデックスを返却．
        else:
            return middle

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()