# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayerSoundNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


class ScenePlayerSoundNotifyPlaySoundType(betterproto.Enum):
    PLAY_SOUND_TYPE_NONE = 0
    PLAY_SOUND_TYPE_START = 1
    PLAY_SOUND_TYPE_STOP = 2


@dataclass
class ScenePlayerSoundNotify(betterproto.Message):
    """
    CmdId: 233 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    sound_name: str = betterproto.string_field(4)
    play_type: "ScenePlayerSoundNotifyPlaySoundType" = betterproto.enum_field(8)
    play_pos: "Vector" = betterproto.message_field(3)
