# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: VehicleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .VehicleMember import *


@dataclass
class VehicleInfo(betterproto.Message):
    member_list: List["VehicleMember"] = betterproto.message_field(1)
    owner_uid: int = betterproto.uint32_field(2)
    cur_stamina: float = betterproto.float_field(3)
