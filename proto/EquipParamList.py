# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EquipParamList.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .EquipParam import *


@dataclass
class EquipParamList(betterproto.Message):
    item_list: List["EquipParam"] = betterproto.message_field(1)
