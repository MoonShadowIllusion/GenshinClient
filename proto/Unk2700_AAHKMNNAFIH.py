# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_AAHKMNNAFIH.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_ICPNKAALJEP import *


@dataclass
class Unk2700_AAHKMNNAFIH(betterproto.Message):
    """
    CmdId: 8231 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gallery_id: int = betterproto.uint32_field(13)
    settle_info: "Unk2700_ICPNKAALJEP" = betterproto.message_field(12)