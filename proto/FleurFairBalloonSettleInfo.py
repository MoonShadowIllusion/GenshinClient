# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FleurFairBalloonSettleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .BalloonSettleInfo import *


@dataclass
class FleurFairBalloonSettleInfo(betterproto.Message):
    settle_info: "BalloonSettleInfo" = betterproto.message_field(10)
    is_new_record: bool = betterproto.bool_field(7)
