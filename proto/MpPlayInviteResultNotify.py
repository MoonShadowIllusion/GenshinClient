# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MpPlayInviteResultNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MpPlayInviteResultNotify(betterproto.Message):
    """
    CmdId: 1815 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    mp_play_id: int = betterproto.uint32_field(11)
    all_argee: bool = betterproto.bool_field(10)