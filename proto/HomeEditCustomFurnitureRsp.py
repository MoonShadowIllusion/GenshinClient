# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeEditCustomFurnitureRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomeCustomFurnitureInfo import *


@dataclass
class HomeEditCustomFurnitureRsp(betterproto.Message):
    """
    CmdId: 4496 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    custom_furniture_info: "HomeCustomFurnitureInfo" = betterproto.message_field(11)
    retcode: int = betterproto.int32_field(14)
