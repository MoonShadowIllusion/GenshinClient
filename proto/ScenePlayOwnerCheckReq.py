# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayOwnerCheckReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ScenePlayOwnerCheckReq(betterproto.Message):
    """
    CmdId: 4448 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    play_id: int = betterproto.uint32_field(9)
    is_skip_match: bool = betterproto.bool_field(6)
