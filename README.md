# Telegram  Bot

A Telegram Bot for sending content with video, rich text and buttons.

一个用于发送信息的Telegram Bot，支持视频、富文本和按钮功能。

## Features | 功能

- Display video at the top of the message
- Show formatted text (supports Markdown and hyperlinks) in the middle
- Include clickable buttons at the bottom

---

- 顶部显示视频
- 中间显示格式化文本（支持Markdown格式和超链接）
- 底部显示可跳转的按钮

## Installation | 安装

1. Clone the repository and enter directory
2. Install dependencies:

---

1. 克隆项目并进入目录
2. 安装依赖：

```bash
pip install -r requirements.txt
```

## Configuration | 配置

Edit the `.env` file and add your Bot Token:

---

编辑`.env`文件，填入你的Bot Token：

```
BOT_TOKEN=your_bot_token_here
```

You can get a token from BotFather on Telegram.

你可以从Telegram的BotFather获取Token。


## Customizing Content | 自定义内容

In the `webapp_bot.py` file, you can modify these variables to customize content:

- `VIDEO_URL`: Video URL
- `PROMO_TEXT`: Promotional text (supports Markdown)
- `BUTTONS`: Button configuration (text and URLs)
- `WEBAPP_URL`: WebApp URL for the Open button

---

在`webapp_bot.py`文件中，你可以修改以下变量来自定义内容：

- `VIDEO_URL`: 视频URL
- `PROMO_TEXT`: 促销文本（支持Markdown格式）
- `BUTTONS`: 按钮配置（文本和URL）
- `WEBAPP_URL`: "Open"按钮打开的WebApp URL

## Running | 运行

```bash
python webapp_bot.py
```

## Usage | 使用方法

Add your bot on Telegram and use these commands:

- `/start` - Start interaction and view promotional content
- `/help` - Display help information
- `/open` - Show WebApp button

---

在Telegram中添加你的bot，然后使用以下命令：

- `/start` - 开始交互并查看促销内容
- `/help` - 显示帮助信息
- `/open` - 显示WebApp按钮 