# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_LCFGKHHIAEH_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_LCFGKHHIAEH_ServerNotify(betterproto.Message):
    """
    CmdId: 4014 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    signature: str = betterproto.string_field(12)
