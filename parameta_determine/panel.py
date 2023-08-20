#三角形多面体の発電量の推移
import math
import matplotlib.pyplot as plt

# 初期点の座標
point1 = complex((1/math.sqrt(3)) * (math.cos(math.radians(90)) + 1j * math.sin(math.radians(90))))
point2 = complex((1/math.sqrt(3)) * (math.cos(math.radians(-30)) + 1j * math.sin(math.radians(-30))))
point3 = complex((1/math.sqrt(3)) * (math.cos(math.radians(-150)) + 1j * math.sin(math.radians(-150))))

# プロットの初期化
x_values_1 = []
y_values_1 = []
x_values_2 = []
y_values_2 = []

# 累積加算角度が360°になるまで繰り返す
angle = 0
total_power = 0
while angle <= 360:
    # 実部の最大値と最小値を計算
    max_real = max(point1.real, point2.real, point3.real)
    min_real = min(point1.real, point2.real, point3.real)
    diff_real = max_real - min_real

    # グラフ1のデータを追加
    x_values_1.append(angle / 360)
    y_values_1.append(diff_real)

    # グラフ2のデータを追加
    total_power += diff_real * 1232*0.3
    x_values_2.append(angle / 360)
    y_values_2.append(total_power)

    # 各点の座標に角度を加算する
    point1 *= complex(math.cos(math.radians(0.5)), math.sin(math.radians(0.5)))
    point2 *= complex(math.cos(math.radians(0.5)), math.sin(math.radians(0.5)))
    point3 *= complex(math.cos(math.radians(0.5)), math.sin(math.radians(0.5)))

    # 累積加算角度が252の時のtotal_powerの値を出力
    if angle == 252:
        print("累積加算角度が252の時のtotal_powerの値:", total_power)

    # 累積加算角度を更新する
    angle += 0.5

# グラフ1の作成
plt.figure(1)
plt.plot(x_values_1, y_values_1)
plt.xlabel('time (moon day)')
plt.ylabel('Solar Light Receipt (-)')
plt.xlim(0, 1)
plt.ylim(0, max(y_values_1))
plt.xticks([i/10 for i in range(11)])
plt.yticks([i/10 for i in range(int(max(y_values_1)*10)+1)])
plt.grid(True)

# グラフ2の作成
plt.figure(2)
plt.plot(x_values_2, y_values_2)
plt.xlabel('time (moon day)')
plt.ylabel('Generated Power(Wh)')
plt.xlim(0, 1)
plt.ylim(0, max(y_values_2))
plt.xticks([i/10 for i in range(11)])
plt.grid(True)

plt.show()
