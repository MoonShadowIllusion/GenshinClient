# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AddFriendNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .FriendBrief import *


@dataclass
class AddFriendNotify(betterproto.Message):
    """
    CmdId: 4022 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_uid: int = betterproto.uint32_field(11)
    target_friend_brief: "FriendBrief" = betterproto.message_field(10)
