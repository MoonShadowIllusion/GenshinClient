# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SeaLampTakePhaseRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SeaLampTakePhaseRewardRsp(betterproto.Message):
    """
    CmdId: 2190 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    phase_id: int = betterproto.uint32_field(2)
    retcode: int = betterproto.int32_field(6)