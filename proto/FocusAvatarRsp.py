# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FocusAvatarRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FocusAvatarRsp(betterproto.Message):
    """
    CmdId: 1681 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(5)
    is_focus: bool = betterproto.bool_field(11)
    avatar_guid: int = betterproto.uint64_field(4)