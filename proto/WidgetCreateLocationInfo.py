# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WidgetCreateLocationInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class WidgetCreateLocationInfo(betterproto.Message):
    rot: "Vector" = betterproto.message_field(3)
    pos: "Vector" = betterproto.message_field(10)
