# Modelo IA — Sistema de identidad y generación de contenido

Sistema modular para generar foto y vídeo de **una misma persona sintética**, de forma
consistente, y publicarla en redes.

> Esta carpeta es independiente del proyecto Django de stock que vive en la raíz del
> repositorio. No comparte código ni dependencias. Si en algún momento quieres, se puede
> mover a su propio repositorio sin romper nada.

## Arquitectura

Nunca se pega el documento maestro entero en cada generación. Se construye por capas:

```
IDENTITY CORE  +  imágenes de referencia
      ↓
   ESCENA  →  ACCIÓN  →  CÁMARA  →  ILUMINACIÓN  →  MOVIMIENTO  →  NEGATIVOS
```

- El **CORE** no se toca nunca. Es la persona.
- Todo lo demás es variable y se cambia en cada pieza de contenido.

## Ficheros

| Fichero | Para qué sirve | Cuándo se usa |
|---|---|---|
| `00-identity-core-master.md` | Documento maestro completo (referencia canónica) | Nunca se pega entero. Consulta y auditoría |
| `01-identity-core-compact.md` | Versión corta del CORE, lista para pegar | En **cada** generación |
| `02-arquitectura-prompts.md` | Cómo montar un prompt por capas + slots | Al crear una pieza nueva |
| `03-negative-prompts.md` | Negativos cortos para imagen y para vídeo | En cada generación |
| `04-biblia-personaje.md` | Quién es: nombre, edad, ciudad, voz, nicho | Guion, copy, comentarios |
| `05-workflow-consistencia.md` | Pipeline, herramientas, control de calidad | Producción |
| `06-publicacion-y-cumplimiento.md` | Etiquetado IA por plataforma, riesgos | Antes de publicar |
| `plantillas/*.md` | Prompts listos por tipo de contenido | Día a día |
| `build_prompt.py` | Ensambla CORE + plantilla + variables | Día a día |

## Uso rápido

```bash
cd modelo-ia
python3 build_prompt.py --lista
python3 build_prompt.py mirror-selfie
python3 build_prompt.py talking-head --var LOCATION="hotel room, Madrid" --var MOOD="relaxed"
python3 build_prompt.py gym --video          # añade capa de movimiento + negativos de vídeo
```

Sale el prompt final por stdout, listo para copiar y pegar.
