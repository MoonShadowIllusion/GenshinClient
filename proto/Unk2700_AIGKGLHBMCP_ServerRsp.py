# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_AIGKGLHBMCP_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_AIGKGLHBMCP_ServerRsp(betterproto.Message):
    """
    CmdId: 6244 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(1)
    room_id: int = betterproto.uint32_field(13)
