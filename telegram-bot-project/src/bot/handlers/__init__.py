# This file initializes the handlers for the Telegram bot. 
# It may import and set up various handler functions for processing messages and commands.

from . import command_handlers
from . import message_handlers
from . import callback_handlers

def setup_handlers(dispatcher):
    command_handlers.setup(dispatcher)
    message_handlers.setup(dispatcher)
    callback_handlers.setup(dispatcher)