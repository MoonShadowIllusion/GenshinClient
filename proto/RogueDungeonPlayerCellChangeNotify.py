# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RogueDungeonPlayerCellChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RogueDungeonPlayerCellChangeNotify(betterproto.Message):
    """
    CmdId: 8347 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    old_cell_id: int = betterproto.uint32_field(10)
    cell_id: int = betterproto.uint32_field(7)
