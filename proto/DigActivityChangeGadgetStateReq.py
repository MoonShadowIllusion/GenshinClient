# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DigActivityChangeGadgetStateReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DigActivityChangeGadgetStateReq(betterproto.Message):
    """
    CmdId: 8464 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(10)
