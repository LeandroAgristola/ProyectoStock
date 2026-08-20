# Negative prompts

Un negativo de 200 palabras funciona **peor** que uno de 25 bien elegidas: el peso se reparte y
ningún término manda lo suficiente. Estas son las listas cortas de trabajo. La lista exhaustiva
está en el §24 del documento maestro, para cuando la herramienta admita negativos largos con peso
(Stable Diffusion / ComfyUI y similares).

---

## NEG-IMG — imagen fija (uso por defecto)

```text
plastic skin, waxy skin, airbrushed, oversmoothed, beauty filter, doll face, CGI render,
different person, altered facial proportions, different eye color, generic beauty nose,
dead eyes, glass eyes, exaggerated eyelashes, perfect symmetry,
malformed hands, extra fingers, fused fingers, missing fingers, warped wrists,
deformed teeth, warped lips, oversharpening, excessive HDR, artificial bokeh, uncanny valley
```

## NEG-IMG-CLOSEUP — añadir en primeros planos

```text
poreless skin, no skin texture, blurred facial detail, low-detail face, asymmetrical pupils,
misaligned pupils, artificial iris pattern, pure white sclera, exaggerated catchlights
```

## NEG-VID — vídeo (además de NEG-IMG)

```text
identity drift, face morphing, face flickering, texture flickering, hair flickering,
skin color shifting, eye color changing, changing teeth, changing lip volume,
temporal instability, frame interpolation artifacts, background warping, object teleportation,
robotic movement, mechanical head rotation, looping animation, frozen expression,
unnatural blinking, rubber face, floating hair, hair clipping through clothing
```

## NEG-TALK — vídeo hablando (además de NEG-VID)

```text
lip-sync artifacts, rubber lips, over-articulated mouth, frozen cheeks, static jaw,
teeth appearing and disappearing, changing tooth shape, unnatural tongue, mouth deformation
```

## NEG-BODY — plano entero / cuerpo

```text
exaggerated hourglass proportions, inconsistent body scale, elongated limbs, rubber limbs,
broken anatomy, floating feet, no contact shadow, inconsistent skin tone between face and body
```

---

## Cómo combinarlos

| Tipo de pieza | Negativos |
|---|---|
| Selfie / retrato | `NEG-IMG` + `NEG-IMG-CLOSEUP` |
| Foto de cuerpo entero | `NEG-IMG` + `NEG-BODY` |
| Vídeo B-roll (sin hablar) | `NEG-IMG` + `NEG-VID` |
| Vídeo hablando a cámara | `NEG-IMG` + `NEG-IMG-CLOSEUP` + `NEG-VID` + `NEG-TALK` |
| GRWM / manos en cuadro | `NEG-IMG` + refuerzo de manos con peso alto |

**Nota:** muchas herramientas de vídeo (Veo, Sora, Kling en su modo básico) **no tienen campo de
negativo**. Ahí la única vía es formular en positivo: en vez de `no robotic movement`, escribes
`natural human biomechanics with realistic acceleration and deceleration`. Cada bloque de arriba
tiene su equivalente positivo en `02-arquitectura-prompts.md`.
