# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetEquipLockStateRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetEquipLockStateRsp(betterproto.Message):
    """
    CmdId: 668 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    target_equip_guid: int = betterproto.uint64_field(14)
    retcode: int = betterproto.int32_field(13)
    is_locked: bool = betterproto.bool_field(10)
