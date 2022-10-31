# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RegionSearchNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .RegionSearchInfo import *


@dataclass
class RegionSearchNotify(betterproto.Message):
    """
    CmdId: 5626 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    region_search_list: List["RegionSearchInfo"] = betterproto.message_field(1)
    uid: int = betterproto.uint32_field(8)