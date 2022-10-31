# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AddNoGachaAvatarCardNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AddNoGachaAvatarCardTransferItem import *


@dataclass
class AddNoGachaAvatarCardNotify(betterproto.Message):
    """
    CmdId: 1655 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    transfer_item_list: List[
        "AddNoGachaAvatarCardTransferItem"
    ] = betterproto.message_field(4)
    initial_promote_level: int = betterproto.uint32_field(2)
    avatar_id: int = betterproto.uint32_field(8)
    is_transfer_to_item: bool = betterproto.bool_field(6)
    reason: int = betterproto.uint32_field(9)
    initial_level: int = betterproto.uint32_field(10)
    item_id: int = betterproto.uint32_field(14)