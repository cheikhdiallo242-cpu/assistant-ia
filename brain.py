import random

# =========================
# MÉMOIRE UTILISATEUR
# =========================
memory = {}

# =========================
# BASES DE LIGNES
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
    "Rap bi du ay fenn",
    "Xel bu rafet mooy alal bu gëna rëy",
]

FRENCH_LINES = [
    "J’écris ma vérité même si elle dérange",
    "La rue m’a appris ce que l’école n’enseigne pas",
    "Chaque cicatrice raconte une histoire",
    "Le silence parle quand les mots mentent",
    "Je marche droit même quand la route tremble",
    "La foi me tient quand le monde lâche",
    "Je transforme la douleur en discipline",
    "Rien n’est donné, tout se mérite",
    "J’ai appris à perdre avant de gagner",
    "Le temps révèle les vrais visages",
]

REFRAIN_WOLOF = [
    "Rap bi mooy sama liggéey",
    "Xel bu leer, xol bu dëgër",
    "Sama baat dafay taxaw",
    "Dëgg rekk laa wax",
]

REFRAIN_FR = [
    "J’avance droit, même dans la tempête",
    "Ma voix résonne quand le monde se tait",
    "Je reste vrai quoi qu’il arrive",
    "Ma plume est libre, mon esprit aussi",
]

THEMES = {
    "amour": {
        "wolof": [
            "Mbëggeel du ay wax rekk",
            "Xol bu gën a metti mooy bu bëgg",
            "Ku bëgg dëgg, bëgg metit",
            "Amour dafay may doole ak metit",
        ],
        "fr": [
            "L’amour élève mais peut aussi briser",
            "Aimer vrai, c’est accepter de souffrir",
            "Les cœurs sincères saignent en silence",
            "L’amour demande plus que des promesses",
        ]
    },
    "rue": {
        "wolof": [
            "Rue bi dafa jàngal, du école",
            "Ci trottoir la ma jàng dund",
            "Rue bi mooy sama livre bu jëkk",
            "Ku am xel ci rue du réer",
        ],
        "fr": [
            "La rue m’a forgé sans pitié",
            "J’ai grandi là où l’erreur coûte cher",
            "Le bitume m’a appris la vérité",
            "Dans la rue, le respect se gagne",
        ]
    }
}

# =========================
# GÉNÉRATION
# =========================

def make_lines(lines, n):
    return "\n".join(random.choices(lines, k=n))

def make_refrain(lang):
    if lang == "wolof":
        return make_lines(REFRAIN_WOLOF, 8)
    return make_lines(REFRAIN_FR, 8)

def rap_theme(lang, theme):
    base = THEMES.get(theme, {}).get(lang)
    if not base:
        base = WOLOF_LINES if lang == "wolof" else FRENCH_LINES

    return (
        f"🎤 THÈME : {theme.upper()}\n\n"
        f"{make_lines(base, 16)}\n\n"
        f"🎶\n{make_refrain(lang)}\n🎶\n\n"
        f"{make_lines(base, 16)}\n\n"
        f"🎶\n{make_refrain(lang)}\n🎶"
    )

def rap_freestyle(lang):
    base = WOLOF_LINES if lang == "wolof" else FRENCH_LINES
    return (
        "🎤 FREESTYLE\n\n"
        f"{make_lines(base, 16)}"
    )

# =========================
# CERVEAU PRINCIPAL
# =========================

def think(user_id, message):
    msg = message.lower()

    if user_id not in memory:
        memory[user_id] = {
            "lang": None,
            "mode": None,
            "theme": None
        }

    state = memory[user_id]

    # SALUT
    if msg in ["salut", "bonjour", "slt"]:
        return "👋 Salut Cheikh. Tu veux du rap en wolof ou en français ?"

    # LANGUE
    if "wolof" in msg:
        state["lang"] = "wolof"
        return "🗣️ Wolof activé. Freestyle ou thème ?"

    if "français" in msg or "francais" in msg:
        state["lang"] = "fr"
        return "🇫🇷 Français activé. Freestyle ou thème ?"

    # FREESTYLE
    if "freestyle" in msg:
        state["mode"] = "freestyle"
        return rap_freestyle(state["lang"])

    # THÈME
    if "thème" in msg or "theme" in msg:
        state["mode"] = "theme"
        return "🎯 Donne-moi un thème (amour, rue, foi, vie…)."

    # THÈME PRÉCIS
    if msg in THEMES:
        state["theme"] = msg
        return rap_theme(state["lang"], msg)

    # ENCORE / AUTRE
    if msg in ["encore", "autre"]:
        if state["mode"] == "freestyle":
            return rap_freestyle(state["lang"])
        if state["mode"] == "theme":
            return rap_theme(state["lang"], state["theme"])

    # COOL / NICE
    if msg in ["cool", "nice"]:
        return "🔥 Content que ça te plaise. On est ensemble 💪"

    return "🎤 Dis *freestyle* ou *thème*."
