# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DeleteFriendRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DeleteFriendRsp(betterproto.Message):
    """
    CmdId: 4075 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(14)
    retcode: int = betterproto.int32_field(5)
