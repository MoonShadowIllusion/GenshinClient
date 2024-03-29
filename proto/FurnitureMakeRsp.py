# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FurnitureMakeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .FurnitureMakeBeHelpedData import *
from .FurnitureMakeHelpData import *
from .FurnitureMakeMakeInfo import *
from .FurnitureMakeSlot import *


@dataclass
class FurnitureMakeRsp(betterproto.Message):
    """
    CmdId: 4782 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    helped_data_list: List["FurnitureMakeBeHelpedData"] = betterproto.message_field(13)
    make_info_list: List["FurnitureMakeMakeInfo"] = betterproto.message_field(4)
    furniture_make_slot: "FurnitureMakeSlot" = betterproto.message_field(1)
    retcode: int = betterproto.int32_field(3)
    help_data_list: List["FurnitureMakeHelpData"] = betterproto.message_field(2)
