# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_KIHEEAGDGIL_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_DPPCDPBBABA import *


@dataclass
class Unk2700_KIHEEAGDGIL_ServerNotify(betterproto.Message):
    """
    CmdId: 108 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    info: "Unk2700_DPPCDPBBABA" = betterproto.message_field(13)