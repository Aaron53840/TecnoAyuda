import re
import json
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text.strip())
    text = re.sub(r'-+', '-', text)
    return text

def extract_field(block, field, next_fields):
    pattern = r'{}:\s*(.*?)(?=\n\n(?:{})\s*:|\Z)'.format(
        re.escape(field), '|'.join(re.escape(f) for f in next_fields)
    )
    m = re.search(pattern, block, re.DOTALL)
    if not m:
        return ''
    return m.group(1).strip()

def split_items(text):
    if not text:
        return []
    parts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return parts

def main():
    with open('raw_kb.txt', encoding='utf-8') as f:
        raw = f.read()

    chunks = re.split(r'\nProblema #\d+\n', '\n' + raw)
    chunks = [c for c in chunks if c.strip()]
    
    # Validación de cantidad exacta esperada
    total_esperado = 301
    assert len(chunks) == total_esperado, f"Error: Se esperaban {total_esperado} problemas, pero se obtuvieron {len(chunks)}"

    fields_order = [
        'Título', 'Categoría', 'Sistema', 'Descripción',
        'Posibles causas', 'Solución paso a paso', 'Consejo',
        'Nivel de dificultad', 'Problemas relacionados', 'Palabras clave'
    ]

    problems = []
    used_slugs = set()
    total_chunks = len(chunks)

    for idx, block in enumerate(chunks, start=1):
        data = {}
        for i, field in enumerate(fields_order):
            next_fields = fields_order[i+1:]
            data[field] = extract_field(block, field, next_fields)

        titulo = data['Título'].strip()
        categoria = data['Categoría'].strip()
        sistema = data['Sistema'].strip()
        descripcion = data['Descripción'].strip()
        causas = split_items(data['Posibles causas'])
        pasos = split_items(data['Solución paso a paso'])
        consejo = data['Consejo'].strip()
        dificultad = data['Nivel de dificultad'].strip()
        relacionados_raw = data['Problemas relacionados'].strip()
        relacionados = [int(x) for x in re.findall(r'#(\d+)', relacionados_raw)]
        palabras_raw = data['Palabras clave'].strip()
        palabras = [p.strip() for p in palabras_raw.split(',') if p.strip()]

        # Validaciones de integridad obligatorias
        assert bool(titulo), f"Problema #{idx}: Título vacío"
        assert bool(categoria), f"Problema #{idx} ({titulo}): Categoría vacía"
        assert bool(sistema), f"Problema #{idx} ({titulo}): Sistema vacío"
        assert len(descripcion) >= 10, f"Problema #{idx} ({titulo}): Descripción demasiado corta o vacía"
        assert len(causas) > 0, f"Problema #{idx} ({titulo}): Sin causas especificadas"
        assert len(pasos) > 0, f"Problema #{idx} ({titulo}): Sin pasos de solución especificados"
        assert bool(dificultad), f"Problema #{idx} ({titulo}): Nivel de dificultad vacío"
        assert len(palabras) > 0, f"Problema #{idx} ({titulo}): Sin palabras clave"

        slug = slugify(titulo)
        base_slug = slug
        n = 2
        while slug in used_slugs:
            slug = f"{base_slug}-{n}"
            n += 1
        used_slugs.add(slug)

        problems.append({
            "id": idx,
            "slug": slug,
            "titulo": titulo,
            "categoria": categoria,
            "sistema": sistema,
            "descripcion": descripcion,
            "causas": causas,
            "pasos": pasos,
            "consejo": consejo,
            "dificultad": dificultad,
            "relacionados": relacionados,
            "palabras_clave": palabras
        })

    # Validación de problemas relacionados
    todos_los_ids = {p["id"] for p in problems}
    for p in problems:
        for rel_id in p["relacionados"]:
            assert rel_id in todos_los_ids, f"Problema #{p['id']} tiene relacionado #{rel_id} que no existe en el catálogo"

    # Validación de unicidad de slugs
    assert len(used_slugs) == total_chunks, f"Error: Hay slugs duplicados ({len(used_slugs)} != {total_chunks})"

    with open('data/problems.json', 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)

    print(f"Éxito: Se procesaron y validaron correctamente {len(problems)} problemas.")
    print(f"Primer problema (#{problems[0]['id']}): {problems[0]['titulo']} [{problems[0]['sistema']} - {problems[0]['categoria']}]")
    print(f"Último problema (#{problems[-1]['id']}): {problems[-1]['titulo']} [{problems[-1]['sistema']} - {problems[-1]['categoria']}]")

if __name__ == '__main__':
    main()
