# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerCookRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .CookRecipeData import *
from .ItemParam import *


@dataclass
class PlayerCookRsp(betterproto.Message):
    """
    CmdId: 188 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    extral_item_list: List["ItemParam"] = betterproto.message_field(15)
    cook_count: int = betterproto.uint32_field(12)
    item_list: List["ItemParam"] = betterproto.message_field(11)
    retcode: int = betterproto.int32_field(3)
    qte_quality: int = betterproto.uint32_field(5)
    recipe_data: "CookRecipeData" = betterproto.message_field(7)
