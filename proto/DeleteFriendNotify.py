# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DeleteFriendNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DeleteFriendNotify(betterproto.Message):
    """
    CmdId: 4053 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(12)
