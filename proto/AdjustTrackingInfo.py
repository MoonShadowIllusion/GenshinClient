# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AdjustTrackingInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AdjustTrackingInfo(betterproto.Message):
    event_token: str = betterproto.string_field(9)
    adid: str = betterproto.string_field(4)
    idfa: str = betterproto.string_field(2)
    app_token: str = betterproto.string_field(14)
    gps_adid: str = betterproto.string_field(3)
    fire_adid: str = betterproto.string_field(13)
