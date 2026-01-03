let memory = {
  language: null,
  style: null
};

// ===============================
// 🗣️ RAP WOLOF (20)
// ===============================
const rapWolof = [
  "🎤 Dëgg laa wax, du fen, sama xel leer na.\nRap bi mooy sama yoon.",
  "🎤 Dundu bi metti waaye dama taxaw.\nKu ragal dund du jot.",
  "🎤 Wolof bi mooy sama racine,\nSama wax du ñàkk doole.",
  "🎤 Xel bu leer, xol bu dëgër,\nRap bi mooy sama liggéey.",
  "🎤 Sama wax dafay jur doole,\nFen du ma génn.",
  "🎤 Ñu ma gis ci suuf, waaye sama xel ci kaw.",
  "🎤 Ku am muñ am alal,\nRap bi mooy sama ndimbal.",
  "🎤 Sama dund mooy sama texte,\nDëgg laa di rapper.",
  "🎤 Rap bi du mbubb, mooy dund.",
  "🎤 Sama baat mooy sama arme.",
  "🎤 Dëgg du sonn, fen mooy dee.",
  "🎤 Dëgg laa wax ngir ñu déglu.",
  "🎤 Rap conscient, xel bu leer.",
  "🎤 Sama wax dafay jàngale.",
  "🎤 Wolof bi mooy sama doxalin.",
  "🎤 Sama plume du ragal.",
  "🎤 Rap bi mooy yoonu xel.",
  "🎤 Dëgg laa wax, ba fa dee.",
  "🎤 Ku am xel du jàpp fen.",
  "🎤 Sama rap dafay wér."
];

// ===============================
// 🇫🇷 RAP FRANÇAIS (20)
// ===============================
const rapFrancais = [
  "🎤 J’écris ce que je vis, pas ce qu’ils attendent.",
  "🎤 Le rap m’a sauvé quand tout était sombre.",
  "🎤 Ma plume est honnête, même quand ça fait mal.",
  "🎤 Pas besoin d’or pour briller.",
  "🎤 La vérité coûte cher mais elle libère.",
  "🎤 Je rappe pour ceux qu’on n’écoute jamais.",
  "🎤 Mon texte est brut, sans maquillage.",
  "🎤 Le silence m’a appris à écrire.",
  "🎤 J’ai transformé la douleur en couplets.",
  "🎤 Le rap c’est la vie, pas un décor.",
  "🎤 J’avance sans masque.",
  "🎤 La rue m’a donné le tempo.",
  "🎤 Chaque phrase est un combat.",
  "🎤 Je rappe pour rester debout.",
  "🎤 Ma voix est mon arme.",
  "🎤 Le rap m’a rendu libre.",
  "🎤 J’ai survécu grâce aux mots.",
  "🎤 J’écris vrai, je vis vrai.",
  "🎤 Le micro m’écoute plus que les hommes.",
  "🎤 Le rap c’est mon refuge."
];

// ===============================
// 🔥 FREESTYLE MIX (15)
// ===============================
const freestyleMix = [
  "🎤 Wolof dans la tête, français dans la voix.",
  "🎤 Je freestyle la vie, sans répétition.",
  "🎤 Pas de script, que du vécu.",
  "🎤 Même sans scène je rappe.",
  "🎤 Micro ouvert, cœur ouvert.",
  "🎤 Je rappe debout, jamais à genoux.",
  "🎤 Flow naturel, parole brute.",
  "🎤 La vérité sort sans filtre.",
  "🎤 Rap bi mooy dund.",
  "🎤 Chaque souffle est un freestyle.",
  "🎤 Pas de calcul, juste du feu.",
  "🎤 Je rappe même en silence.",
  "🎤 La rue m’inspire.",
  "🎤 Le freestyle c’est l’instant.",
  "🎤 Je parle comme je vis."
];

// ===============================
// 🧠 OUTILS
// ===============================
function random(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

// ===============================
// 🤖 IA LOGIQUE
// ===============================
function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  const userText = input.value.trim();
  if (!userText) return;

  const text = userText.toLowerCase();
  input.value = "";

  messages.innerHTML += `<div class="user">👤 ${userText}</div>`;

  let reply = "🤖 Dis-moi : rap, wolof, français ou freestyle.";

  if (text.includes("salut") || text.includes("bonjour") || text.includes("slt")) {
    reply = "👋 Salut Cheikh. Tu veux du rap ou un freestyle ?";
  }

  else if (text.includes("qui es tu") || text.includes("tu es qui")) {
    reply = "🤖 Je suis ton assistant rap personnel, créé pour t’aider à écrire vrai.";
  }

  else if (text.includes("aide")) {
    reply = "🧠 Je peux écrire du rap, freestyle, wolof ou français.";
  }

  else if (text.includes("wolof")) {
    memory.language = "wolof";
    reply = "🗣️ Wolof noté. Conscient ou freestyle ?";
  }

  else if (text.includes("français")) {
    memory.language = "français";
    reply = "🇫🇷 Français noté. Conscient ou freestyle ?";
  }

  else if (text.includes("freestyle")) {
    memory.style = "freestyle";
    reply = random(freestyleMix);
  }

  else if (text.includes("conscient")) {
    memory.style = "conscient";
    reply = memory.language === "wolof"
      ? random(rapWolof)
      : random(rapFrancais);
  }

  else if (text.includes("encore") || text.includes("continue")) {
    if (memory.style === "freestyle") reply = random(freestyleMix);
    else if (memory.language === "wolof") reply = random(rapWolof);
    else reply = random(rapFrancais);
  }

  else if (text.includes("rap")) {
    reply = "🎤 Tu veux en wolof ou en français ?";
  }

  messages.innerHTML += `<div class="bot">${reply}</div>`;
}
