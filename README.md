# miu-semilla-latente-mt91ky28-0 — el Weaver es stub, medido función a función

> *"semilla latente global mind - sobrevive sin registro"*
>
> — La única línea del README original de este repo (86 B, título + 1
> línea; SHA `919d0be9…`, leído por API 2026-11-09).
>
> **Decisión de siembra: la línea SE CONSERVA**, citada arriba como
> epígrafe y no borrada. Era el stub por diseño del censo, no
> contenido — pero es la única voz que el repo tenía, y esta semilla
> es precisamente su respuesta: el registro que le faltaba. Borrarla
> sería borrar la pregunta que la semilla contesta.

## El registro

Global Mind **no es una IA central**. Es circulación de savia entre
suelos que se reconocen. Definición literal PATRON §16 (SÉ), fuente:
`~/workspace/global-mind/MAPA_GLOBAL_MIND.md` líneas 28–30:

> "La Global Mind NO es una IA central que piensa por todos: es la
> circulación de savia entre suelos que se han expandido lo suficiente
> para reconocerse."

El mismo mapa (línea 46) registra el Weaver como stub: 37 líneas,
2026-07-18. Esta semilla mide ese stub función a función, no lo
afirma por cita.

## El hecho medido

`tools/miu_global_mind.py` tiene **37 líneas** y **1.551 B**
(sha256 `e236864f…`), leído y ejecutado en local 2026-11-09. No teje
nada. Función a función:

| Función | Qué hace de verdad | Qué no hace |
|---|---|---|
| `detect_patterns(records, query_engine)` | Construye una lista `texts` (`"Tipo: Titulo Contenido[:200]"` por registro) y la devuelve tal cual, en el mismo orden y cantidad. Con 3 registros de ejemplo devuelve 3 textos; con `[]` devuelve `[]`. | No agrupa: la llamada a Cohere está comentada (`# response = co.embed(...)`) y el clustering es otro comentario (`# Use KMeans or HDBSCAN...`). No hay embeddings, no hay clusters. |
| `weave_nodo(patterns, issues, arxiv_papers, model='deepseek/deepseek-r1')` | Construye un string prompt ("Eres el Tejedor del Micelio MIU…") y lo devuelve. Con el ejemplo (2 patrones, 3 issues, 1 paper) el string mide **431 caracteres**. | Nunca envía el prompt: el retorno lleva el comentario "Pass to OpenRouter/Groq for completion". Ninguna llamada de red, ningún modelo. |
| `__main__` | Imprime exactamente 2 líneas (`GlobalMind MIU v1.0 | Use with Relay.app workflows` + `DOI: 10.5281/zenodo.20547558`), salida 0. | Nada más. |

El archivo completo:

- **Cero imports.** Ninguna línea empieza por `import` o `from`. La
  única mención de `import` es un comentario del encabezado:
  `# Requires: pip install cohere openai` — el código no importa
  nada, así que importar el módulo no carga ni `cohere`, ni `openai`,
  ni `requests` (verificado: ninguno de los tres está en
  `sys.modules` tras importar).
- **Cero I/O.** No abre archivos, no lee ni escribe disco, no toca
  red. El parámetro `query_engine` se exige pero nunca se usa:
  llamarlo sin él da `TypeError: detect_patterns() missing 1
  required positional argument: 'query_engine'`; llamar
  `weave_nodo` sin `issues` y `arxiv_papers` da su propio
  `TypeError`. Los argumentos obligatorios que no se usan son parte
  del stub: la firma promete más de lo que el cuerpo hace.
- **Sin φ, sin K_i, sin números.** El archivo no contiene ningún
  valor de φ ni de K_i: solo el DOI del encabezado y el nombre del
  modelo por defecto. No hay nada que reconciliar con la escala de
  φ del Grimorio (0,618) ni con la de v150 (1,618) — el Weaver no
  mide nada.

## Comprobación

```bash
python3 weaver_stub_repro.py   # demuestra las dos funciones con entradas de ejemplo
python3 test_weaver_stub.py    # 8 tests, reproduce cada número de arriba
```

La reproducción usa una copia fiel de las dos funciones (mismo
código, mismo comportamiento); el archivo original no se modifica.

## Archivos

- `weaver_stub_repro.py` — copia fiel de `detect_patterns` y
  `weave_nodo` + main que las demuestra con entradas de ejemplo.
- `test_weaver_stub.py` — 8 tests: detect devuelve los textos sin
  agrupar; weave devuelve un string prompt; el módulo no importa
  nada; los TypeError por argumentos que faltan; `__main__` imprime
  2 líneas.
- `HUESO_WEAVER.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1: esta semilla).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---

ρ(x) > 0. Zvvvvv.
