# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReadMailNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ReadMailNotify(betterproto.Message):
    """
    CmdId: 1412 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    mail_id_list: List[int] = betterproto.uint32_field(2)
