# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AsterLargeInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AsterLargeDetailInfo import *


@dataclass
class AsterLargeInfoNotify(betterproto.Message):
    """
    CmdId: 2146 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    info: "AsterLargeDetailInfo" = betterproto.message_field(10)
