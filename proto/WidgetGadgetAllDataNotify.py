# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WidgetGadgetAllDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .WidgetGadgetData import *


@dataclass
class WidgetGadgetAllDataNotify(betterproto.Message):
    """
    CmdId: 4284 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    widget_gadget_data: List["WidgetGadgetData"] = betterproto.message_field(13)
