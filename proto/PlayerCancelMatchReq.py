# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerCancelMatchReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MatchType import *


@dataclass
class PlayerCancelMatchReq(betterproto.Message):
    """
    CmdId: 4157 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    match_type: "MatchType" = betterproto.enum_field(11)
