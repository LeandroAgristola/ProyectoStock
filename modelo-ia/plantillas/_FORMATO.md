# Formato de las plantillas

Cada plantilla es un `.md` con tres partes que `build_prompt.py` sabe leer:

```
---
name: identificador-sin-espacios
type: image | video
core: A | B | C          # qué versión del CORE inyectar
negatives: NEG-IMG,NEG-IMG-CLOSEUP
---

## DEFAULTS
CLAVE=valor por defecto

## PROMPT
Texto del prompt con {CLAVE} entre llaves.

## VIDEO            (opcional: capa de movimiento, se añade con --video)
Texto extra.
```

Para crear una plantilla nueva, copia la más parecida y cambia lo que necesites.
Las claves en `{LLAVES}` se pueden sobrescribir desde la línea de comandos con `--var CLAVE=valor`.
