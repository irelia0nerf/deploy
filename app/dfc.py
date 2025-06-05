from datetime import datetime

flags = ["trusted", "review", "blocked"]
flags_history = []

def get_flags():
    return {"flags": flags, "updated": False}

def update_flags(flag_req):
    global flags
    if flag_req.action == "add" and flag_req.flag not in flags:
        flags.append(flag_req.flag)
    elif flag_req.action == "remove" and flag_req.flag in flags:
        flags.remove(flag_req.flag)
    flags_history.append({
        "flag": flag_req.flag,
        "action": flag_req.action,
        "timestamp": datetime.utcnow().isoformat()
    })
    return {"flags": flags, "updated": True}
