# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SelectRoguelikeDungeonCardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SelectRoguelikeDungeonCardRsp(betterproto.Message):
    """
    CmdId: 8138 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    card_id: int = betterproto.uint32_field(9)
    retcode: int = betterproto.int32_field(8)
