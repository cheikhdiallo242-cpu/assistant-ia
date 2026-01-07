import random

# =========================
# MÉMOIRE UTILISATEUR
# =========================
memory = {}

# =========================
# BASE TECHNIQUE RAP
# =========================

TECHNIQUES = [
    "multisyllabes",
    "images fortes",
    "oppositions",
    "vérité crue",
    "flow interne",
]

# =========================
# LIGNES RAP TECHNIQUES
# =========================

WOLOF_LINES = [
    "Xel bu leer, xol bu dëgër, sama yoon du daw",
    "Dëgg du ay wax, mooy ay jëf ci kaw",
    "Ci guddi gu lëndëm laa jàng boppam",
    "Ku muñ moo gën a dox, du ku wax rekk",
    "Sama baat dafay jaay xel, du ay fenn",
    "Dund bi dafa metti waaye jàng la",
    "Ku am xel du jàpp ndox mu tàq",
    "Sama flow dafay dox ni deret ci veine",
]

FRENCH_LINES = [
    "Je taille des phrases profondes, pas des slogans vides",
    "Chaque rime est pensée, chaque souffle est lucide",
    "Mon flow glisse, multisyllabes dans la matrice",
    "J’écris avec des cicatrices, pas avec des artifices",
    "La vérité cogne fort, pas besoin de décor",
    "J’ai appris dans l’ombre ce que la lumière ignore",
    "Je pèse chaque mot, discipline verbale",
    "Ma plume est tranchante, précision chirurgicale",
]

REFRAIN_WOLOF = [
    "Rap bi mooy sama liggéey",
    "Dëgg rekk laa wax",
    "Sama baat du wéy",
    "Xel bu leer, xol bu dëgër",
]

REFRAIN_FR = [
    "Je reste vrai même quand ça dérange",
    "Ma voix pèse, mon esprit s’engage",
    "Pas là pour plaire, là pour marquer",
    "Chaque mot vise, rien n’est jeté",
]

THEMES = {
    "vie": {
        "wolof": [
            "Dund mooy test bu sax",
            "Ku muñ moo gën a dox",
            "Yoon wi gudd na waaye ndam neex na",
            "Dund du yomb waaye dafay jàngal",
        ],
        "fr": [
            "La vie frappe sans prévenir",
            "Chaque jour forge le mental",
            "Vivre c’est tomber puis se relever",
            "La vie respecte les disciplinés",
        ]
    },
    "amour": {
        "wolof": [
            "Mbëggeel du ay wax rekk",
            "Xol bu bëgg dafay sonn",
            "Mbëggeel mooy testu xol",
            "Ku bëgg dëgg, bëgg metit",
        ],
        "fr": [
            "L’amour élève mais expose",
            "Aimer vrai demande du cran",
            "Les cœurs sincères paient le prix",
            "L’amour révèle qui tu es",
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
            "La rue enseigne sans pitié",
            "Le respect ne se demande pas",
            "Chaque erreur coûte cher",
            "Le bitume garde la mémoire",
        ]
    },
    "foi": {
        "wolof": [
            "Ku ragal Yàlla du ñakk yoon",
            "Yàlla rekk mooy sama ndimbal",
            "Foofu la doole di joge",
            "Xol bu am fooi du wér",
        ],
        "fr": [
            "La foi tient quand tout lâche",
            "Je marche droit par conviction",
            "Dieu avant le bruit",
            "Ma force ne vient pas d’ici",
        ]
    }
}

# =========================
# OUTILS RAP
# =========================

def unique_lines(lines, n):
    lines = list(dict.fromkeys(lines))
    random.shuffle(lines)
    while len(lines) < n:
        lines += lines
    return "\n".join(lines[:n])

def rap_freestyle(lang):
    lines = WOLOF_LINES if lang == "wolof" else FRENCH_LINES
    return (
        "🎤 FREESTYLE TECHNIQUE\n\n"
        + unique_lines(lines, 16)
        + "\n\n— flow libre, écriture maîtrisée —"
    )

def rap_theme(lang, theme):
    base = THEMES[theme][lang]
    technique = random.choice(TECHNIQUES)

    couplet1 = unique_lines(base + (WOLOF_LINES if lang == "wolof" else FRENCH_LINES), 16)
    refrain = unique_lines(REFRAIN_WOLOF if lang == "wolof" else REFRAIN_FR, 8)
    couplet2 = unique_lines(base + (WOLOF_LINES if lang == "wolof" else FRENCH_LINES), 16)

    return (
        f"🎯 THÈME : {theme.upper()} | TECHNIQUE : {technique}\n\n"
        f"🟦 COUPLET 1\n{couplet1}\n\n"
        f"🎶 REFRAIN\n{refrain}\n\n"
        f"🟦 COUPLET 2\n{couplet2}\n\n"
        f"🎶 REFRAIN\n{refrain}"
    )

# =========================
# CERVEAU IA
# =========================

def think(user_id, message):
    msg = message.lower().strip()

    if user_id not in memory:
        memory[user_id] = {"lang": None, "mode": None, "theme": None}

    state = memory[user_id]

    if msg in ["salut", "bonjour"]:
        return "👋 Salut Cheikh. Wolof ou français ?"

    if "wolof" in msg:
        state["lang"] = "wolof"
        state["mode"] = None
        return "🗣️ Wolof activé. Freestyle ou thème ?"

    if "français" in msg or "francais" in msg:
        state["lang"] = "fr"
        state["mode"] = None
        return "🇫🇷 Français activé. Freestyle ou thème ?"

    if state["lang"] is None:
        return "🌍 Choisis une langue : wolof ou français."

    if msg == "freestyle":
        state["mode"] = "freestyle"
        return rap_freestyle(state["lang"])

    if msg in ["thème", "theme"]:
        state["mode"] = "theme"
        return "🎯 Choisis un thème : vie, amour, rue, foi."

    if state["mode"] == "theme" and msg in THEMES:
        state["theme"] = msg
        return rap_theme(state["lang"], msg)

    if msg == "encore":
        if state["mode"] == "freestyle":
            return rap_freestyle(state["lang"])
        if state["mode"] == "theme":
            return rap_theme(state["lang"], state["theme"])

    return "🎤 Dis *freestyle* ou *thème*."
