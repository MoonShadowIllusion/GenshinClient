# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MailItem.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .EquipParam import *
from .MaterialDeleteInfo import *


@dataclass
class MailItem(betterproto.Message):
    equip_param: "EquipParam" = betterproto.message_field(1)
    delete_info: "MaterialDeleteInfo" = betterproto.message_field(2)
