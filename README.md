# sphinx-search

## Quick start

1. Move dataset to `datasets/plwiki.json`
2. Start containers \
`docker-compose up -d`
3. Install python dependencies \
`docker-compose run python bash -c "pip install PyMySQL"`
4. Index data \
`docker-compose run python bash -c "python /scripts/load-jsons.py"`

## Query sphinx

```bash
docker-compose exec mysql mysql -h sphinx -P 9306
```

## Example queries

```sql
SELECT j.id, j.title, weight()
FROM plwiki
WHERE MATCH('@(text) python');
```

```sql
SELECT
    j.title,
    j.datetime,
    weight()
FROM plwiki
WHERE
    MATCH('@(text) hybrydowy && @(title) toyota') AND
    j.datetime BETWEEN 1514764800 AND 1585440000
ORDER BY j.datetime DESC, j.title DESC
LIMIT 0,10;
```

## Perf test

```bash
docker-compose run python bash -c "python /scripts/run-multiple.py"
```
