# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GachaInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .GachaUpInfo import *


@dataclass
class GachaInfo(betterproto.Message):
    gacha_type: int = betterproto.uint32_field(13)
    schedule_id: int = betterproto.uint32_field(10)
    begin_time: int = betterproto.uint32_field(1)
    end_time: int = betterproto.uint32_field(14)
    cost_item_id: int = betterproto.uint32_field(9)
    cost_item_num: int = betterproto.uint32_field(3)
    gacha_prefab_path: str = betterproto.string_field(15)
    gacha_prob_url: str = betterproto.string_field(8)
    gacha_record_url: str = betterproto.string_field(12)
    gacha_preview_prefab_path: str = betterproto.string_field(4)
    ten_cost_item_id: int = betterproto.uint32_field(2)
    ten_cost_item_num: int = betterproto.uint32_field(6)
    left_gacha_times: int = betterproto.uint32_field(5)
    gacha_times_limit: int = betterproto.uint32_field(11)
    gacha_sort_id: int = betterproto.uint32_field(7)
    gacha_prob_url_oversea: str = betterproto.string_field(1481)
    gacha_record_url_oversea: str = betterproto.string_field(1854)
    gacha_up_info_list: List["GachaUpInfo"] = betterproto.message_field(1233)
    title_textmap: str = betterproto.string_field(736)
    display_up5_item_list: List[int] = betterproto.uint32_field(2006)
    display_up4_item_list: List[int] = betterproto.uint32_field(1875)
    wish_item_id: int = betterproto.uint32_field(1637)
    wish_progress: int = betterproto.uint32_field(1819)
    wish_max_progress: int = betterproto.uint32_field(1222)
    is_new_wish: bool = betterproto.bool_field(733)