# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MaterialDeleteInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class MaterialDeleteInfo(betterproto.Message):
    has_delete_config: bool = betterproto.bool_field(1)
    count_down_delete: "MaterialDeleteInfoCountDownDelete" = betterproto.message_field(
        2, group="delete_info"
    )
    date_delete: "MaterialDeleteInfoDateTimeDelete" = betterproto.message_field(
        3, group="delete_info"
    )
    delay_week_count_down_delete: "MaterialDeleteInfoDelayWeekCountDownDelete" = (
        betterproto.message_field(4, group="delete_info")
    )


@dataclass
class MaterialDeleteInfoCountDownDelete(betterproto.Message):
    delete_time_num_map: Dict[int, int] = betterproto.map_field(
        1, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    config_count_down_time: int = betterproto.uint32_field(2)


@dataclass
class MaterialDeleteInfoDateTimeDelete(betterproto.Message):
    delete_time: int = betterproto.uint32_field(1)


@dataclass
class MaterialDeleteInfoDelayWeekCountDownDelete(betterproto.Message):
    delete_time_num_map: Dict[int, int] = betterproto.map_field(
        1, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    config_delay_week: int = betterproto.uint32_field(2)
    config_count_down_time: int = betterproto.uint32_field(3)