import pandas as pd
import numpy as np
import os
import glob
os.chdir(rf'C:\Users')    #保存先入力
list = glob.glob('*.txt')
N = len(list)
Sea = -500      #海面のレベル下げ
Emphasis = 20   #地形の凹凸の強調
Size = 200      #3Dソフトで表示される大きさ1/Size

for i in range(0,N):
    text1 = list[i]
    df = pd.read_csv(text1,encoding = 'cp932', header = None)
    La = []
    Lo = []
    r = []
    def calc_lo(n):
     return n
    for val in df[0]:
     Lo.append(calc_lo(val))
    def calc_la(n):
     return n
    for val in df[1]:
     La.append(calc_la(val))
    def calc_r(n):
     if n == 0:
      return (n-Sea)*Emphasis/1000 + 6378.1
     else:
      return n*Emphasis/1000 + 6378.1
    for val in df[2]:
     r.append(calc_r(val))
    X = [r * np.cos(np.radians(la)) * np.cos(np.radians(lo))/Size for (r, la, lo) in zip(r, La, Lo)]   # 座標系の変換コード。
    Y = [r * np.cos(np.radians(la)) * np.sin(np.radians(lo))/Size for (r, la, lo) in zip(r, La, Lo)]
    Z = [r * np.sin(np.radians(la))/Size for (r, la, lo) in zip(r, La, Lo)]
    df = pd.DataFrame({'X':X,'Y':Y,'Z':Z})   # リストをデータフレームに格納
    df.to_csv(str(text1)+'_earth.csv', sep = ' ', header = False, index = False)   # Blenderに対応するフォーマットへ変換。Excellでセルを分けたい場合はsep = ','とし、csv形式で保存してください。
    os.rename(str(text1)+'_earth.csv',str(text1)+'_earth.txt')


####
