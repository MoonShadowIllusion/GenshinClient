# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RefreshBackgroundAvatarRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class RefreshBackgroundAvatarRsp(betterproto.Message):
    """
    CmdId: 1800 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    hp_full_time_map: Dict[int, int] = betterproto.map_field(
        15, betterproto.TYPE_UINT64, betterproto.TYPE_UINT32
    )
    retcode: int = betterproto.int32_field(3)
