# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivityShopSheetInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ActivityShopSheetInfo(betterproto.Message):
    end_time: int = betterproto.uint32_field(1)
    begin_time: int = betterproto.uint32_field(12)
    sheet_id: int = betterproto.uint32_field(2)