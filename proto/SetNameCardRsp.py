# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetNameCardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetNameCardRsp(betterproto.Message):
    """
    CmdId: 4093 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    name_card_id: int = betterproto.uint32_field(11)
    retcode: int = betterproto.int32_field(12)
