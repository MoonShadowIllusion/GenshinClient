# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CoopPointUpdateNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .CoopPoint import *


@dataclass
class CoopPointUpdateNotify(betterproto.Message):
    """
    CmdId: 1991 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    coop_point: "CoopPoint" = betterproto.message_field(13)