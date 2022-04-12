import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from ..Config import Config
from .client import JmthonUserBotClient

__version__ = "2.10.6"

loop = None


jmthon.tgbot = tgbot = JmthonUserBotClient(
    session="JmthonTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
#
