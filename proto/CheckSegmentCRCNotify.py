# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CheckSegmentCRCNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .SegmentInfo import *


@dataclass
class CheckSegmentCRCNotify(betterproto.Message):
    """CmdId: 39 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true"""

    info_list: List["SegmentInfo"] = betterproto.message_field(6)
