# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SaveCoopDialogRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SaveCoopDialogRsp(betterproto.Message):
    """
    CmdId: 1962 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    dialog_id: int = betterproto.uint32_field(8)
    main_coop_id: int = betterproto.uint32_field(10)
    retcode: int = betterproto.int32_field(7)