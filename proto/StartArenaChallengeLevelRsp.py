# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: StartArenaChallengeLevelRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class StartArenaChallengeLevelRsp(betterproto.Message):
    """
    CmdId: 2125 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    arena_challenge_level: int = betterproto.uint32_field(1)
    retcode: int = betterproto.int32_field(9)
    gadget_entity_id: int = betterproto.uint32_field(3)
    arena_challenge_id: int = betterproto.uint32_field(6)
