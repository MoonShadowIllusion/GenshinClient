# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_FPJLFMEHHLB_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_DPPCDPBBABA import *


@dataclass
class Unk2700_FPJLFMEHHLB_ServerNotify(betterproto.Message):
    """
    CmdId: 4060 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    info: "Unk2700_DPPCDPBBABA" = betterproto.message_field(14)
