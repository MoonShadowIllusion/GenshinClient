# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayGuestReplyNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ScenePlayGuestReplyNotify(betterproto.Message):
    """
    CmdId: 4423 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    play_id: int = betterproto.uint32_field(13)
    guest_uid: int = betterproto.uint32_field(12)
    is_agree: bool = betterproto.bool_field(3)