# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TrialAvatarGrantRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class TrialAvatarGrantRecordGrantReason(betterproto.Enum):
    GRANT_REASON_INVALID = 0
    GRANT_REASON_BY_QUEST = 1
    GRANT_REASON_BY_TRIAL_AVATAR_ACTIVITY = 2
    GRANT_REASON_BY_DUNGEON_ELEMENT_CHALLENGE = 3
    GRANT_REASON_BY_MIST_TRIAL_ACTIVITY = 4
    GRANT_REASON_BY_SUMO_ACTIVITY = 5
    GRANT_REASON_Unk2700_ELPMDIEIOHP = 6
    GRANT_REASON_Unk2700_FALPDBLGHJB = 7
    GRANT_REASON_Unk2700_GAMADMGGMBC = 8
    GRANT_REASON_Unk2800_FIIDJHAKMOI = 9
    GRANT_REASON_Unk3000_ANPCNHCADHG = 10
    GRANT_REASON_Unk3000_AJIFFOLFKLO = 11


@dataclass
class TrialAvatarGrantRecord(betterproto.Message):
    grant_reason: int = betterproto.uint32_field(1)
    from_parent_quest_id: int = betterproto.uint32_field(2)
