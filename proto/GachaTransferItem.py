# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GachaTransferItem.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ItemParam import *


@dataclass
class GachaTransferItem(betterproto.Message):
    item: "ItemParam" = betterproto.message_field(3)
    is_transfer_item_new: bool = betterproto.bool_field(1)
