# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MpPlayGuestReplyNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MpPlayGuestReplyNotify(betterproto.Message):
    """
    CmdId: 1812 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    uid: int = betterproto.uint32_field(7)
    is_agree: bool = betterproto.bool_field(4)
    mp_play_id: int = betterproto.uint32_field(14)
