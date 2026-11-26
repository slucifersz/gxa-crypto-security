"""第 1 讲判分。默认测 exercise/；设 GXA_SOLUTION=1 测参考答案。"""
import importlib.util
import os
from pathlib import Path

_which = "solution" if os.environ.get("GXA_SOLUTION") else "exercise"
_spec = importlib.util.spec_from_file_location("ecc", Path(__file__).parent.parent / _which / "ecc.py")
ecc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ecc)

# 小曲线上 k·G 的值，和第 1 讲里的网格一致
TOY = {1: (15, 13), 2: (2, 10), 3: (8, 3), 4: (12, 1), 5: (6, 6), 6: (5, 8), 7: (10, 15), 8: (1, 12),
       9: (3, 0), 10: (1, 5), 11: (10, 2), 12: (5, 9), 13: (6, 11), 14: (12, 16), 15: (8, 14),
       16: (2, 7), 17: (15, 4)}


def test_1_inv():
    assert ecc.inv(5, 17) == 7
    for a in range(1, 17):
        assert a * ecc.inv(a, 17) % 17 == 1


def test_2_add():
    G = ecc.TOY_G
    assert ecc.add(G, G, 17) == TOY[2]            # 倍点
    assert ecc.add(TOY[2], G, 17) == TOY[3]       # 两个不同的点相加
    assert ecc.add(G, TOY[17], 17) is None        # G + (−G) = O
    assert ecc.add(None, G, 17) == G              # O 是“零”


def test_3_mul():
    for k, pt in TOY.items():
        assert ecc.mul(k, ecc.TOY_G, 17) == pt
    assert ecc.mul(18, ecc.TOY_G, 17) is None     # 一共 18 个点


def test_4_brute_force():
    for k, pt in TOY.items():
        assert ecc.brute_force(pt) == k


def test_brute_force_infinity_returns_generator_order():
    assert ecc.brute_force(None) == 18
    assert ecc.brute_force(None, g=TOY[9]) == 2


def test_point_with_zero_y_doubles_to_infinity():
    assert ecc.add(TOY[9], TOY[9], ecc.TOY_P) is None


def test_5_secp256k1():
    two_g = ecc.mul(2, ecc.G, ecc.P)
    assert two_g[0] == 0xC6047F9441ED7D6D3045406E95C07CD85C778E4B8CEF3CA7ABAC09B95C709EE5
    assert ecc.mul(ecc.N, ecc.G, ecc.P) is None   # n·G = O


# 进阶题
def test_6_address():
    assert ecc.address(1) == "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf"
