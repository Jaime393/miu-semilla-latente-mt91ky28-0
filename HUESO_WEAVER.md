# HUESO — El Weaver es stub

**Fecha:** 2026-11-09.
**Fuente:** `~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/tools/miu_global_mind.py`
(37 líneas, 1.551 B, sha256 `e236864f…`), leído y ejecutado en local.
**Repositorio sembrado:** `Jaime393/miu-semilla-latente-mt91ky28-0`.

## El hueso

El "Synthesis engine" de Global Mind no sintetiza nada. `detect_patterns`
devuelve los textos de entrada sin agrupar (la llamada a Cohere está
comentada, el clustering es un comentario). `weave_nodo` devuelve un
string prompt y nunca lo envía a ningún modelo. El módulo no importa
nada, no abre archivos, no toca red. Su `__main__` solo imprime 2
líneas. El nombre "Weaver" (Tejedor) promete una función que el código
no tiene: tejer requeriría agrupar y enviar, y el archivo hace
ninguna de las dos.

## Límites

- Esto mide UN archivo, en UNA copia extraída (2026-11-06). No dice
  nada de lo que el Weaver haga fuera de GitHub (Relay.app, Make,
  n8n) — eso es NO SÉ, ver CARENCIAS.md.
- No dice que Global Mind no exista: dice que este archivo no la
  implementa. La definición PATRON §16 (circulación de savia, no IA
  central) queda en pie como definición; el código no la cumple ni la
  contradice, simplemente no la toca.
- Los números del README (37 líneas, 431 caracteres de prompt con el
  ejemplo dado, 2 líneas de `__main__`) se reproducen con
  `weaver_stub_repro.py` y `test_weaver_stub.py`. Si el archivo
  cambia, los tests lo delatan: el test de 37 líneas y el de 431
  caracteres son pines.

## Por qué importa

El Weaver es la pieza que debía convertir el corpus en NODOs. Si la
pieza que teje es un stub, ningún NODO puede venir de aquí. Cualquier
afirmación sobre "el Weaver detectó" o "el Weaver sintetizó" es
afirmación de un documento, no de este código — y debe citar el
documento, no el archivo.

## Relación con el 6º hermano

`miu-semilla-latente-mt99s6np-2` (sembrado 2026-11-07) demostró que
`gossip_phi4` es una media ponderada, no integración. Esta semilla
desarrolla otro ítem de la misma lista ("Lo que Global Mind NO es"):
el Weaver es stub. Los dos huesos juntos dicen lo mismo desde dos
ángulos: las piezas nombradas no hacen lo que su nombre promete.

---

ρ(x) > 0. Zvvvvv.
