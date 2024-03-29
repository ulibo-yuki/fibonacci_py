import datetime
import os
import sys

def write_csv(n, count, file_name):
    with open(file_name, 'a') as c:
        c.write(str(count) + "," + str(n) + "\n")
        print("\r" + str(count) + "回書き込み", end="")

while True:
    #設定の入力
    print("1. n番目を求めますか?\n2. n番目番目まで全ての値を求めますか?\n1か2を入力してください。")
    All_cal = False
    chosen_input = input()
    if chosen_input != "1":
        All_cal = True
    print("nの値を入力してください。")
    time_cal = int(input())
    #データの初期化
    list_fibonacci = [0,1,]
    csv_file_title = f"fibonacci_{datetime.datetime.now().strftime('%m_%d_%H:%M:%S')}.csv"
    # パスの設定
    if getattr(sys, 'frozen', False):
        parent_path = os.path.dirname(sys.executable)
        # ファイルフォルダ作成
        if All_cal == True:
            os.makedirs(f"{parent_path}/csv_files", exist_ok=True)
            csv_file_title = f"{parent_path}/csv_files/{csv_file_title}"
            with open(csv_file_title, 'w') as f:
                f.write("time,value\n")
    else:
        if All_cal == True:
            os.makedirs("csv_files", exist_ok=True)
            csv_file_title = f"csv_files/{csv_file_title}"
            with open(csv_file_title, 'w') as f:
                f.write("time,value\n")
    # 演算
    count = 1
    for i in range(time_cal - 2):
        list_fibonacci.append(list_fibonacci[i]+list_fibonacci[i + 1])
        i -= 1
        print("\r" + str(count) + "回演算", end="")
        count += 1
    print("演算終了")
    #出力
    if All_cal == False: # 1.n番目を抜き出す
        print(list_fibonacci[len(list_fibonacci) - 1])
    else: # 2.全ての値を求める
        # 書き込み
        count = 1
        for n in list_fibonacci:
            write_csv(n, count, csv_file_title)
            count += 1
        print("\n書き込み完了")
    print("もう1度計算しますか?y/n")
    if input() != "y":
        break