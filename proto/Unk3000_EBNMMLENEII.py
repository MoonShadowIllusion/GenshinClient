# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_EBNMMLENEII.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_JACOCADDNFE import *


@dataclass
class Unk3000_EBNMMLENEII(betterproto.Message):
    """
    CmdId: 24857 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_info_list: List["Unk3000_JACOCADDNFE"] = betterproto.message_field(13)