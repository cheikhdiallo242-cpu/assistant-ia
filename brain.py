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

import random

def make_lines(lines, n):
    unique_lines = list(dict.fromkeys(lines))  # enlève doublons
    random.shuffle(unique_lines)

    if len(unique_lines) < n:
        unique_lines = unique_lines * (n // len(unique_lines) + 1)

    return "\n".join(unique_lines[:n])

def make_refrain(lang):
    if lang == "wolof":
        return make_lines(REFRAIN_WOLOF, 8)
    return make_lines(REFRAIN_FR, 8)

def rap_theme(lang, theme):
    lines = WOLOF_LINES if lang == "wolof" else FRENCH_LINES

    couplet1 = make_lines(lines, 16)
    refrain = make_lines(lines, 8)
    couplet2 = make_lines(lines, 16)

    return (
        f"🎯 THÈME : {theme.upper()}\n\n"
        f"🟦 COUPLET 1\n{couplet1}\n\n"
        f"🎶 REFRAIN\n{refrain}\n\n"
        f"🟦 COUPLET 2\n{couplet2}\n\n"
        f"🎶 REFRAIN\n{refrain}"
    )

def rap_freestyle(lang):
    lines = WOLOF_LINES if lang == "wolof" else FRENCH_LINES

    return (
        "🎤 FREESTYLE\n\n"
        + make_lines(lines, 16)
        + "\n\n— freestyle libre, pas de refrain —"
    )

# =========================
# CERVEAU PRINCIPAL
# =========================

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
        return "🗣️ Wolof activé. Freestyle ou thème ?"

    if "français" in msg or "francais" in msg:
        state["lang"] = "fr"
        state["mode"] = None
        return "🇫🇷 Français activé. Freestyle ou thème ?"

    # =========================
    # CHOIX DU MODE
    # =========================
    if msg == "freestyle":
        state["mode"] = "freestyle"
        return generate_freestyle(state["lang"])

    if msg == "thème" or msg == "theme":
        state["mode"] = "theme"
        return "🎯 Donne-moi un thème (rue, amour, foi, vie…)."

    # =========================
    # THÈME DONNÉ
    # =========================
    if state["mode"] == "theme" and state["theme"] is None:
        state["theme"] = msg
        return generate_theme(state["lang"], state["theme"])

    # =========================
    # ENCORE / AUTRE
    # =========================
    if msg in ["encore", "autre"]:
        if state["mode"] == "freestyle":
            return generate_freestyle(state["lang"])
        if state["mode"] == "theme":
            return generate_theme(state["lang"], state["theme"])

    return "🎤 Dis *freestyle* ou *thème*."
