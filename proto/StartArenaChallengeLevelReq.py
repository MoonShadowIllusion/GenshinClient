# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: StartArenaChallengeLevelReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class StartArenaChallengeLevelReq(betterproto.Message):
    """
    CmdId: 2127 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    arena_challenge_id: int = betterproto.uint32_field(4)
    gadget_entity_id: int = betterproto.uint32_field(5)
    arena_challenge_level: int = betterproto.uint32_field(2)
