# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerFloorRecordChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .TowerFloorRecord import *


@dataclass
class TowerFloorRecordChangeNotify(betterproto.Message):
    """
    CmdId: 2498 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_finished_entrance_floor: bool = betterproto.bool_field(11)
    tower_floor_record_list: List["TowerFloorRecord"] = betterproto.message_field(8)
