# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlessingScanReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BlessingScanReq(betterproto.Message):
    """
    CmdId: 2081 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(11)