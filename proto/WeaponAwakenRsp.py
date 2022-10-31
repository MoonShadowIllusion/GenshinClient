# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WeaponAwakenRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class WeaponAwakenRsp(betterproto.Message):
    """
    CmdId: 606 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(9)
    avatar_guid: int = betterproto.uint64_field(10)
    old_affix_level_map: Dict[int, int] = betterproto.map_field(
        4, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    target_weapon_awaken_level: int = betterproto.uint32_field(2)
    target_weapon_guid: int = betterproto.uint64_field(15)
    cur_affix_level_map: Dict[int, int] = betterproto.map_field(
        11, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
