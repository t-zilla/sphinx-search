# sphinx-search

## Quick start

`docker-compose up -d`

## Load dataset

`docker-compose exec mysql bash -c "mysql -proot stackoverflow < /scripts/load-dataset.sql"`

## Index dataset

`docker-compose run sphinx sh -c "indexer -c /opt/sphinx/conf/sphinx.conf --all"`
