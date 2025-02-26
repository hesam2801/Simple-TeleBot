# Simple-TeleBot

**Simple-TeleBot** is a Python-based Telegram bot that provides real-time currency prices. Users can input the name of any cryptocurrency, and the bot will return the latest price, making it an essential tool for traders and finance enthusiasts.

## Requirements

Before running the bot, make sure you have Python installed on your machine. You will also need to create a virtual environment for managing dependencies.

### Setting Up the Virtual Environment

1. **Create a virtual environment**:
   ```bash
   python -m venv .venv
2. **Activate the virtual environment**:

On Windows:
```bash
.venv\Scripts\activate
```
On macOS/Linux:
```bash
source .venv/bin/activate
```
3. **Install the required packages**:

```bash
pip install python-telegram-bot
pip install requests
```
## Creating Your Telegram Bot
1. Go to Telegram and search for BotFather.
2. Ensure that BotFather has a star and is verified.
3. Use the command /newbot to create a new bot.
4. Follow the prompts to set a name and username for your bot.
5. After creating the bot, you will receive a token.
### Updating the Bot Token
In your bot's code, locate the following line:
```python
application = Application.builder().token("YOUR_TOKEN_HERE").build()
```
Replace `YOUR_TOKEN_HERE` with the token you received from BotFather.

## Running the Bot
After setting everything up, run the bot with the following command:
```bash
python your_bot_file.py
```
Replace your_bot_file.py with the name of your Python file containing the bot code.

## Commands
- /start: Start the bot and receive a welcome message.
- /help: Get help on how to use the bot.
- /price_currency: Get the current price of a cryptocurrency (e.g., /price_btc for Bitcoin).
## License
This project is licensed under the MIT License - see the LICENSE file for details.
```css
Feel free to customize it further if needed!
```