# Workflow de producción y control de consistencia

## Pipeline recomendado

```
1. HOJA DE REFERENCIA (una sola vez, y bien)
        ↓
2. BANCO DE IMÁGENES BASE  (foto fija, muchos ángulos y escenas)
        ↓
3. IMAGE-TO-VIDEO          (animar la imagen ya aprobada)
        ↓
4. AUDIO / VOZ             (voz clonada fija)
        ↓
5. MONTAJE + QC            (checklist de deriva)
        ↓
6. PUBLICACIÓN
```

Regla que sostiene todo el sistema: **nunca se genera vídeo desde texto puro.** Siempre desde una
imagen fija ya validada. El texto no es capaz de sostener una identidad; una imagen sí.

---

## 1. Hoja de referencia

Ya la tienes (la parrilla multiángulo + el selfie). Es el activo más valioso del proyecto:
**guárdala versionada y no la pierdas.** Idealmente:

- 3 frontales (neutra, sonrisa leve, hablando)
- 2 tres cuartos (izquierda y derecha)
- 2 perfiles puros (izquierda y derecha)
- 1 cuerpo entero, ropa ajustada y neutra, fondo liso
- 1 primer plano extremo de piel (para textura)
- Todas con **la misma luz neutra y difusa**, sin maquillaje extremo

Si le añades el cuerpo entero y el close-up de piel a lo que ya tienes, la hoja queda completa.

## 2. Métodos de fijación de identidad, de mejor a peor

| Método | Consistencia | Coste | Cuándo |
|---|---|---|---|
| **LoRA / modelo entrenado** con 20–40 imágenes suyas | Muy alta | Alto (setup) | Cuando el volumen justifique el esfuerzo |
| **Character reference nativo** (referencia de personaje de la herramienta) | Alta | Bajo | Punto de partida por defecto |
| **Image-to-image / edición sobre foto base** | Alta en cara, limitada en pose | Bajo | Cambiar ropa, fondo, luz |
| **Solo texto con el CORE** | Baja | Nulo | Solo planos generales donde la cara no se lee |

El salto de calidad real está en el LoRA. Todo lo anterior es puente hasta llegar ahí.
Para entrenarlo necesitas primero un banco consistente de 20–40 imágenes suyas aprobadas — que es
exactamente lo que produce la fase 2.

## 3. Herramientas (el ecosistema cambia rápido; verifica antes de contratar)

- **Imagen con referencia de personaje:** Midjourney (referencia de personaje), Flux + LoRA,
  editores de imagen por instrucción tipo Nano Banana / Flux Kontext, Seedream.
- **Vídeo image-to-video:** Kling, Veo, Runway, Hailuo, Sora. Prioriza el que mejor conserve la cara
  en tus pruebas, no el que tenga mejor movimiento de cámara.
- **Voz:** clonación de voz fija (ElevenLabs y equivalentes). **Una sola voz para siempre.**
  Cambiar de voz rompe el personaje tanto como cambiar de cara.
- **Labios / lipsync:** solo si el vídeo hablando directo no te da calidad suficiente.
- **Upscale y grano:** un upscale suave + grano ligero mata mucho del "look IA". No sobresharpen.

Haz una **prueba comparativa** con las mismas 3 escenas en 2–3 herramientas antes de suscribirte
a ninguna. La diferencia en conservación de identidad entre herramientas es enorme.

## 4. Control de calidad — checklist antes de publicar

Cara:
- [ ] Los ojos son del mismo color que en la referencia (el fallo nº1)
- [ ] La nariz de perfil coincide con el perfil de referencia
- [ ] La distancia entre ojos y la anchura de boca no han cambiado
- [ ] Hay poro visible; la piel no es de cera
- [ ] Las pupilas están alineadas y no hay brillos imposibles

Manos y cuerpo:
- [ ] 5 dedos por mano, sin fusiones
- [ ] El móvil está sujeto de forma físicamente posible
- [ ] Las proporciones del cuerpo coinciden con piezas anteriores
- [ ] Tono de piel de cara y cuerpo coincide

Vídeo:
- [ ] Ver el clip **a 0,25×**: ahí aparece el morphing que a velocidad normal no ves
- [ ] La cara no cambia entre el primer y el último fotograma
- [ ] Parpadea, y a intervalos irregulares
- [ ] El pelo se mueve por inercia, no rígido
- [ ] No hay parpadeo de textura en el fondo
- [ ] Si habla: los dientes no cambian de forma entre sílabas

Entorno:
- [ ] Los reflejos y sombras son coherentes con la luz
- [ ] Los textos del fondo (carteles, etiquetas) no son galimatías
- [ ] Es un fondo canónico o justificable en la narrativa

## 5. Organización de archivos

```
modelo-ia/
├── referencias/           ← hoja multiángulo, NO tocar, versionada
├── banco-imagenes/        ← imágenes aprobadas, nombradas por escena
│   └── 2026-08-20_dormitorio_selfie_01.png
├── descartes/             ← lo que falló y por qué (esto enseña mucho)
└── publicado/             ← lo que ya está en redes, con fecha y plataforma
```

Nombrado sugerido: `AAAA-MM-DD_escena_tipo_NN.ext`. Guarda junto a cada pieza el prompt exacto y la
semilla si la herramienta la da: sin eso no puedes reproducir un acierto.

## 6. Registro de versiones del CORE

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| v1.0 | 2026-08-20 | CORE inicial a partir de la hoja multiángulo + selfie | Arranque |

Cualquier cambio en la anatomía descrita sube versión. Anótalo aquí siempre: cuando dentro de tres
meses el contenido de enero no case con el de abril, este registro es la única forma de saber por qué.
