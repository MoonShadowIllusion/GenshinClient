# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerOfferingDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .PlayerOfferingData import *


@dataclass
class PlayerOfferingDataNotify(betterproto.Message):
    """
    CmdId: 2923 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    offering_data_list: List["PlayerOfferingData"] = betterproto.message_field(2)
