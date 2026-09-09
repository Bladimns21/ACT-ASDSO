def serialize_row(row):
    """Convierte campos datetime/date a string y decimal a float para serialización JSON segura."""
    if not row:
        return row
    d = dict(row)
    for k, v in d.items():
        if hasattr(v, 'isoformat'):
            d[k] = v.isoformat()
        elif hasattr(v, '__float__') and not isinstance(v, (int, float, bool)):
            d[k] = float(v)
    return d

def serialize_rows(rows):
    """Serializa una lista o tupla de registros."""
    if not rows:
        return []
    return [serialize_row(r) for r in rows]
