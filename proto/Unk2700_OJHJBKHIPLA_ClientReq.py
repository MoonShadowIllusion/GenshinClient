# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_OJHJBKHIPLA_ClientReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_OJHJBKHIPLA_ClientReq(betterproto.Message):
    """
    CmdId: 2009 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(15)
    activity_id: int = betterproto.uint32_field(12)
