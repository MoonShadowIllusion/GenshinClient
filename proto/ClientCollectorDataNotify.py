# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientCollectorDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ClientCollectorData import *


@dataclass
class ClientCollectorDataNotify(betterproto.Message):
    """
    CmdId: 4264 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    client_collector_data_list: List["ClientCollectorData"] = betterproto.message_field(
        13
    )