# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SkyCrystalDetectorQuickUseResult.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_CCEOEOHLAPK import *


@dataclass
class SkyCrystalDetectorQuickUseResult(betterproto.Message):
    unk2700__c_o_i_e_l_i_g_e_a_c_l: "Unk2700_CCEOEOHLAPK" = betterproto.message_field(9)
    retcode: int = betterproto.int32_field(8)