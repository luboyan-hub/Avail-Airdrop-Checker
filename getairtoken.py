# -*- coding: utf-8 -*-
import web3
import requests
import time  # 导入time模块
from eth_account.messages import defunct_hash_message

# 连接到以太坊节点
web3 = web3.Web3(web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/RVFr1wst0ojqF-UlHe_k7pEECIAPLRN-'))


def clean_private_key(private_key):
    # 去除'0x'前缀（如果存在）
    if private_key.startswith('0x'):
        private_key = private_key[2:]
    # 验证私钥是否只包含十六进制字符
    if not all(c in '0123456789abcdefABCDEF' for c in private_key):
        raise ValueError("私钥包含非十六进制字符")
    # 验证私钥长度是否正确（64个字符）
    if len(private_key) != 64:
        raise ValueError("私钥长度不正确")
    return private_key

# def sign_message(web3, private_key, message):
#     cleaned_private_key = clean_private_key(private_key)
#     account = web3.eth.account.from_key(cleaned_private_key)
#     signature = account.sign_message(message)
#     return signature.hex()

def sign_message(web3, private_key, message):
    cleaned_private_key = clean_private_key(private_key)
    # 计算消息的Keccak哈希
    message_hash = defunct_hash_message(text=message)
    # 使用私钥创建账户对象
    account = web3.eth.account.from_key(cleaned_private_key)
    # 签名消息哈希
    signed_message = account.signHash(message_hash)
    # 返回签名的十六进制字符串
    return signed_message.signature.hex()

def check_airdrop(address, private_key):
    # 获取当前时间戳
    current_time = int(time.time())
    # 准备要签名的消息
    sign_data = f"Greetings from Avail!\n\nSign this message to check your eligibility. This signature will not cost you any fees.\n\nTimestamp: {current_time}"
    # 生成签名
    signature = sign_message(web3, private_key, sign_data)  # 确保传递所有需要的参数
    headers = {
        "Host": "claim-api.availproject.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "content-type": "application/json",
    }
    url = 'https://claim-api.availproject.org/check-rewards'
    data = {
        "account": address,
        "type": "ETHEREUM",
        "timestamp": current_time,
        "signedMessage": signature
    }

    # 发送请求并获取响应
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # 如果响应状态码不是200，将抛出异常
        data = response.json()
        if data.get('message') == 'Claim':
            print(f"{address} - available")
        else:
            print(f"{address} - No")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def main():
    # 从文件中读取账户信息
        # 读取账户信息文件
    with open('avail.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            address, private_key = line.split('----')
            print(address, private_key)
            time.sleep(1)
            check_airdrop(address, private_key)


if __name__ == "__main__":
    main()