# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WeaponPromoteRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class WeaponPromoteRsp(betterproto.Message):
    """
    CmdId: 665 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_weapon_guid: int = betterproto.uint64_field(3)
    old_promote_level: int = betterproto.uint32_field(7)
    cur_promote_level: int = betterproto.uint32_field(12)
    retcode: int = betterproto.int32_field(4)
