#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    MenuButtonWebApp,
    Bot,
    BotCommand,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get BOT_TOKEN from environment variables
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    logger.error("Please set BOT_TOKEN in .env file")
    exit(1)

# Web app URL (actual UPUP task link)
WEBAPP_URL = "https://task.upupusa.com/#/pages/index/index?code=iob1y"

# Video URL (sample video URL, replace with actual video when needed)
VIDEO_URL = "https://core.telegram.org/file/464001679/11aa9/KQx_BlPVXRo.4922145.mp4/c65433c8ac11a347a8"

# Tips
Tip_TEXT = """
📌 Available Commands:
/start - Start interaction and view promotional content
/open - Show WebApp button
"""

# Promotional text content (supports Markdown formatting)
PROMO_TEXT = """
⭐ *Join Now to Win Huge Rewards!*

⭐ *Step 1:* Sign up and scan the QR code to get Huge Rupees.
"Scan once, stay online, make money forever"

⭐ *Step 2:* Invite friends to join the money-making program and get invitation bonus
"Once your friends sign up and scan their own QR code, you can earn huge commissions"

⭐ *Step 3:* Watch the tutorial video above 👆 👆
Learn how to scan the code using WhatsApp and claim your rewards.

👉 [Click to Open UPUP](https://task.upupusa.com/#/pages/index/index?code=iob1y)
"""

# Button configuration
BUTTONS = [
    {
        "text": "🐶 UPUP  🐶",
        "url": "https://task.upupusa.com/#/pages/index/index?code=iob1y",
    },
    {"text": "📣 Join UPUP Community 📣", "url": "https://t.me/upup550"},
    {
        "text": "📱 Find Us on WhatsApp 📱",
        "url": "https://whatsapp.com/channel/0029Vb0Kb1r42DckfMHnBI29",
    },
]


async def set_menu_button(bot: Bot) -> None:
    """Set the Menu Button in the chat list as WebApp button"""
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="💰Earn💰", web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )


async def set_commands(bot: Bot) -> None:
    """Set bot commands to display /start in the input field"""
    commands = [
        BotCommand("start", "Start and view information"),
        # BotCommand("help", "Get help information"),
        BotCommand("open", "Open UPUP application"),
    ]
    await bot.set_my_commands(commands)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Response to /start command, sends a message with video, text and buttons"""
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Set menu button (displays Open button in chat list)
    await set_menu_button(context.bot)

    # Tip Msg
    await update.message.reply_text(Tip_TEXT.strip())

    # Create inline buttons
    inline_keyboard = []
    # Only add regular URL buttons
    for button in BUTTONS:
        inline_keyboard.append(
            [InlineKeyboardButton(button["text"], url=button["url"])]
        )

    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    try:
        # Send video and text in the same message
        await context.bot.send_video(
            chat_id=chat_id,
            video=VIDEO_URL,
            caption=PROMO_TEXT,  # Use PROMO_TEXT as video caption
            parse_mode=ParseMode.MARKDOWN,  # Enable Markdown formatting
            reply_markup=inline_markup,  # Add buttons
            supports_streaming=True,
        )
    except Exception as e:
        logger.error(f"Failed to send video: {e}")
        # If video sending fails, only send text and buttons
        await update.message.reply_text(
            text=f"*Video loading failed*\n\n{PROMO_TEXT}",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=inline_markup,
        )

    # Create a persistent keyboard with Web App button - temporarily commented out
    """
    keyboard = [
        [KeyboardButton("Open UPUP App", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # Send keyboard button prompt
    await update.message.reply_text(
        "You can also use the button below to quickly open the app:",
        reply_markup=reply_markup
    )
    """


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Response to /help command"""
    # Set menu button
    await set_menu_button(context.bot)

    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start interaction, view video, information and app entry\n"
        "/help - Display this help information\n"
        "/open - Show Web app button"
    )


async def open_webapp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show Web App button"""
    # Create inline button with Web App link
    keyboard = [[InlineKeyboardButton("Open UPUP", web_app=WebAppInfo(url=WEBAPP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Set menu button
    await set_menu_button(context.bot)

    await update.message.reply_text(
        "Click the button below to open UPUP app:", reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages"""
    # Set menu button
    await set_menu_button(context.bot)

    await update.message.reply_text(
        "Please use the /start command to view our video, information and open the app."
    )


async def post_init(application: Application) -> None:
    """Set menu button and commands after application startup"""
    await set_menu_button(application.bot)
    await set_commands(application.bot)  # Set command menu


def main() -> None:
    """Start the bot"""
    # Create application and pass in token
    app = Application.builder().token(TOKEN).post_init(post_init).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("open", open_webapp))

    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot started!")
    print("Press Ctrl+C to exit")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
