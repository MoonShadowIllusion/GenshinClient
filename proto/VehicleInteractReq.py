# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: VehicleInteractReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .VehicleInteractType import *


@dataclass
class VehicleInteractReq(betterproto.Message):
    """
    CmdId: 865 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    interact_type: "VehicleInteractType" = betterproto.enum_field(8)
    pos: int = betterproto.uint32_field(12)
    entity_id: int = betterproto.uint32_field(15)
