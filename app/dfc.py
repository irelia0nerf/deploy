flags = ["trusted", "review", "blocked"]

def get_flags():
    return {"flags": flags, "updated": False}

def update_flags(flag_req):
    global flags
    if flag_req.action == "add" and flag_req.flag not in flags:
        flags.append(flag_req.flag)
    elif flag_req.action == "remove" and flag_req.flag in flags:
        flags.remove(flag_req.flag)
    return {"flags": flags, "updated": True}
