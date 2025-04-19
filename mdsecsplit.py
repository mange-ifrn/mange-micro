#!/usr/bin/env python

import argparse
from pathlib import Path

from slugify import slugify

parser: argparse.ArgumentParser = argparse.ArgumentParser('Separa seções de arquivo Markdown')
parser.add_argument('arquivo', help='Arquivo no formato Markdown')
args: argparse.Namespace = parser.parse_args()

fpath: Path = Path(args.arquivo)
if fpath.exists() and fpath.is_file():
    with fpath.open(mode='r', encoding='utf-8') as arq:
        titulo: str = arq.readline()
        while titulo and not titulo.startswith('# '):
            titulo = arq.readline()

        secoes = arq.read().split('\n## ')

        docs_path: Path = fpath.parent / 'docs'
        docs_path.mkdir(exist_ok=True, parents=True)
        idx_path: Path = docs_path/'index.md'
        with idx_path.open(mode='w', encoding='utf-8') as arq_idx:
            arq_idx.write(titulo)
            arq_idx.write(secoes[0])

        arqs_secoes = []
        for sec in secoes[1:]:
            titulo,conteudo = sec.split('\n', maxsplit=1)
            slug_titulo = slugify(titulo)
            fname = f'{slug_titulo}.md'
            arqs_secoes.append(fname)
            fsec_path = docs_path / f'{fname}'
            with fsec_path.open(mode='w', encoding='utf-8') as arq_sec:
                arq_sec.write(f'# {titulo}')
                arq_sec.write(conteudo)

        print(f'  - {"\n  - ".join(arqs_secoes)}')
