let memory = {
  language: null,
  style: null
};

const rapWolof = [
  "🎤 Dëgg laa wax, du fen, sama xel leer na.\nRap bi mooy yoon, ba ma dee.",
  "🎤 Dundu bi metti, waaye dama jog ci kow.\nWolof bi mooy sama arme.",
  "🎤 Ku xam boppam du ragal,\nRap conscient mooy sama signal."
];

const rapFrancais = [
  "🎤 J’écris ce que je vis, pas ce qu’ils veulent entendre.\nMa plume est libre.",
  "🎤 Le rap m’a sauvé quand le monde m’a lâché.",
  "🎤 Pas besoin d’or pour briller,\nJ’ai la parole et la vérité."
];

const freestyleMix = [
  "🎤 Wolof dans la tête, français dans la voix,\nJe freestyle ma vie, je triche pas.",
  "🎤 Même sans scène je rappe debout,\nLa vérité sort brute.",
  "🎤 Rap bi mooy dund,\nMicro mooy sama doom."
];

function random(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  const userText = input.value.trim();
  if (!userText) return;

  const text = userText.toLowerCase();
  input.value = "";

  messages.innerHTML += `<div class="user">👤 ${userText}</div>`;

  let reply = "🤖 Dis-moi ce que tu veux : rap, wolof, freestyle ou aide.";

  // 👋 SALUTATIONS
  if (
    text.includes("salut") ||
    text.includes("bonjour") ||
    text.includes("slt")
  ) {
    reply = "👋 Salut Cheikh. Tu veux du rap, du wolof ou un freestyle ?";
  }

  // 🧠 QUI ES-TU
  else if (
    text.includes("qui es tu") ||
    text.includes("tu es qui") ||
    text.includes("c'est qui") ||
    text.includes("t'es qui")
  ) {
    reply = "🤖 Je suis ton assistant rap personnel. Je t’aide à écrire, freestyle et améliorer ton wolof.";
  }

  // 🤝 AIDE
  else if (
    text.includes("aide") ||
    text.includes("aider") ||
    text.includes("m'aider") ||
    text.includes("me aider")
  ) {
    reply = "🧠 Je peux écrire du rap, freestyle, wolof ou français. Dis juste ce que tu veux.";
  }

  // 🌍 LANGUES
  else if (text.includes("wolof")) {
    memory.language = "wolof";
    reply = "🗣️ Wolof noté. Tu veux conscient ou freestyle ?";
  }

  else if (text.includes("français")) {
    memory.language = "français";
    reply = "🇫🇷 Français noté. Conscient ou freestyle ?";
  }

  // 🎤 STYLES
  else if (text.includes("conscient")) {
    memory.style = "conscient";
    reply = memory.language === "wolof"
      ? random(rapWolof)
      : random(rapFrancais);
  }

  else if (text.includes("freestyle")) {
    memory.style = "freestyle";
    reply = random(freestyleMix);
  }

  // 🔁 ENCORE
  else if (
    text.includes("encore") ||
    text.includes("autre") ||
    text.includes("continue")
  ) {
    if (memory.style === "freestyle") {
      reply = random(freestyleMix);
    } else if (memory.language === "wolof") {
      reply = random(rapWolof);
    } else {
      reply = random(rapFrancais);
    }
  }

  // 🎶 RAP GÉNÉRAL
  else if (text.includes("rap")) {
    reply = "🎤 Tu veux en wolof ou en français ?";
  }

  messages.innerHTML += `<div class="bot">${reply}</div>`;
}
