# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerConfirmMatchReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MatchType import *


@dataclass
class PlayerConfirmMatchReq(betterproto.Message):
    """
    CmdId: 4172 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    match_type: "MatchType" = betterproto.enum_field(12)
    is_agreed: bool = betterproto.bool_field(10)
