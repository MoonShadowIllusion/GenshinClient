# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ProjectorOptionRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ProjectorOptionRsp(betterproto.Message):
    """
    CmdId: 895 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(10)
    retcode: int = betterproto.int32_field(12)
    op_type: int = betterproto.uint32_field(13)
