# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UpdatePlayerShowAvatarListRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class UpdatePlayerShowAvatarListRsp(betterproto.Message):
    """
    CmdId: 4058 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    show_avatar_id_list: List[int] = betterproto.uint32_field(1)
    is_show_avatar: bool = betterproto.bool_field(3)
    retcode: int = betterproto.int32_field(10)
