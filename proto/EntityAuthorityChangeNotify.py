# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EntityAuthorityChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .AuthorityChange import *


@dataclass
class EntityAuthorityChangeNotify(betterproto.Message):
    """
    CmdId: 394 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    authority_change_list: List["AuthorityChange"] = betterproto.message_field(15)
