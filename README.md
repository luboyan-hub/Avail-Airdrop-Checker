# Avail-Airdrop-Checker
Avail Airdrop Checker 是一个Python脚本，旨在帮助用户自动化检查和参与Avail项目的空投活动。该脚本通过与以太坊节点的交互，验证用户的私钥，以及发送签名消息来确认用户对特定空投活动的资格。


项目网址：https://claim.availproject.org/
你需要配置的节点申请网站：https://alchemy.com

```markdown
# Get Airdrop Token Script
This Python script is designed to check and claim airdrop tokens for Ethereum addresses. It connects to an Ethereum node, signs a message with a given private key, and then checks the eligibility for an airdrop reward.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- The `web3.py` library for interacting with Ethereum nodes
- The `requests` library for making HTTP requests

You can install the required libraries using pip:
```
pip install web3 requests
```

## Usage
To use the script, follow these steps:

1. Create a text file named `avail.txt` with the following format:
   ```
   address1----private_key1
   address2----private_key2
   ```
   Replace `addressX` with the Ethereum address and `private_keyX` with the corresponding private key.

2. Run the script:
   ```
   python getairtoken.py
   ```

The script will read each line from `avail.txt`, sign a predefined message, and check for airdrop eligibility.

## Features
- Connects to the Ethereum mainnet using Alchemy's HTTP provider.
- Cleans and validates the private key before signing.
- Signs a message to prove ownership of the Ethereum address.
- Checks for airdrop eligibility by sending a POST request to the Avail Project's API.

## Disclaimer
- This script is for educational purposes only.
- Always keep your private keys secure and never expose them in your code or to anyone.
- The script assumes that the Avail Project's API endpoint and message format remain unchanged.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any questions or support, feel free to reach out:
- Email: [201305139@stu.lzjtu.edu.cn](mailto:201305139@stu.lzjtu.edu.cn)
- GitHub: [luboyan-hub](https://github.com/luboyan-hub)
```

请根据你的项目实际情况调整上述内容，比如添加你的电子邮件地址或GitHub用户名。如果你的项目有特定的许可证，也要确保包含正确的许可证文件。此外，如果你的脚本有更复杂的配置或运行要求，你应该在Usage部分提供更详细的说明。