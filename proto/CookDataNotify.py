# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CookDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .CookRecipeData import *


@dataclass
class CookDataNotify(betterproto.Message):
    """
    CmdId: 195 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    recipe_data_list: List["CookRecipeData"] = betterproto.message_field(2)
    grade: int = betterproto.uint32_field(11)
