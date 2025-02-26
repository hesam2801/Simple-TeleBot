import logging
import requests
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def usd_price_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("10000!")


def get_crypto_price(symbol: str) -> str:
    """Fetch the latest price of the given cryptocurrency symbol."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if symbol in data:
            price = data[symbol]["usd"]
            return f"The current price of {symbol.upper()} is ${price}"
        else:
            return "Invalid currency symbol. Please try again!"
    else:
        return "Failed to retrieve price data. Try again later."


async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles commands like /price_btc to fetch cryptocurrency prices."""
    command_text = update.message.text.lower()
    crypto_dict = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "usdt": "tether",
        "bnb": "binance coin",
        "xrp": "xrp",
        "ada": "cardano",
        "doge": "dogecoin",
        "sol": "solana",
        "dot": "polkadot",
        "matic": "polygon",
        "shib": "shiba inu",
        "ltc": "litecoin",
        "trx": "tron",
        "bch": "bitcoin cash",
        "avax": "avalanche",
        "xlm": "stellar",
        "link": "chainlink",
        "uni": "uniswap",
        "xmr": "monero",
        "algo": "algorand",
        "atom": "cosmos",
        "vet": "vechain",
        "icp": "internet computer",
        "fil": "filecoin",
        "mana": "decentraland",
        "sand": "the sandbox",
        "egld": "multiversx (formerly elrond)",
        "theta": "theta network",
        "axs": "axie infinity",
        "ftm": "fantom",
        "grt": "the graph",
        "eos": "eos",
        "xtz": "tezos",
        "aave": "aave",
        "flow": "flow",
        "chz": "chiliz",
        "near": "near protocol",
        "qnt": "quant",
        "ldo": "lido dao",
        "hbar": "hedera",
        "crv": "curve dao token",
        "ksm": "kusama",
        "rune": "thorchain",
        "enj": "enjin coin",
        "zec": "zcash",
        "snx": "synthetix",
        "bat": "basic attention token",
        "kava": "kava",
        "gala": "gala",
        "1inch": "1inch",
        "cake": "pancakeswap",
        "rose": "oasis network",
        "dash": "dash",
        "ar": "arweave",
        "stx": "stacks",
        "xdc": "xdc network",
        "ankr": "ankr",
        "hnt": "helium",
        "celo": "celo",
        "yfi": "yearn.finance",
        "omg": "omg network",
        "icx": "icon",
        "zil": "zilliqa",
        "bnt": "bancor",
        "comp": "compound",
        "waves": "waves",
        "srm": "serum",
    }
    if command_text.startswith("/price_"):
        currency = command_text.replace("/price_", "")
        price_info = get_crypto_price(crypto_dict[currency] if currency in crypto_dict else currency)
        await update.message.reply_text(price_info)
    else:
        await update.message.reply_text("Invalid command format. Use /price_currency (e.g., /price_btc)")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("1").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("usd_price", usd_price_command))
    application.add_handler(MessageHandler(filters.Regex(r"^/price_\w+$"), price_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
