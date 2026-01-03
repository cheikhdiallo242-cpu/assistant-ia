// ===== MÉMOIRE SIMPLE =====
let lastLanguage = null;
let lastStyle = null;

// ===== BASE DE TEXTES =====
const rapWolof = [
  "🎤 Dundu bi metti na, waaye dama dox ci dëgg,\nSama xel dafay leer, dùgguma ci fen.",
  "🎤 Wolof laa def arme, xam-xam laa def doole,\nKu xamul boppam, rap bi du ko sol.",
  "🎤 Ñu bare di wax, waaye jëf mooy solo,\nRap conscient, du fecc, du yëngu solo."
];

const rapFrancais = [
  "🎤 J’écris pour survivre, pas pour plaire au système,\nMa plume est honnête, même quand le monde saigne.",
  "🎤 Pas besoin d’or pour briller, j’ai la parole et la dalle,\nChaque phrase est un combat, chaque rime une rafale.",
  "🎤 J’rappe pour ceux qu’on n’écoute pas,\nLa vérité dérange, mais moi je l’écris là."
];

const freestyleMix = [
  "🎤 Xel bu leer dans un monde flou,\nJe rappe en wolof, en français, toujours debout.",
  "🎤 Dakar dans le cœur, micro dans la main,\nRap bi mooy yoon, même quand demain est incertain.",
  "🎤 Même sans scène, je freestyle la vérité,\nRap bi du jeu, c’est une nécessité."
];

// ===== OUTIL RANDOM =====
function randomFrom(array) {
  return array[Math.floor(Math.random() * array.length)];
}

// ===== FONCTION PRINCIPALE =====
function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  const userText = input.value.trim();
  if (!userText) return;

  const text = userText.toLowerCase();

  messages.innerHTML += `<div class="user">👤 ${userText}</div>`;
  input.value = "";

  let reply = "🤖 Je n’ai pas compris. Tu veux : rap, freestyle, wolof ou français ?";

  // ===== SALUTATIONS =====
  if (text.includes("salut") || text.includes("slt") || text.includes("bonjour")) {
    reply = "👋 Salut Cheikh. Tu veux un texte rap, freestyle ou conscient ?";
  }

  // ===== COMPLIMENTS =====
  else if (text.includes("nice") || text.includes("bien") || text.includes("ok")) {
    reply = "🙏 Merci. Tu veux encore un autre ?";
  }

  // ===== LANGUES =====
  else if (text.includes("wolof")) {
    lastLanguage = "wolof";
    reply = "🗣️ Wolof noté. Tu veux conscient ou freestyle ?";
  }

  else if (text.includes("français")) {
    lastLanguage = "français";
    reply = "🇫🇷 Français noté. Conscient ou freestyle ?";
  }

  // ===== STYLES =====
  else if (text.includes("conscient")) {
    lastStyle = "conscient";

    if (lastLanguage === "wolof") {
      reply = randomFrom(rapWolof);
    } else {
      reply = randomFrom(rapFrancais);
    }
  }

  else if (text.includes("freestyle")) {
    lastStyle = "freestyle";
    reply = randomFrom(freestyleMix);
  }

  // ===== DEMANDE GÉNÉRALE RAP =====
  else if (text.includes("rap") || text.includes("texte")) {
    reply = "🎤 Tu veux en wolof ou en français ?";
  }

  // ===== ENCORE / AUTRE =====
  else if (text.includes("encore") || text.includes("autre")) {
    if (lastStyle === "freestyle") {
      reply = randomFrom(freestyleMix);
    } else if (lastLanguage === "wolof") {
      reply = randomFrom(rapWolof);
    } else {
      reply = randomFrom(rapFrancais);
    }
  }

  messages.innerHTML += `<div class="bot">${reply}</div>`;
}
