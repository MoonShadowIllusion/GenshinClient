# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonDieOptionRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .PlayerDieOption import *


@dataclass
class DungeonDieOptionRsp(betterproto.Message):
    """
    CmdId: 948 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(5)
    revive_count: int = betterproto.uint32_field(10)
    die_option: "PlayerDieOption" = betterproto.enum_field(6)