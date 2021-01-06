#問題1
THICKNESS = 0.00008
folded_thickness = THICKNESS*2**43
print("厚さ： {}メートル".format(folded_thickness))

#問題2
answer1 = folded_thickness/1000
#print(answer1)

answer2=answer1 / 10000
print("厚さ： {:.2f}万キロメートル".format(answer2))

moon_distance = 38.40
if answer2 > moon_distance:
  print("月まで届きました。いい夢を！")
else:
  print("月まで届きませんでした。残念！")

#問題3
THICKNESS = 0.00008
for i in range(1, 44):
    THICKNESS *= 2
    answer3 = THICKNESS/10000000
print("厚さ : {:.2f}万キロメートル".format(answer3))

#問題4

# ベキ乗**使う方
import time
start = time.time()
#####
THICKNESS = 0.00008
folded_thickness = THICKNESS*2**43
#print("厚さ： {}メートル".format(folded_thickness))
#####
elapsed_time = time.time() - start
print("ベキ乗**を使う方法")
print("time : {}[s]".format(elapsed_time))

# for文使う方
import time
start = time.time()
#####
THICKNESS = 0.00008
for i in range(1, 44):
    THICKNESS *= 2
    answer3 = THICKNESS/10000000
#print("厚さ : {:.2f}万キロメートル".format(answer3))
#####
elapsed_time = time.time() - start
print("for文を使う方法")
print("time : {}[s]".format(elapsed_time))

'''
%%timeit
#####
THICKNESS = 0.00008
folded_thickness = THICKNESS*2**43
print("厚さ： {}メートル".format(folded_thickness))
#####
%%timeit
#####
THICKNESS = 0.00008
for i in range(1, 44):
    THICKNESS *= 2
    answer3 = THICKNESS/10000000
print("厚さ : {:.2f}万キロメートル".format(answer3))
#####
'''
#問題5
box = []
THICKNESS = 0.00008
for i in range(1, 44):
    THICKNESS *= 2
    box.append(THICKNESS)
    print(box)
#print(answer)
print(len(box))

#問題6
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(box)
plt.show()
'''37回目あたりから急激に厚みが増す'''

#問題7
#パターン1(線の色を緑にする)
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(box, color="green")
plt.show()
#パターン2(ラインの太さを太くする)
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(box, linewidth=4)
plt.show()
#パターン3(マーカーをつける,グリッドを入れる)
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(box, marker="o")
plt.grid()
plt.show()
