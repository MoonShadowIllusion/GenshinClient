# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AllWidgetDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AnchorPointData import *
from .ClientCollectorData import *
from .LunchBoxData import *
from .OneofGatherPointDetectorData import *
from .Unk2700_CCEOEOHLAPK import *
from .WidgetCoolDownData import *
from .WidgetSlotData import *


@dataclass
class AllWidgetDataNotify(betterproto.Message):
    """
    CmdId: 4271 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__c_n_n_f_g_f_b_b_b_f_p: List[int] = betterproto.uint32_field(11)
    lunch_box_data: "LunchBoxData" = betterproto.message_field(1)
    cool_down_group_data_list: List["WidgetCoolDownData"] = betterproto.message_field(
        13
    )
    anchor_point_list: List["AnchorPointData"] = betterproto.message_field(3)
    slot_list: List["WidgetSlotData"] = betterproto.message_field(6)
    next_anchor_point_usable_time: int = betterproto.uint32_field(10)
    client_collector_data_list: List["ClientCollectorData"] = betterproto.message_field(
        4
    )
    oneof_gather_point_detector_data_list: List[
        "OneofGatherPointDetectorData"
    ] = betterproto.message_field(15)
    normal_cool_down_data_list: List["WidgetCoolDownData"] = betterproto.message_field(
        9
    )
    unk2700__c_o_i_e_l_i_g_e_a_c_l: "Unk2700_CCEOEOHLAPK" = betterproto.message_field(
        12
    )
