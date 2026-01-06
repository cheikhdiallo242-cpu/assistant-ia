import random

# =========================
# MÉMOIRE UTILISATEUR
# =========================
memory = {}

# =========================
# LIGNES DE BASE
# =========================
WOLOF_LINES = [
    "Xel bu leer, xol bu dëgër",
    "Ku muñ moo gën a dox",
    "Nit ku xam sa bopp du topp mbubb mi",
    "Yoon wi gudd na waaye ndam neex na",
    "Sama baat dafay taxaw, du daw",
    "Dëgg du am xarit waaye mooy ndam",
    "Dund bi dafa metti waaye jàng la",
    "Ku ragal Yàlla du ñakk yoon",
    "Xel bu rafet mooy alal bu gëna rëy",
    "Rap bi du ay fenn",
]

REFRAIN = [
    "Rap bi mooy sama liggéey",
    "Xel bu leer, xol bu dëgër",
    "Sama baat dafay taxaw",
    "Dëgg rekk laa wax",
]

THEMES = {
    "amour": [
        "Mbëggeel du ay wax rekk",
        "Xol bu gën a metti mooy bu bëgg",
        "Ku bëgg dëgg, bëgg metit",
        "Amour dafay may doole ak metit",
        "Mbëggeel mooy jangoro bu neex",
    ],
    "rue": [
        "Rue bi dafa jàngal, du école",
        "Ci trottoir la ma jàng dund",
        "Rue bi mooy sama livre bu jëkk",
        "Bitim-réew du yomb waaye moo may doole",
        "Ku am doole ci rue am xel",
    ],
}

# =========================
# GÉNÉRATION STRUCTURÉE
# =========================
def make_couplet(lines, n):
    return "\n".join(random.choices(lines, k=n))

def make_refrain():
    return "\n".join(random.choices(REFRAIN, k=8))

def rap_theme(theme):
    base = THEMES.get(theme, WOLOF_LINES)
    return (
        f"🎤 Thème : {theme.upper()}\n\n"
        f"{make_couplet(base, 8)}\n\n"
        f"🎶\n{make_refrain()}\n🎶\n\n"
        f"{make_couplet(base, 8)}\n\n"
        f"🎶\n{make_refrain()}\n🎶"
    )

def rap_freestyle():
    return (
        "🎤 FREESTYLE\n\n"
        + make_couplet(WOLOF_LINES, 8)
    )

# =========================
# CERVEAU PRINCIPAL
# =========================
def think(user_id, message):
    msg = message.lower()

    if user_id not in memory:
        memory[user_id] = {
            "mode": None,
            "theme": None
        }

    state = memory[user_id]

    # SALUT
    if msg in ["salut", "bonjour", "slt"]:
        return "👋 Salut Cheikh. Tu veux du rap en wolof ou français ?"

    # LANGUE
    if "wolof" in msg:
        state["mode"] = "wolof"
        return "🗣️ Wolof activé. Dis *freestyle*, *conscient* ou donne un thème."

    # FREESTYLE
    if "freestyle" in msg:
        state["mode"] = "freestyle"
        return rap_freestyle()

    # CONSCIENT
    if "conscient" in msg:
        state["mode"] = "theme"
        state["theme"] = "conscience"
        return rap_theme("conscience")

    # THÈME
    if msg in THEMES:
        state["mode"] = "theme"
        state["theme"] = msg
        return rap_theme(msg)

    # ENCORE / AUTRE
    if msg in ["encore", "autre"]:
        if state["mode"] == "freestyle":
            return rap_freestyle()
        if state["mode"] == "theme":
            return rap_theme(state["theme"])

    # COOL / NICE
    if msg in ["cool", "nice"]:
        return "🔥 Content que ça te plaise. On est ensemble 💪"

    return "🎤 Dis *freestyle*, *conscient* ou donne un thème."
