# {
#     "location_key": {
#         "intro": "intro text",
#         "actions": [
#             ("action text", "next_location_key", "post action text"),
#         ]
#     }
# }
#
# location_key = end -> is a special word that halts the game

import text

LOCATION = {
    "front_door": {
        "intro": text.FRONT_DOOR_INTRO,
        "actions": [
            ("Open the front door and enter the house.", "mud_room", text.FRONT_DOOR_OPEN),
            ("Call 911", "end", text.END_911),
        ]
    },
    "mud_room": {
        "intro": text.MUD_ROOM_INTRO,
        "actions": [
            ("Walk towards the shimmering light", "living_room", text.LIVING_ROOM_ENTER),
            ("Call 911", "end", text.END_911),
        ]
    },
    "living_room": {
        "intro": text.LIVING_ROOM_INTRO,
        "actions": [
            ("Call 911", "end", text.END_911),
        ]
    }
}
