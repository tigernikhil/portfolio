---
name: kyahoga-microdrama
description: Production-grade blueprint for creating viral interactive micro-drama short-form reels (Hindi horror, suspense, thriller) matching @aage.kya.hoga.stories. Enforces dynamic emotional pacing ("sometime more, sometime less"), zero spoken Foley rule, acoustic sound effects layering, 3-character consistent rigs, 1080x1920 Playwright/Canvas progressive rendering, and EBU R128 loudness mastering. Compatible with both cloud agents and local models (Ollama).
---

# Kyahoga Interactive Micro-Drama Production Skill

## 1. Overview & Golden Standards
This skill governs the end-to-end automated generation of high-retention 9:16 vertical short-form reels (40–55s) in Hindi. It standardizes the lessons learned from the production of **Room 404 (Episode 001)** into a repeatable engine for any episode or franchise.

### Core Commandments
1. **Never speak Foley sound words with the narrator's voice**:
   - ❌ Never speak: `"खट-खट"`, `"धम"`, `"चटाक"`, `"चीं"`.
   - ✅ Narrator speaks tense setup (*"सन्नाटे में... अचानक उस बंद कमरे के दरवाजे से आवाज़ आई—"*), followed immediately by real acoustic Foley audio.
2. **Dynamic Pacing ("Sometime More, Sometime Less")**:
   - Intra-sentence breathing: `auto-editor --margin 0.16s`.
   - Trailing pauses must be emotionally modulated based on the dramatic weight of the preceding sentence.
3. **Consistent Character Rigs**:
   - **Aryan** (Lead / Action-taker: black hoodie, phone).
   - **Kabir** (Skeptic / Analyst: teal sweater, round glasses, documents).
   - **Vicky** (Panicker / Audience Surrogate: yellow '99' hoodie, shock eyes).
4. **Broadcast Audio Mastering**:
   - Continuous 55Hz sub-bass ambient drone at 0.18 volume.
   - EBU R128 Loudnorm (`-1.2 dB` True Peak, `-18.4 dB` LUFS) for mobile phone speaker punch.

---

## 2. Emotional Pause Calibration Matrix

| Beat Role | Narrative Function | Voice Rate & Pitch | Trailing Pause (`tail_pause`) | Why |
|---|---|---|---|---|
| **HOOK_RUSH** | 3:15 AM crisis in media res | Rate `+9%`, Pitch `-1Hz` | `0.45s` | Lets the ominous warning settle before the backstory. |
| **TABLE_ASSEMBLY** | Strategy / Lease Contract discussion | Rate `+8%`, Pitch `-1Hz` | `0.40s` | Ominous condition lingers as friends look toward danger. |
| **HALLWAY_STALK** | Approaching the danger with flashlight | Rate `+7%`, Pitch `-2Hz` | `0.35s` | Creeping suspension leading into the sudden shock. |
| **SHOCK_CLIMAX** | Sudden door knock / impact | Rate `+10%`, Pitch `+1Hz` | **`0.60s`** | **Stunned frozen silence** right after the sound effect. |
| **GROUND_MACRO** | Note/clue sliding into flashlight beam | Rate `+8%`, Pitch `-1Hz` | `0.35s` | Tense pause as characters reach down for the clue. |
| **TWIST_REVEAL** | Shocking revelation read aloud | Rate `+8%`, Pitch `-2Hz` | **`0.65s`** | **Deep chilling dread vacuum** after the plot twist. |
| **DILEMMA_HUD** | Key turns in lock + [A] vs [B] vote | Rate `+10%`, Pitch `+1Hz` | **`0.85s`** | Gives viewers time to process choices and comment. |

---

## 3. Standard Episode Manifest Schema (JSON)

Every episode script must be structured as a 7-beat JSON manifest:

```json
[
  {
    "id": 1,
    "role": "HOOK_RUSH",
    "text": "रात के सवा तीन बजे टेबल पर रखे फोन की स्क्रीन जली। मकान मालिक का मैसेज था— चौथे कमरे से कोई भी आवाज़ आए... ताला मत खोलना!",
    "rate": "+9%",
    "pitch": "-1Hz",
    "sub_prefix": "3:15 AM: Phone jala...",
    "sub_highlight": "Taala mat kholna!",
    "sub_suffix": "Makan Malik",
    "foley": "foley_phone_vibe",
    "foley_delay": 0.05,
    "tail_pause": 0.45
  },
  {
    "id": 2,
    "role": "TABLE_ASSEMBLY",
    "text": "हम तीन दोस्तों को ये फ्लैट आधी कीमत पर मिला था, लेकिन शर्त बस एक ही थी— वो चौथा कमरा... हमेशा बंद रहेगा।",
    "rate": "+8%",
    "pitch": "-1Hz",
    "sub_prefix": "Hum 3 dosto ko flat mila...",
    "sub_highlight": "Chautha Kamra Band Rahega",
    "sub_suffix": "Adhi Keemat Par",
    "foley": "foley_clock_tick",
    "foley_delay": 0.08,
    "tail_pause": 0.40
  },
  {
    "id": 4,
    "role": "SHOCK_CLIMAX",
    "text": "सन्नाटे में... अचानक उस बंद कमरे के दरवाजे से आवाज़ आई—",
    "rate": "+10%",
    "pitch": "+1Hz",
    "sub_prefix": "Sannate mein andar se...",
    "sub_highlight": "Darwaze par Dastak!",
    "sub_suffix": "Khat-Khat Aawaz",
    "foley": "foley_door_bang",
    "foley_delay": "end",
    "tail_pause": 0.60
  }
]
```

---

## 4. Local Model Integration (Ollama / Offline LLM)

Local models (`llama3:8b`, `qwen2.5:7b`, `mistral:7b`) can draft new episodes completely offline using this strict system prompt:

### System Prompt for Local LLM:
```text
You are the Lead Screenwriter for Kyahoga Studio (@aage.kya.hoga.stories).
Write a 7-beat interactive Hindi suspense micro-drama reel script.

STRICT CONSTRAINTS:
1. Exactly 7 beats in JSON format.
2. The narrator MUST NEVER SPEAK FOLEY WORDS ("खट-खट", "धम", "चीं"). Lead with tension, then end with a dash "—" where the sound effect plays.
3. Every beat must have an emotional 'tail_pause' in seconds:
   - Setup/Exposition: 0.35s
   - Warning/Ominous: 0.40s
   - Shock/Jump impact: 0.60s (stunned silence)
   - Twist reveal: 0.65s (dread vacuum)
   - Dilemma question: 0.85s (comment buffer)
4. Use clean Hindi prose without raw XML tags. Use ellipsis '...' only where a natural breath occurs.
5. Return ONLY a valid JSON array matching the Kyahoga schema.
```

---

## 5. Automated Pipeline Execution

Run the universal pipeline engine:
```bash
/Users/admin/Documents/insta/.venv/bin/python3 /Users/admin/Documents/insta/scripts/kyahoga_pipeline_engine.py \
  --manifest /path/to/beats_manifest.json \
  --html /path/to/web/index.html \
  --output /path/to/master_cut.mp4
```
This automatically handles:
1. `edge-tts` synthesis with `hi-IN-SwaraNeural`.
2. `auto-editor --margin 0.16s` silence trimming.
3. Foley track layering and exact silence tail padding.
4. Playwright headless progressive rendering at 1080x1920 30fps.
5. FFmpeg concat, 55Hz sub-bass ambient drone mixing, and EBU R128 Loudnorm mastering.
