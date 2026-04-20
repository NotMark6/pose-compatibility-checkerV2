import streamlit as st
from pose_validator import roles, act_tags, directions, check_act, DEFAULT_POSITION

# =========================
# POSITIONS (all safe with DEFAULT_POSITION)
# =========================
positions = {}


# Rodeo family (reverse cowgirl - A facing away)
base_rodeo = {**DEFAULT_POSITION,
    "hips_aligned": True,
    "A_can_reach_down": True,
    "B_can_reach_up": True,
    "A_facing_away": True,
    "face_access": False,
    "head_access_A_to_B": False,          # A cannot reach B's head/hair (facing away)
    "head_access_B_to_A": True,
    "neck_access_A_to_B": False,
    "neck_access_B_to_A": True,
    "chest_access": False,
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": True,           # B can easily spank A's butt
    "rear_swing_access_A_to_B": False,
    "rear_swing_access_B_to_A": True,     # needed for spanking from bottom
    "genital_access_A_to_B": True,
    "genital_access_B_to_A": True,
    "oral_alignment": False,
    "chest_alignment": False
}

positions["Rodeo"] = base_rodeo
positions["Lazy Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Lying Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Open Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Planted Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Squatting Open Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Squatting Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Standing Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Standing Twisted Rodeo"] = {**base_rodeo, "B_can_reach_up": False}
positions["Twisted Rodeo"] = {**base_rodeo, "B_can_reach_up": False}

# Missionary family
base_missionary = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": False,
    "faces_aligned": True, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": True,
    "neck_access_A_to_B": True, "neck_access_B_to_A": True,
    "head_access_A_to_B": True, "head_access_B_to_A": True,
    "face_access": True, "chest_access": True,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True
}
positions["Missionary"] = base_missionary
positions["Closed Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Folded Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Kneeling Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Mating Press"] = {**base_missionary, "B_can_reach_up": False}
positions["Mixed Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Open Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Oystered Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Split Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Tilted Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Tucked Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Tucked Missionary 180"] = {**base_missionary, "B_can_reach_up": False}
positions["Twisted Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Upright Missionary"] = {**base_missionary, "B_can_reach_up": False}
positions["Wrapped Missionary"] = {**base_missionary, "B_can_reach_up": False}

# Lotus family
base_lotus = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": False,
    "faces_aligned": True, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": True,
    "A_facing_away": False,
    "neck_access_A_to_B": True, "neck_access_B_to_A": True,
    "head_access_A_to_B": True, "head_access_B_to_A": True,
    "face_access": True, "chest_access": True,
    "butt_access_A_to_B": True, "butt_access_B_to_A": True,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True,
    "oral_alignment": False, "chest_alignment": False,
    "rear_entry_angle": False, "rear_swing_access_A_to_B": True, "rear_swing_access_B_to_A": False,
    "A_can_use_feet": False, "B_can_use_feet": False
}
positions["Lotus"] = base_lotus
positions["Blossoming (Utphallaka)"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}
positions["Crabby Lotus"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}
positions["Folded Lotus"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}
positions["Kneeling Lotus"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}
positions["Lazy Lotus"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}
positions["Mixed Lotus"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}
positions["Wrapped Lotus"] = {**base_lotus, "butt_access_A_to_B": False, "butt_access_B_to_A": True}

# Manual / Handjob family
base_manual = {**DEFAULT_POSITION,
    "faces_aligned": True, "hips_aligned": False,
    "A_can_reach_down": True, "B_can_reach_up": True,
    "A_facing_away": False,
    "neck_access_A_to_B": True, "neck_access_B_to_A": True,
    "head_access_A_to_B": True, "head_access_B_to_A": True,
    "face_access": True, "chest_access": False,
    "butt_access_A_to_B": False, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True
}
positions["Manual Base(Face-to-Face Seated Mutual)"] = base_manual
positions["Head-to-Toe Mutual"] = {**base_manual, "B_can_reach_up": False}
positions["Intercrural (Between Thighs)"] = base_manual.copy()
positions["Kneeling Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Kneeling Reach-Around"] = {**base_manual, "B_can_reach_up": False}
positions["Lap Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Lying Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Mutual Missionary (Hand)"] = {**base_manual, "B_can_reach_up": False}
positions["Over the Shoulder Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Reach Around (Standing)"] = {**base_manual, "B_can_reach_up": False}
positions["Side-by-Side Mutual Masturbation"] = {**base_manual, "B_can_reach_up": False}
positions["Sitting Reach-Around"] = {**base_manual, "B_can_reach_up": False}
positions["Spooning Reach-Around"] = {**base_manual, "B_can_reach_up": False}
positions["Standard Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Standing Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Straddling Handjob"] = {**base_manual, "B_can_reach_up": False}
positions["Titjob / Chest Stimulation"] = {**base_manual, "B_can_reach_up": False}

# Full Nelson family
base_fullnelson = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": False,
    "faces_aligned": False, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": False,
    "A_facing_away": False, "face_access": False,
    "neck_access_A_to_B": True, "neck_access_B_to_A": False,
    "head_access_A_to_B": True, "head_access_B_to_A": False,
    "chest_access": False,
    "butt_access_A_to_B": True, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": False
}
positions["Full Nelson"] = base_fullnelson
positions["Full Nelson (Knees)"] = {**base_fullnelson, "A_can_reach_down": True}
positions["Full Nelson (Knees, Arms & Head)"] = {**base_fullnelson, "A_can_reach_down": True}
positions["Full Nelson (Knees & Head)"] = {**base_fullnelson, "A_can_reach_down": True}
positions["Kneeling Full Nelson"] = {**base_fullnelson, "A_can_reach_down": True}
positions["Kneeling Full Nelson (Knees)"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Kneeling Full Nelson (Knees, Arms & Head)"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Kneeling Full Nelson (Knees & Head)"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Laying Back Full Nelson"] = {**base_fullnelson, "B_can_reach_up": True, "genital_access_B_to_A": True}
positions["Laying Back Full Nelson (Knees)"] = {**base_fullnelson, "B_can_reach_up": True, "genital_access_B_to_A": True}
positions["Laying Back Full Nelson (Knees, Arms & Head)"] = {**base_fullnelson, "B_can_reach_up": True, "genital_access_B_to_A": True}
positions["Laying Back Full Nelson (Knees & Head)"] = {**base_fullnelson, "B_can_reach_up": True, "genital_access_B_to_A": True}
positions["Sitting Full Nelson"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Sitting Full Nelson (Knees)"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Sitting Full Nelson (Knees, Arms & Head)"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Sitting Full Nelson (Knees & Head)"] = {**base_fullnelson, "B_can_reach_up": True}
positions["Suspended Full Nelson"] = {**base_fullnelson, "A_can_reach_down": False}
positions["Suspended Full Nelson (Knees)"] = {**base_fullnelson, "A_can_reach_down": False}
positions["Suspended Full Nelson (Knees, Arms & Head)"] = {**base_fullnelson, "A_can_reach_down": False}
positions["Suspended Full Nelson (Knees & Head)"] = {**base_fullnelson, "A_can_reach_down": False}

# Pile Driver family
base_piledriver = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": False,
    "faces_aligned": False, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": False,
    "A_facing_away": False, "face_access": False,
    "neck_access_A_to_B": False, "neck_access_B_to_A": False,
    "head_access_A_to_B": False, "head_access_B_to_A": False,
    "chest_access": False,
    "butt_access_A_to_B": True, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": False
}
positions["Pile Driver"] = base_piledriver
positions["Grounded Pile Driver"] = {**base_piledriver, "A_can_reach_down": True}
positions["Pile Driver 180"] = {**base_piledriver, "genital_access_A_to_B": True}
positions["Squatting Pile Driver"] = {**base_piledriver, "A_can_reach_down": False}
positions["Squatting Pile Driver 180"] = {**base_piledriver, "A_can_reach_down": False}
positions["Twisted Pile Driver"] = {**base_piledriver, "hips_aligned": False}

# Saint family
base_saint = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": True,
    "faces_aligned": True, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": True,
    "A_facing_away": False, "face_access": True,
    "neck_access_A_to_B": True, "neck_access_B_to_A": True,
    "head_access_A_to_B": True, "head_access_B_to_A": True,
    "chest_access": True,
    "butt_access_A_to_B": False, "butt_access_B_to_A": True,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True
}
positions["Saint"] = base_saint
positions["Crabby Saint"] = {**base_saint, "A_can_reach_down": False, "B_can_reach_up": False}
positions["Folded Saint"] = {**base_saint, "A_can_reach_down": False, "B_can_reach_up": False}
positions["Kneeling Saint"] = {**base_saint, "A_can_reach_down": False, "B_can_reach_up": False}
positions["Kneeling Saint 180"] = {**base_saint, "A_can_reach_down": False, "B_can_reach_up": False}
positions["Lazy Saint"] = {**base_saint, "A_can_reach_down": False, "B_can_reach_up": False}
positions["Mixed Saint"] = {**base_saint, "A_can_reach_down": False, "B_can_reach_up": False}
positions["Saint 180"] = {**base_saint, "faces_aligned": False}
positions["Wrapped Saint"] = {**base_saint, "A_can_reach_down": True}

# Scissors family
base_scissors = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": True,
    "faces_aligned": True, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": True,
    "A_facing_away": False, "face_access": True,
    "neck_access_A_to_B": True, "neck_access_B_to_A": True,
    "head_access_A_to_B": True, "head_access_B_to_A": True,
    "chest_access": True,
    "butt_access_A_to_B": False, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True
}
positions["Scissors"] = base_scissors
positions["Classic Tribbing"] = {**base_scissors, "face_access": True}
positions["Crabby Scissors"] = {**base_scissors, "face_access": True}
positions["Kneeling Scissors"] = {**base_scissors, "face_access": True}
positions["Missionary Scissors"] = {**base_scissors, "face_access": True}
positions["Scissored Flagpole"] = {**base_scissors, "face_access": True}
positions["Sitting Scissors"] = {**base_scissors, "face_access": True}
positions["Twisted Kneeling Scissors"] = {**base_scissors, "B_can_reach_up": False}
positions["Upright Scissor"] = {**base_scissors, "B_can_reach_up": False}
positions["Wrapped Scissors"] = {**base_scissors, "B_can_reach_up": False}

# Sinner family
base_sinner = {**DEFAULT_POSITION,
    "actor_can_thrust_A": True, "actor_can_thrust_B": False,
    "faces_aligned": True, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": False,
    "A_facing_away": False, "face_access": True,
    "neck_access_A_to_B": True, "neck_access_B_to_A": False,
    "head_access_A_to_B": True, "head_access_B_to_A": False,
    "chest_access": True,
    "butt_access_A_to_B": False, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True
}
positions["Sinner"] = base_sinner
positions["Closed Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Folded Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Kneeling Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Planted Closed Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Planted Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Pressed Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Split Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Tilted Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Tucked Sinner"] = {**base_sinner, "B_can_reach_up": False}
positions["Wrapped Sinner"] = {**base_sinner, "hips_aligned": True, "B_can_reach_up": True}

# Spoon family
base_spoon = {**DEFAULT_POSITION,
    "faces_aligned": False, "hips_aligned": True,
    "A_can_reach_down": False, "B_can_reach_up": True,
    "A_facing_away": True, "face_access": False,
    "neck_access_A_to_B": False, "neck_access_B_to_A": True,
    "head_access_A_to_B": False, "head_access_B_to_A": True,
    "chest_access": False,
    "butt_access_A_to_B": False, "butt_access_B_to_A": True,
    "genital_access_A_to_B": False, "genital_access_B_to_A": True
}
positions["Spoon"] = base_spoon
positions["Bent Spoon"] = {**base_spoon, "genital_access_B_to_A": True}
positions["Bipolar Spoon"] = {**base_spoon, "genital_access_B_to_A": True}
positions["Box Position (Parshva Samputa)"] = {**base_spoon, "chest_access": True}
positions["Crossed Spoon"] = {**base_spoon, "genital_access_B_to_A": True}
positions["Wrapped Spoon"] = {**base_spoon, "hips_aligned": False}

# Shotgun family
base_shotgun = {**DEFAULT_POSITION,
    "faces_aligned": False, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": True,
    "A_facing_away": False, "face_access": False,
    "neck_access_A_to_B": False, "neck_access_B_to_A": False,
    "head_access_A_to_B": False, "head_access_B_to_A": False,
    "chest_access": False,
    "butt_access_A_to_B": False, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": True
}
positions["Shotgun Base"] = base_shotgun
positions["Shotgun Doggy"] = {**base_shotgun, "A_facing_away": True, "butt_access_A_to_B": True, "butt_access_B_to_A": False, "genital_access_A_to_B": True, "genital_access_B_to_A": False}
positions["Shotgun Open Missionary"] = {**base_shotgun, "faces_aligned": True, "neck_access_A_to_B": True, "neck_access_B_to_A": True, "head_access_A_to_B": True, "head_access_B_to_A": True, "chest_access": True}
positions["Shotgun Rodeo"] = {**base_shotgun, "A_facing_away": True, "A_can_reach_down": False, "face_access": False, "butt_access_A_to_B": False, "butt_access_B_to_A": True, "genital_access_B_to_A": True}
positions["Shotgun Road Head"] = {**base_shotgun, "genital_access_B_to_A": True, "butt_access_B_to_A": True, "A_can_reach_down": False}
positions["Shotgun Open Lap Dance"] = {**base_shotgun, "butt_access_B_to_A": True}
positions["Shotgun Sinner"] = {**base_shotgun, "faces_aligned": True, "B_can_reach_up": False}
positions["Shotgun Tucked Groundhog"] = {**base_shotgun, "B_can_reach_up": False, "A_can_reach_down": False}
positions["Shotgun Servant"] = {**base_shotgun, "A_can_reach_down": False, "B_can_reach_up": True}
positions["Shotgun Collapsed Cowgirl"] = {**base_shotgun, "A_can_reach_down": False}
positions["Shotgun Open Butterfly"] = {**base_shotgun, "chest_access": True}

# Wheelbarrow family
base_wheelbarrow = {**DEFAULT_POSITION,
    "has_free_hand": False,
    "actor_can_thrust_A": True, "actor_can_thrust_B": False,
    "faces_aligned": False, "hips_aligned": True,
    "A_can_reach_down": True, "B_can_reach_up": False,
    "A_facing_away": True, "face_access": False,
    "neck_access_A_to_B": False, "neck_access_B_to_A": False,
    "head_access_A_to_B": False, "head_access_B_to_A": False,
    "chest_access": False,
    "butt_access_A_to_B": True, "butt_access_B_to_A": False,
    "genital_access_A_to_B": True, "genital_access_B_to_A": False,
    "rear_entry_angle": True, "rear_swing_access_A_to_B": True
}
positions["Wheelbarrow"] = base_wheelbarrow
positions["Kneeling Wheelbarrow"] = {**base_wheelbarrow, "A_can_reach_down": True}
positions["Sitting Wheelbarrow"] = {**base_wheelbarrow, "B_can_reach_up": False}
positions["Supported Wheelbarrow"] = {**base_wheelbarrow, "B_can_reach_up": False}
positions["Supported Kneeling Wheelbarrow"] = {**base_wheelbarrow, "A_can_reach_down": True, "B_can_reach_up": False}

# Driver's family
positions["Driver's Open Lap Dance"] = {**DEFAULT_POSITION,
    "faces_aligned": False, "hips_aligned": True,
    "A_can_reach_down": False, "B_can_reach_up": True,
    "A_facing_away": False, "face_access": False,
    "neck_access_A_to_B": False, "neck_access_B_to_A": True,
    "head_access_A_to_B": False, "head_access_B_to_A": True,
    "chest_access": False,
    "butt_access_A_to_B": False, "butt_access_B_to_A": True,
    "genital_access_A_to_B": False, "genital_access_B_to_A": True
}
positions["Driver's Road Head"] = {**positions["Driver's Open Lap Dance"], "genital_access_B_to_A": True}

# =========================
# UI
# =========================
st.title("Pose Compatibility Checker")

role_A = st.selectbox("Role A", list(roles.keys()))
role_B = st.selectbox("Role B", list(roles.keys()))
pose = st.selectbox("Position", list(positions.keys()))

if st.button("Generate"):
    current_position = positions[pose]          # ← this is the correct safe way
    A = roles[role_A]
    B = roles[role_B]

    st.subheader(f"{role_A} (A) + {role_B} (B)")

    for act in act_tags:
        for direction in directions:
            result, reason = check_act(A, B, act, direction, current_position)
            if result:
                st.write(f"**({direction.replace('->','→')}) {act}** — {reason}")