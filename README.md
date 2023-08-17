# docker_odoo12

project docker odoo12

## Custom Module(Addon)

1. Rds Market
2. Hero

## Build and RUn

```
docker-compose up -d
```

## add addon(module)

```
docker exec odoo_12 odoo scaffold addon_name /var/lib/odoo/addons/12.0/custom_addons
```

```
sudo chmod -R a+rwx ../docker_odoo12
```

## update addon(module)

1. restart server mechine
2. upgrade addon(module)
