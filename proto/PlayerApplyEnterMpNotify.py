# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerApplyEnterMpNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .OnlinePlayerInfo import *


@dataclass
class PlayerApplyEnterMpNotify(betterproto.Message):
    """
    CmdId: 1826 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    src_thread_index: int = betterproto.uint32_field(5)
    src_app_id: int = betterproto.uint32_field(6)
    src_player_info: "OnlinePlayerInfo" = betterproto.message_field(2)
