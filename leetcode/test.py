# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 11:02 上午
# @Author  : ZolHo
# @FileName: test.py

from array import array
from typing import List
import base64
from collections import deque
a= [False, False,1]
print(a[:1],a[1:])

s = """tx.origin 为 Solidity 智 能 合 约 中 的 全 局 变 量 ，通 过
回 溯 整 个 调 用 栈 并 返 回 原 始 发 送 者 的 账 户 地 址 。 使
用 tx . origin 来 检 测 合 约 调 用 者 可 能 会 使 合 约 变 得 脆
弱 。 采 用 tx . origin 进 行 授 权 ， 授 权 地 址 将 会 被 存 储
到 tx . origin ， 对 方 可 以 使 用 fallback 函 数 调 用 合 约 并
获 得 授 权 。 msg . sender 是 当 前 发 生 调 用 的 账 户 或 合约 地 址 。 在 智 能 合 约 授 权 时 应 尽 量 使 用 msg . sender
代 替 tx . origin 。
利 用 tx . origin 攻 击 需 要 提 前 部 署 攻 击 者 合 约 ，
通 过 钓 鱼 等 手 段 使 漏 洞 合 约 向 攻 击 者 合 约 转 账 ， 达
到 调 用 攻 击 者 的 fallback 函 数 和 获 取 tx . origin 值 的
目 的 。 由 于 tx . origin 指 向 最 初 发 起 交 易 的 地 址 ， 通
过 fallback 函 数 调 用 漏 洞 合 约 中 以 tx . origin 作 为 授
权 的 转 账 函 数 ， 授 权 会 获 得 通 过 ， 攻 击 者 因 此 可 以
发 起 恶 意 转 账 操 作 。"""
s = s.replace(" ", "")
s = s.replace("\n", "")
print(s)