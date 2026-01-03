function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  const userText = input.value.trim();
  if (!userText) return;

  const text = userText.toLowerCase();

  messages.innerHTML += `<div class="user">👤 ${userText}</div>`;
  input.value = "";

  let reply = "🤖 Je n’ai pas encore compris. Essaie : rap, wolof, aide, salut.";

  // ===== TEXTES RAP CONSCIENT WOOLOF =====
  const rapConscientWolof = [
    "🎤 Dundu bi jafe na, waaye dama jog, xel bu leer, sama yoon du ñàkk.\nÑu bare wax, waaye jëf mooy am solo,\nRap bi di xam-xam, du fecc, du dolo.",
    
    "🎤 Ma wax li ma gis, li ma dundu,\nDakar la ma jogé, sama xel du gëna gundu.\nRap conscient, wax dëgg, wax jàmm,\nKu am xel du jaay boppam ngir xaalis.",
    
    "🎤 Wolof laa def arme, xam-xam laa def bouclier,\nRap bi di école, du distraction, du piège.\nDama wër àddina, waaye dama fi taxaw,\nSama wax mooy fitna ci ku bëgg a daw."
  ];

  // ===== LOGIQUE =====
  if (text.includes("salut") || text.includes("bonjour")) {
    reply = "👋 Salut Cheikh, je suis là. Rap, wolof ou projets ?";
  }

  else if (text.includes("aide")) {
    reply = "🧠 Je peux écrire du rap, améliorer ton wolof et créer des idées.";
  }

  else if (text.includes("rap") && text.includes("wolof") && text.includes("conscient")) {
    const i = Math.floor(Math.random() * rapConscientWolof.length);
    reply = rapConscientWolof[i];
  }

  else if (text.includes("rap") || text.includes("texte")) {
    reply = "🎤 Tu veux un texte en wolof ou en français ?";
  }

  else if (text.includes("wolof")) {
    reply = "🗣️ Tu veux un texte street ou conscient ?";
  }

  messages.innerHTML += `<div class="bot">${reply}</div>`;
}
