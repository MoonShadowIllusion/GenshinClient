# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AsterMiscInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AsterMiscInfoNotify(betterproto.Message):
    """
    CmdId: 2036 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    aster_token: int = betterproto.uint32_field(2)
    aster_credit: int = betterproto.uint32_field(15)