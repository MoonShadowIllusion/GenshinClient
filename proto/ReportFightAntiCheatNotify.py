# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReportFightAntiCheatNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ReportFightAntiCheatNotify(betterproto.Message):
    """
    CmdId: 368 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cheat_count: int = betterproto.uint32_field(8)
    cheat_type: int = betterproto.uint32_field(12)