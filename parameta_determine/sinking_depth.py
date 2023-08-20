def compute_L_from_formula(Q_val, B_val, c_val, C_val, g_val, G_val, D_val, N_val):
    """ 
    与えられた式 Q = BL{(1+0.3(B/L))cC+(0.5-0.1(B/L)BgG)+gDN} に基づいて L の値を計算する関数。
    
    引数:
    - Q_val: Q の値 - 地盤の支持力
    - B_val: B の値 - 車輪幅
    - c_val: c の値 - 地盤の粘着力
    - C_val: C の値 - 
    - g_val: g の値 - 単位体積重量
    - G_val: G の値 - 
    - D_val: D の値 - 沈下量
    - N_val: N の値 - 
    
    戻り値:
    - L の計算結果
    """
    L_expr = 0.2 * (B_val**3 * G_val * g_val - 3.0 * B_val**2 * C_val * c_val + 10.0 * Q_val) / \
            (B_val * (B_val * G_val * g_val + 2.0 * C_val * c_val + 2.0 * D_val * N_val * g_val))
    return L_expr

# テストの実行
if __name__ == "__main__":
    result = compute_L_from_formula(100, 2, 3, 4, 5, 6, 7, 8)
    print(result)

import math
Radius=0.1
sinking_depth = Radius*(1-math.acos(result/(2*Radius)))
print(sinking_depth)