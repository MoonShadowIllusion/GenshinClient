# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerPropChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerPropChangeNotify(betterproto.Message):
    """
    CmdId: 139 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    prop_delta: int = betterproto.uint32_field(13)
    prop_type: int = betterproto.uint32_field(12)