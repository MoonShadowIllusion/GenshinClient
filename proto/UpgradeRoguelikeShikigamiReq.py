# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UpgradeRoguelikeShikigamiReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UpgradeRoguelikeShikigamiReq(betterproto.Message):
    """
    CmdId: 8151 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    upgrade_level: int = betterproto.uint32_field(6)
    shikigami_group_id: int = betterproto.uint32_field(15)
