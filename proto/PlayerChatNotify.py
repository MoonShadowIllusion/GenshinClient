# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerChatNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ChatInfo import *


@dataclass
class PlayerChatNotify(betterproto.Message):
    """
    CmdId: 3010 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    chat_info: "ChatInfo" = betterproto.message_field(3)
    channel_id: int = betterproto.uint32_field(6)