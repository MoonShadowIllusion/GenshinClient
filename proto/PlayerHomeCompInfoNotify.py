# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerHomeCompInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .PlayerHomeCompInfo import *


@dataclass
class PlayerHomeCompInfoNotify(betterproto.Message):
    """
    CmdId: 4880 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    comp_info: "PlayerHomeCompInfo" = betterproto.message_field(4)