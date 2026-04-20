import os
from typing import Dict, List, Tuple

# =========================
# ROLE DEFINITIONS
# =========================
roles: Dict[str, Dict[str, object]] = {
    "Cis Female": {"penis": False, "vagina": True, "breasts": True, "hair": True, "flexibility": 1.0, "reach": 1.0},
    "Cis Female (Athletic)": {"penis": False, "vagina": True, "breasts": True, "hair": True, "flexibility": 1.3, "reach": 1.1},
    "Cis Female (Curvy)": {"penis": False, "vagina": True, "breasts": True, "hair": True, "flexibility": 0.8, "reach": 0.9},
    "Cis Female (Petite)": {"penis": False, "vagina": True, "breasts": True, "hair": True, "flexibility": 1.1, "reach": 0.8},
    "Cis Male": {"penis": True, "vagina": False, "breasts": False, "hair": False, "flexibility": 1.0, "reach": 1.0},
    "Cis Male (Large penis size)": {"penis": True, "vagina": False, "breasts": False, "hair": False, "flexibility": 0.9, "reach": 1.0},
    "Cis Male (Small penis size)": {"penis": True, "vagina": False, "breasts": False, "hair": False, "flexibility": 1.1, "reach": 1.0},
    "Eunuch": {"penis": False, "vagina": False, "breasts": False, "hair": False, "flexibility": 1.0, "reach": 1.0},
    "Futanari": {"penis": True, "vagina": True, "breasts": True, "hair": True, "flexibility": 1.0, "reach": 1.0},
    "Mastectomy Survivor": {"penis": False, "vagina": True, "breasts": False, "hair": True, "flexibility": 1.0, "reach": 1.0},
    "Trans Man (Pre-op)": {"penis": False, "vagina": True, "breasts": True, "hair": True, "flexibility": 1.0, "reach": 1.0},
    "Trans Woman (Pre-op)": {"penis": True, "vagina": False, "breasts": True, "hair": True, "flexibility": 1.0, "reach": 1.0},
}

# =========================
# DEFAULT POSITION TEMPLATE
# =========================
DEFAULT_POSITION: Dict[str, bool] = {
    "has_free_hand": True,
    "faces_aligned": False,
    "hips_aligned": True,
    "A_can_reach_down": True,
    "B_can_reach_up": True,
    "A_facing_away": False,
    "neck_access_A_to_B": False,
    "neck_access_B_to_A": False,
    "head_access_A_to_B": False,
    "head_access_B_to_A": False,
    "face_access": False,
    "chest_access": False,
    "genital_access_A_to_B": False,
    "genital_access_B_to_A": False,
    "butt_access_A_to_B": False,
    "butt_access_B_to_A": False,
    "rear_entry_angle": False,
    "rear_swing_access_A_to_B": False,
    "rear_swing_access_B_to_A": False,
    "oral_alignment": False,
    "chest_alignment": False,
    "A_can_use_feet": False,
    "B_can_use_feet": False,
    "actor_can_thrust_A": False,
    "actor_can_thrust_B": False,
    "bottom_can_perform_oral_chest": False,   # ← realism flag for all face-to-face poses
}

# =========================
# ACTION TAGS
# =========================
act_tags: Dict[str, List[str]] = {
    "Scratching": ["needs_reach"],
    "Vaginal Penetration": ["needs_penis", "needs_vagina", "needs_actor_control"],
    "Anal Penetration": ["needs_penis", "needs_actor_control"],
    "Fellatio": ["needs_penis", "needs_face", "needs_oral_alignment"],
    "Deep Throat": ["needs_penis", "needs_face", "needs_oral_alignment"],
    "Cunnilingus": ["needs_vagina", "needs_face", "needs_oral_alignment"],
    "Analingus": ["needs_face", "needs_oral_alignment"],
    "Kissing": ["needs_face"],
    "Neck Kissing": ["needs_face", "needs_neck_access"],
    "Nipple Stimulation (Oral)": ["needs_breasts", "needs_face"],
    "Breast Sucking": ["needs_breasts", "needs_face"],
    "Titjob": ["actor_needs_breasts", "target_needs_penis", "needs_chest_alignment"],
    "Handjob": ["needs_hand", "needs_genital_access", "target_needs_penis", "needs_free_hand"],
    "Vaginal Fingering": ["needs_hand", "needs_genital_access", "needs_free_hand"],
    "Anal Fingering": ["needs_hand", "needs_butt_access", "needs_rear_entry"],
    "Breast Stimulation (Manual)": ["needs_hand", "needs_chest_access", "needs_free_hand"],
    "Nipple Stimulation (Manual)": ["needs_hand", "needs_chest_access", "needs_free_hand"],
    "Choking": ["needs_reach", "needs_neck_access"],
    "Hair Pulling": ["needs_hand", "needs_head_access"],
    "Spanking": ["needs_hand", "needs_butt_access", "needs_rear_swing"],
    "Biting": ["needs_face"],
    "Footjob": ["needs_penis", "target_needs_penis", "needs_feet"],
}

directions = ["A->B", "B->A"]


# =========================
# HELPERS
# =========================
def get_actor_target(A, B, direction):
    return (A, B) if direction == "A->B" else (B, A)

def role_labels(direction):
    return ("Role A", "Role B") if direction == "A->B" else ("Role B", "Role A")


# =========================
# CHECK FUNCTION (now consistent across ALL poses)
# =========================
def check_act(A, B, act_name, direction, current_position):
    actor, target = get_actor_target(A, B, direction)
    actor_label, target_label = role_labels(direction)
    tags = act_tags.get(act_name, [])

    # 1. ANATOMY
    if "needs_penis" in tags and not actor.get("penis", False):
        return False, f"{actor_label} has no penis"
    if "needs_vagina" in tags and not target.get("vagina", False):
        return False, f"{target_label} has no vagina"
    if "needs_breasts" in tags and not target.get("breasts", False):
        return False, f"{target_label} has no breasts"
    if "actor_needs_breasts" in tags and not actor.get("breasts", False):
        return False, f"{actor_label} has no breasts"
    if "target_needs_penis" in tags and not target.get("penis", False):
        return False, f"{target_label} has no penis"

    # 2. POSITION CHECKS
    if "needs_face" in tags and not current_position.get("face_access", False):
        return False, "No face access in this position"
    if "needs_oral_alignment" in tags and not current_position.get("oral_alignment", False):
        return False, f"{actor_label} cannot perform this action due to body orientation"
    if "needs_chest_alignment" in tags and not current_position.get("chest_alignment", False):
        return False, f"{actor_label} cannot perform this action due to body alignment"
    if "needs_rear_entry" in tags and not current_position.get("rear_entry_angle", False):
        return False, f"{actor_label} cannot perform this action due to positioning angle"
    if "needs_rear_swing" in tags:
        key = f"rear_swing_access_{'A_to_B' if direction == 'A->B' else 'B_to_A'}"
        if not current_position.get(key, False):
            return False, f"{actor_label} cannot perform this action due to movement restriction"

    # 3. REALISM: Oral chest actions (Nipple Stimulation (Oral) + Breast Sucking)
    if act_name in ["Nipple Stimulation (Oral)", "Breast Sucking"]:
        if direction == "B->A" and current_position.get("faces_aligned", False):
            if not current_position.get("bottom_can_perform_oral_chest", False):
                return False, f"{actor_label} cannot realistically reach {target_label.lower()}'s chest from the bottom in this pose"

    # 4. REACH / HAND / FEET
    if ("needs_hand" in tags or "needs_free_hand" in tags):
        if direction == "A->B" and not current_position.get("A_can_reach_down", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}"
        if direction == "B->A" and not current_position.get("B_can_reach_up", False):
            return False, f"{actor_label} cannot reach {target_label.lower()}"
    if "needs_feet" in tags:
        if direction == "A->B" and not current_position.get("A_can_use_feet", False):
            return False, f"{actor_label} cannot use feet in this position"
        if direction == "B->A" and not current_position.get("B_can_use_feet", False):
            return False, f"{actor_label} cannot use feet in this position"

    # 5. CONTROL
    if "needs_actor_control" in tags:
        key = f"actor_can_thrust_{direction[0]}"
        if not current_position.get(key, False):
            return False, f"{actor_label} cannot control movement in this position"

    # 6. SUCCESS
    reason_map = {
        "Vaginal Penetration": f"{actor_label} has a penis and can reach {target_label.lower()}'s vagina",
        "Anal Penetration": f"{actor_label} has a penis and can reach {target_label.lower()}'s anus",
        "Vaginal Fingering": f"{actor_label} can reach to finger {target_label.lower()}'s vagina",
        "Anal Fingering": f"{actor_label} can reach {target_label.lower()}'s anus",
        "Breast Stimulation (Manual)": f"{actor_label} can reach {target_label.lower()}'s breasts",
        "Nipple Stimulation (Manual)": f"{actor_label} can reach {target_label.lower()}'s nipples",
        "Hair Pulling": f"{actor_label} can pull {target_label.lower()}'s hair easily",
        "Choking": f"{actor_label} can reach {target_label.lower()}'s neck",
        "Titjob": f"{actor_label} can use breasts to stimulate {target_label.lower()}'s penis",
        "Handjob": f"{actor_label} can stimulate {target_label.lower()}'s genitals by hand",
        "Scratching": f"{actor_label} can reach {target_label.lower()}",
        "Spanking": f"{actor_label} can access {target_label.lower()}'s backside",
        "Footjob": f"{actor_label} can use feet to stimulate {target_label.lower()}",
    }
    return True, reason_map.get(act_name, f"{actor_label} can perform {act_name} due to position and reach")