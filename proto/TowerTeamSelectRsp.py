# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerTeamSelectRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TowerTeamSelectRsp(betterproto.Message):
    """
    CmdId: 2403 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(8)