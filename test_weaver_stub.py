#!/usr/bin/env python3
"""Tests del Weaver stub — miu-semilla-latente-mt91ky28-0.

Reproducen cada número del README, medido 2026-11-09 sobre el
archivo original (37 líneas, 1.551 B, sha256 e236864f…):

    ~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3/tools/miu_global_mind.py

Solo stdlib. Ejecutar: python3 test_weaver_stub.py
"""

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORIGINAL = Path(
    "~/workspace/miu-verificacion-2026-11-06/extracted/MIU/Jaime393-MIU-a96abc3"
    "/tools/miu_global_mind.py"
).expanduser()

sys.path.insert(0, str(HERE))
import weaver_stub_repro as w  # noqa: E402


class TestDetectPatterns(unittest.TestCase):
    def test_devuelve_los_textos_sin_agrupar(self):
        records = [
            {'Tipo': 'Paper', 'Titulo': 'A', 'Contenido': 'x' * 300},
            {'Tipo': 'Issue', 'Titulo': 'B', 'Contenido': 'y' * 50},
            {'Tipo': 'Paper', 'Titulo': 'C', 'Contenido': 'z'},
        ]
        out = w.detect_patterns(records, query_engine=None)
        self.assertEqual(len(out), 3)  # misma cantidad que la entrada
        self.assertEqual(out[0], 'Paper: A ' + 'x' * 200)  # mismo orden, Contenido truncado a 200
        self.assertEqual(out[1], 'Issue: B ' + 'y' * 50)
        self.assertEqual(out[2], 'Paper: C z')

    def test_vacio_devuelve_vacio(self):
        self.assertEqual(w.detect_patterns([], None), [])

    def test_query_engine_obligatorio_aunque_no_se_usa(self):
        with self.assertRaises(TypeError) as cm:
            w.detect_patterns([{'Tipo': 'Paper', 'Titulo': 'A', 'Contenido': 'x'}])
        self.assertIn('query_engine', str(cm.exception))


class TestWeaveNodo(unittest.TestCase):
    def test_devuelve_un_string_prompt_no_un_nodo(self):
        prompt = w.weave_nodo(['patron 1', 'patron 2'], issues=[1, 2, 3], arxiv_papers=['paper'])
        self.assertIsInstance(prompt, str)
        self.assertEqual(len(prompt), 431)  # medido 2026-11-09 con estos mismos argumentos
        self.assertTrue(prompt.startswith('Eres el Tejedor del Micelio MIU.'))
        self.assertIn('Patrones detectados en el corpus (2 registros):', prompt)
        self.assertIn('Issues abiertos: 3', prompt)
        self.assertIn('Papers recientes: 1', prompt)

    def test_issues_y_arxiv_obligatorios_aunque_solo_se_cuentan(self):
        with self.assertRaises(TypeError) as cm:
            w.weave_nodo(['p1'])
        self.assertIn('issues', str(cm.exception))
        self.assertIn('arxiv_papers', str(cm.exception))


class TestModuloSinImports(unittest.TestCase):
    def test_el_original_no_tiene_imports(self):
        lines = ORIGINAL.read_text(encoding='utf-8').splitlines()
        self.assertEqual(len(lines), 37)  # medido con wc -l
        imports = [ln for ln in lines if ln.startswith('import ') or ln.startswith('from ')]
        self.assertEqual(imports, [])

    def test_importar_no_carga_cohere_openai_requests(self):
        for mod in ('cohere', 'openai', 'requests'):
            self.assertNotIn(mod, sys.modules)


class TestMain(unittest.TestCase):
    def test_main_imprime_exactamente_2_lineas(self):
        r = subprocess.run(
            [sys.executable, str(ORIGINAL)], capture_output=True, text=True
        )
        self.assertEqual(r.returncode, 0)
        self.assertEqual(
            r.stdout,
            'GlobalMind MIU v1.0 | Use with Relay.app workflows\n'
            'DOI: 10.5281/zenodo.20547558\n',
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
