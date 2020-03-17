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
SELECT j.id, j.components, j.title, IN(j.components, 'Antitrust Division') AS ad, weight() FROM doj WHERE MATCH('toyota') AND ad = 1;
```

## Perf test

`docker-compose run python bash -c "python /scripts/test.py"`
