#!/usr/bin/env python3
"""Ensambla el prompt final: IDENTITY CORE + escena + negativos.

Uso:
    python3 build_prompt.py --lista
    python3 build_prompt.py mirror-selfie
    python3 build_prompt.py talking-head --var LOCATION="hotel room" --var MOOD="relaxed"
    python3 build_prompt.py gym --video
    python3 build_prompt.py cafe --core B
"""

import argparse
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
CORE_FILE = BASE / "01-identity-core-compact.md"
NEG_FILE = BASE / "03-negative-prompts.md"
TPL_DIR = BASE / "plantillas"


def read(path):
    if not path.exists():
        sys.exit(f"No encuentro {path}")
    return path.read_text(encoding="utf-8")


def load_cores():
    """Devuelve {'A': texto, 'B': texto, 'C': texto} leyendo los bloques ```text``` de cada sección."""
    text = read(CORE_FILE)
    cores = {}
    for letter, body in re.findall(r"^##\s+([ABC])\)(.*?)(?=^##\s|\Z)", text, re.S | re.M):
        block = re.search(r"```text\n(.*?)```", body, re.S)
        if block:
            cores[letter] = " ".join(block.group(1).split())
    return cores


def load_negatives():
    """Devuelve {'NEG-IMG': texto, ...} leyendo los bloques ```text``` bajo cada '## NEG-...'."""
    text = read(NEG_FILE)
    negs = {}
    for name, body in re.findall(r"^##\s+(NEG-[A-Z-]+)(.*?)(?=^##\s|\Z)", text, re.S | re.M):
        block = re.search(r"```text\n(.*?)```", body, re.S)
        if block:
            negs[name] = " ".join(block.group(1).split())
    return negs


def parse_template(path):
    text = read(path)
    meta, defaults, sections = {}, {}, {}

    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if fm:
        for line in fm.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        text = text[fm.end():]

    for name, body in re.findall(r"^##\s+([A-Z]+)\n(.*?)(?=^##\s|\Z)", text, re.S | re.M):
        sections[name] = body.strip()

    for line in sections.get("DEFAULTS", "").splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            defaults[k.strip()] = v.strip()

    return meta, defaults, sections


def substitute(text, values):
    missing = []

    def repl(match):
        key = match.group(1)
        if key in values:
            return values[key]
        missing.append(key)
        return "{" + key + "}"

    out = re.sub(r"\{([A-Z_][A-Z0-9_]*)\}", repl, text)
    return out, sorted(set(missing))


def main():
    ap = argparse.ArgumentParser(description="Ensambla prompts de la modelo IA.")
    ap.add_argument("plantilla", nargs="?", help="nombre de la plantilla (sin .md)")
    ap.add_argument("--lista", action="store_true", help="lista las plantillas disponibles")
    ap.add_argument("--var", action="append", default=[], metavar="CLAVE=valor",
                    help="sobrescribe una variable de la plantilla")
    ap.add_argument("--core", choices=["A", "B", "C"], help="fuerza una versión del CORE")
    ap.add_argument("--video", action="store_true", help="incluye la capa de movimiento y negativos de vídeo")
    ap.add_argument("--sin-negativos", action="store_true", help="omite el bloque de negativos")
    args = ap.parse_args()

    plantillas = sorted(p for p in TPL_DIR.glob("*.md") if not p.name.startswith("_"))

    if args.lista or not args.plantilla:
        print("Plantillas disponibles:\n")
        for p in plantillas:
            meta, _, _ = parse_template(p)
            print(f"  {p.stem:<18} {meta.get('type', '?'):<6} core {meta.get('core', '?')}")
        print("\nUso: python3 build_prompt.py <plantilla> [--video] [--var CLAVE=valor]")
        return

    path = TPL_DIR / f"{args.plantilla}.md"
    if not path.exists():
        sys.exit(f"No existe la plantilla '{args.plantilla}'. Prueba con --lista.")

    meta, values, sections = parse_template(path)

    for pair in args.var:
        if "=" not in pair:
            sys.exit(f"--var mal formado: '{pair}'. Formato: CLAVE=valor")
        k, v = pair.split("=", 1)
        values[k.strip().upper()] = v.strip()

    cores = load_cores()
    core_key = args.core or meta.get("core", "B")
    if core_key not in cores:
        sys.exit(f"No encuentro el CORE '{core_key}' en {CORE_FILE.name}")

    es_video = args.video or meta.get("type") == "video"

    partes = [cores[core_key], ""]
    cuerpo, faltan = substitute(sections.get("PROMPT", ""), values)
    partes.append(cuerpo)

    if es_video and "VIDEO" in sections:
        video, faltan_v = substitute(sections["VIDEO"], values)
        partes += ["", video]
        faltan = sorted(set(faltan) | set(faltan_v))

    if not args.sin_negativos:
        negs = load_negatives()
        pedidos = [n.strip() for n in meta.get("negatives", "NEG-IMG").split(",") if n.strip()]
        if es_video and "NEG-VID" not in pedidos:
            pedidos.append("NEG-VID")
        aplicados = [negs[n] for n in pedidos if n in negs]
        if aplicados:
            partes += ["", "Negative: " + ", ".join(aplicados)]

    print("\n".join(partes))

    if faltan:
        print(f"\n[aviso] variables sin valor: {', '.join(faltan)}", file=sys.stderr)


if __name__ == "__main__":
    main()
