# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_IMHNKDHHGMA.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_JCOIDFNDHPB import *


@dataclass
class Unk2700_IMHNKDHHGMA(betterproto.Message):
    """
    CmdId: 8186 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gallery_id: int = betterproto.uint32_field(10)
    settle_info: "Unk2700_JCOIDFNDHPB" = betterproto.message_field(13)
