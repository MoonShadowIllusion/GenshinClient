# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UpgradeRoguelikeShikigamiRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UpgradeRoguelikeShikigamiRsp(betterproto.Message):
    """
    CmdId: 8966 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
    shikigami_group_id: int = betterproto.uint32_field(14)
    cur_level: int = betterproto.uint32_field(4)