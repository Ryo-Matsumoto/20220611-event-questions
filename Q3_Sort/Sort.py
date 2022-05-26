def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 先頭から末端に向かって探索を行う制御変数iの初期化
    i = 0
    # 末端から先頭に向かって探索を行う制御変数jの初期化
    j = len(array) - 1
    
    # 無限ループ
    while True:
        
        # 基準値以上の値が見つかるまでiをインクリメント
        # 見つかったときのインデックスがiに格納される
        while i <= len(array) - 1 and array[i] < pivot:
            i = i + 1
        
        # 基準値未満の値が見つかるまでjをデクリメント
        # 見つかったときのインデックスがjに格納され，見つからなかったときは-1が格納される
        while j >= 0 and array[j] >= pivot:
            j = j - 1
            
        # iとjの大小関係が逆転した時点で，「探索がぶつかった」とみなし探索を終了
        if i >= j:
            break
                
        # array[i]とarray[j]の入れ替え
        work = array[i]
        array[i] = array[j]
        array[j] = work
    
    # 基準値未満のグループ
    left = array[:j+1]
    
    # 基準値以上のグループ
    right = array[i:]
    
    # 基準値未満が存在せず全て基準値以上のときは，rightのうち基準値より大きい値についてソート
    if len(left) == 0:
        array = [right[0]] + sort(right[1:])
    
    # そうでなければ，leftとrightの各々についてソート
    else:
        array = sort(left) + sort(right)
    
    return array
    
    # ここまで記述

if __name__ == '__main__':
    main()