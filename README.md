# GXA 密码学 × 安全公开课

用真实的被盗和攻击事故来教密码学。每讲从一个事故切入，倒推出背后的密码学原语，再用一道练习把攻击做出来。

共 12 讲，每讲约 30 分钟。面向有基础编程能力的高校学生，不要求密码学先修。

状态：建设中。

## 课程范围

本课讲密钥和签名：密钥怎么生成和派生，签名怎么产生、授权了什么、怎么被验证，以及托管系统里这些环节怎么出错。

不在范围内：零知识证明的系统讲解、通信加密。

## 大纲

| 讲 | 主题 | 事故 |
|---|---|---|
| [00](lecture-00/) | 开始之前（文字版） | |
| **模块一：密钥是怎么丢的** | | |
| [01](lecture-01/) | 课程地图与椭圆曲线 | 币安 2026、Bitget 2026 |
| [02](lecture-02/) | 随机数与熵 | Profanity / Wintermute 2022、Milk Sad 2023 |
| [03](lecture-03/) | 助记词、派生与 keystore | Slope 钱包 2022 |
| **模块二：签名是怎么被伪造和滥用的** | | |
| [04](lecture-04/) | ECDSA 与 nonce 重用 | PS3 2010、Anyswap 2021 |
| [05](lecture-05/) | 哈希与 Merkle 证明 | BNB Bridge 2022 |
| [06](lecture-06/) | 验签错误与签名可塑性 | Wormhole 2022 |
| [07](lecture-07/) | 签名绑定的上下文：链 ID 与 EIP-712 | Optimism OP 事件 2022、spWETH permit 盗签 2024 |
| **模块三：密钥没丢，钱为什么还是丢了** | | |
| [08](lecture-08/) | 确定性 nonce 与格攻击入门 | 比特币链上偏置 nonce 研究 |
| [09](lecture-09/) | 多签、盲签与审批系统 | Bybit 2025、Radiant 2024 |
| [10](lecture-10/) | EIP-7702 授权与委托 | 币安 2026 |
| [11](lecture-11/) | 秘密共享与门限签名 | Ronin 2022、Harmony 2022 |
| [12](lecture-12/) | MPC 协议实现漏洞 | BitForge 2023 |

## 怎么学

1. 读 [第 0 讲](lecture-00/) 搭好环境。
2. 在 B 站学习该讲（搜索“GXA 密码学训练营”），再读该讲目录下的讲义。
3. 做 `exercise/` 里的练习，在本地跑判分测试。
4. 12 道必做题完成 10 道算结课，第 8 讲不强制。

## 排行榜

在自己的 fork 里通过测试后，提一个 PR 把 GitHub 用户名加到下表。

| 用户名 | 完成讲数 |
|---|---|
| [mia03ther](https://github.com/mia03ther) | 1 |

## 其他资料

- [签名与密钥安全检查清单](checklist.md)
- [案例核对表](docs/case-verification.md)：每个事故的核对结果和来源链接
- [币安 2026 事件链上数据核对](docs/binance-onchain.md)

## 许可

- 代码：MIT，见 [LICENSE](LICENSE)。
- 讲义和其他文字内容：CC BY 4.0，见 [LICENSE-CONTENT](LICENSE-CONTENT)。

## 致谢

Supported by GCC（华语公共物品基金）。

由 GXA 广州区块链大学生协会制作。
