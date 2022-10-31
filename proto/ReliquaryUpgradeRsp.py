# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReliquaryUpgradeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ReliquaryUpgradeRsp(betterproto.Message):
    """
    CmdId: 693 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    old_level: int = betterproto.uint32_field(4)
    cur_level: int = betterproto.uint32_field(13)
    target_reliquary_guid: int = betterproto.uint64_field(9)
    cur_append_prop_list: List[int] = betterproto.uint32_field(2)
    power_up_rate: int = betterproto.uint32_field(6)
    old_append_prop_list: List[int] = betterproto.uint32_field(15)
    retcode: int = betterproto.int32_field(5)
