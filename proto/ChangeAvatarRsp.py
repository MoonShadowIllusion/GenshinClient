# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChangeAvatarRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChangeAvatarRsp(betterproto.Message):
    """
    CmdId: 1607 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    skill_id: int = betterproto.uint32_field(3)
    retcode: int = betterproto.int32_field(10)
    cur_guid: int = betterproto.uint64_field(4)
