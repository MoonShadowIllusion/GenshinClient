# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlessingGiveFriendPicReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BlessingGiveFriendPicReq(betterproto.Message):
    """
    CmdId: 2062 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    uid: int = betterproto.uint32_field(11)
    pic_id: int = betterproto.uint32_field(3)
