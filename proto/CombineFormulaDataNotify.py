# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CombineFormulaDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CombineFormulaDataNotify(betterproto.Message):
    """
    CmdId: 632 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    combine_id: int = betterproto.uint32_field(6)
    is_locked: bool = betterproto.bool_field(3)
