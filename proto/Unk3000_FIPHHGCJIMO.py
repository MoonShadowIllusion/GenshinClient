# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_FIPHHGCJIMO.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_JACOCADDNFE import *


@dataclass
class Unk3000_FIPHHGCJIMO(betterproto.Message):
    """
    CmdId: 23678 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_info_list: List["Unk3000_JACOCADDNFE"] = betterproto.message_field(6)
