# Arquitectura de prompts por capas

## El esqueleto

```
[1] IDENTITY CORE     ← fijo, de 01-identity-core-compact.md
[2] ESCENA            ← dónde está, qué lleva puesto, qué hay alrededor
[3] ACCIÓN            ← qué hace, expresión, pose
[4] CÁMARA            ← plano, lente, distancia, ángulo, formato
[5] ILUMINACIÓN       ← fuente, dirección, temperatura, hora
[6] MOVIMIENTO        ← SOLO vídeo: micromovimiento, cámara, física del pelo
[7] NEGATIVOS         ← de 03-negative-prompts.md
```

Orden importante: la mayoría de modelos pondera más lo que va **al principio**. La identidad va
primero siempre. En herramientas que aceptan pesos, la identidad es lo que se refuerza.

---

## Plantilla vacía — IMAGEN

```text
[CORE]

Scene: [LOCATION], [TIME OF DAY]. She wears [OUTFIT]. [ENVIRONMENT DETAILS].
Action: she is [ACTIVITY], [POSE]. Expression: [FACIAL EXPRESSION], [MOOD].
Hair: [HAIRSTYLE]. Makeup: [MAKEUP INTENSITY].
Camera: [SHOT TYPE], [LENS], [ANGLE], [ASPECT RATIO]. [DEPTH OF FIELD].
Light: [LIGHT SOURCE], [DIRECTION], [QUALITY], [COLOR TEMPERATURE].
Look: authentic social-media capture, not a studio production. Slightly imperfect framing.
Visible skin texture and pores. Natural highlight roll-off. Subtle sensor noise.

Negative: [NEGATIVOS IMAGEN]
```

## Plantilla vacía — VÍDEO

```text
[CORE]

Scene: [LOCATION], [TIME OF DAY]. She wears [OUTFIT].
Action: [ACTIVITY] for [VIDEO DURATION]. [DIALOGUE si habla].
Expression: [FACIAL EXPRESSION] evolving naturally, not held static.
Camera: [SHOT TYPE], [CAMERA MOVEMENT], handheld with subtle natural shake.
Light: [LIGHT SOURCE], [DIRECTION]. Light must respond as she moves.
Motion: natural human biomechanics — irregular blinking, subtle breathing, small gaze shifts,
micro posture adjustments, hair lagging slightly behind head movement and settling by inertia.
Identity lock: the face must stay anatomically identical in every frame. No morphing between frames.

Negative: [NEGATIVOS VIDEO]
```

---

## Vocabulario por capa (copia y pega)

### Cámara — tipo de plano
`extreme close-up` · `close-up portrait` · `bust shot` · `waist-up medium shot` ·
`three-quarter shot` · `full body shot` · `wide environmental shot` · `over-the-shoulder` ·
`mirror selfie framing` · `handheld front-facing selfie, arm's length`

### Cámara — lente y equipo
- Selfie / contenido nativo: `shot on iPhone 15 Pro front camera, 23mm equivalent, slight wide-angle distortion`
- Contenido "de fotógrafo": `85mm f/1.8, shallow depth of field, natural bokeh`
- Lifestyle abierto: `35mm f/2.0, environmental context in focus`
- Vídeo social: `vertical 9:16, 4K, handheld, natural motion blur`

### Iluminación
`soft window light from the left` · `golden hour backlight with warm rim on the hair` ·
`overcast diffused daylight` · `bathroom vanity light, soft frontal` ·
`warm indoor lamp light, 2700K, mixed with cool window light` ·
`car interior daylight through windshield` · `night street light, mixed neon reflections` ·
`gym overhead fluorescent, slightly cool` · `restaurant candlelight, warm and low`

### Expresión / mood
`relaxed neutral, calm confidence` · `soft closed-lip smile starting in the eyes` ·
`genuine laugh with cheek elevation and eye involvement` · `mid-sentence, natural talking face` ·
`distracted, looking away from the lens` · `playful, slight head tilt` · `tired-but-happy, end of day`

### Movimiento (solo vídeo)
`slowly turns her head to camera and settles` · `tucks hair behind her ear` ·
`walks toward camera, natural weight shift` · `laughs and looks away` ·
`applies lip gloss looking into the mirror` · `talks to camera, gesturing occasionally with one hand` ·
`adjusts phone angle mid-recording` · `shifts weight, small posture correction`

### Movimiento de cámara
`static handheld with subtle natural shake` · `slow push-in` · `slow pan following her` ·
`phone held in hand, walking, natural bounce` · `locked-off tripod, she moves within frame`

---

## Reglas que evitan el 80 % de los fallos

1. **Una acción por generación.** "Camina, se ríe, se recoge el pelo y saluda" produce morphing.
   Un vídeo = un gesto principal.
2. **Vídeos de 5–8 segundos.** Casi todos los modelos empiezan a derivar la identidad a partir
   de los ~8 s. Para clips más largos, encadena tomas cortas con corte de montaje.
3. **Image-to-video antes que text-to-video.** Genera primero un fotograma que te guste y anímalo.
   La identidad la fija la imagen, no el texto.
4. **Nunca describas la cara y la escena mezcladas.** Bloque de identidad, punto, bloque de escena.
5. **Manos: o se ven bien o se esconden.** Si la pieza no necesita las manos, sácalas de encuadre
   o mételas en un bolsillo. Es más barato que reintentar 15 veces.
6. **No pidas perfección.** `slightly imperfect framing`, `not perfectly posed`, `candid` son las
   palabras que separan "contenido de creadora" de "render de IA".
7. **Un cambio por iteración.** Si cambias luz + ropa + ángulo a la vez, no sabes qué funcionó.
