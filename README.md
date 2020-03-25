# sphinx-search

## Quick start

`docker-compose up -d`
`docker-compose run python bash -c "pip install PyMySQL"`

## Index dataset

`docker-compose run python bash -c "python /scripts/load-jsons.py"`

## Query sphinx

`docker-compose exec mysql mysql -h sphinx -P 9306`

## Example queries

```sql
SELECT j.id, j.title, weight() FROM doj WHERE MATCH('@(title) toyota');
```

```sql
SELECT j.id, j.components, j.title, IN(j.components, 'Antitrust Division') AS ad, weight() FROM doj WHERE MATCH('toyota') AND ad = 1;
```

```sql
SELECT
    j.components,
    j.title,
    IN(j.components, 'Office of Public Affairs') + IN(j.components, 'Office of the Attorney General') AS ad,
    weight()
FROM doj
WHERE
    MATCH('@(contents) WASHINGTON && @(title) Justice') AND
    ad > 0 AND
    j.date BETWEEN 1233442800 AND 1235862000
ORDER BY j.contents DESC, j.title DESC
LIMIT 0,10;
```

## Perf test

`docker-compose run python bash -c "python /scripts/test.py"`
