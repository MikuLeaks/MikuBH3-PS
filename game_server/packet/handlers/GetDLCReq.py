import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetDLCReq,
    GetDLCRsp,
    DLCSupportNPC
)

async def handle(session: Session, msg: GetDLCReq) -> betterproto.Message:
    return GetDLCRsp(
        retcode=0,
        exp=5300,
        finished_dialog_id_list=[
            310145,
            310151,
            310207,
            310237,
            310240,
            310250,
            310523,
            310724,
            320206,
            320224,
            350510,
            350515,
            350526,
            360607,
            500010006,
            500010020,
            500010037,
            500010068,
            500010069,
            500010079,
            500020008,
            500020014,
            500050003,
            500060005,
            500060014,
            500060039,
            500070016,
            500070021,
            500070040,
            500080006,
            500090006,
            500090015,
            500100043,
            500110024,
            500110039,
            500110045,
            500120012,
            500120021,
            500120036,
            500130003,
            500130016,
            500140003,
            500140017,
            500140029,
            500150007,
            500200003,
            500200036,
            500200054,
            500210005,
            500210009,
            510010006,
            510010014,
            510010019,
            510050010,
            510080005,
            510080025,
            510090006,
            510100004,
            510100022,
            510110007,
            510120008,
            510120013
        ],
        has_take_reward_level=30,
        level=30,
        name="ley",
        support_npc_list=[
            DLCSupportNPC(
                npc_id=1,
                support_level=3
            ),
            DLCSupportNPC(
                npc_id=2,
                support_level=2,
                support_point=75
            ),
            DLCSupportNPC(
                npc_id=3,
                support_level=3
            ),
            DLCSupportNPC(
                npc_id=4,
                support_level=3
            ),
            DLCSupportNPC(
                npc_id=5,
                support_level=1,
                support_point=2
            )
        ]
    )