# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerCurLevelRecordChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .TowerCurLevelRecord import *


@dataclass
class TowerCurLevelRecordChangeNotify(betterproto.Message):
    """
    CmdId: 2412 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cur_level_record: "TowerCurLevelRecord" = betterproto.message_field(10)
