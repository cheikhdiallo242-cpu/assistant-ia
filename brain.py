def think(user_id, message):
    msg = message.lower().strip()

    if user_id not in memory:
        memory[user_id] = {
            "lang": None,
            "mode": None,
            "theme": None
        }

    state = memory[user_id]

    # =========================
    # RÉPONSES HUMAINES
    # =========================
    if msg in ["salut", "bonjour", "slt"]:
        return "👋 Salut Cheikh. Tu veux du rap en wolof ou en français ?"

    if msg in ["qui es tu", "qui es-tu"]:
        return "🤖 Je suis ton assistant rap intelligent, créé pour t’aider à écrire du rap authentique."

    if msg in ["qui t'a créé", "qui t’a créé"]:
        return "🧠 J’ai été créé par Cheikh pour transformer les idées en rap solide."

    if msg in ["cool", "nice"]:
        return "🔥 Content que ça te plaise. On est ensemble 💪"

    if msg == "merci":
        return "🙏 Avec plaisir. On avance ensemble."

    # =========================
    # CHOIX DE LANGUE
    # =========================
    if "wolof" in msg:
        state["lang"] = "wolof"
        state["mode"] = None
        state["theme"] = None
        return "🗣️ Wolof activé. Freestyle ou thème ?"

    if "français" in msg or "francais" in msg:
        state["lang"] = "fr"
        state["mode"] = None
        state["theme"] = None
        return "🇫🇷 Français activé. Freestyle ou thème ?"

    # =========================
    # PROTECTION : langue obligatoire
    # =========================
    if state["lang"] is None:
        return "🌍 Choisis d’abord une langue : wolof ou français."

    # =========================
    # CHOIX DU MODE
    # =========================
    if msg == "freestyle":
        state["mode"] = "freestyle"
        state["theme"] = None
        return rap_freestyle(state["lang"])

    if msg in ["thème", "theme"]:
        state["mode"] = "theme"
        state["theme"] = None
        return "🎯 Donne-moi un thème (rue, amour, foi, vie…)."

    # =========================
    # THÈME DONNÉ (CLÉ DU BUG)
    # =========================
    if state["mode"] == "theme" and msg in THEMES:
        state["theme"] = msg
        return rap_theme(state["lang"], msg)

    if state["mode"] == "theme" and msg not in THEMES:
        return "🎯 Thème non reconnu. Choisis : rue, amour, vie ou foi."

    # =========================
    # ENCORE / AUTRE
    # =========================
    if msg in ["encore", "autre"]:
        if state["mode"] == "freestyle":
            return rap_freestyle(state["lang"])
        if state["mode"] == "theme" and state["theme"]:
            return rap_theme(state["lang"], state["theme"])

    return "🎤 Dis *freestyle* ou *thème*."
