#! /bin/bash
cd /app/
sed -i "s/db_master_host/${db_master_host}/g" /app/.env
sed -i "s/db_master_port/${db_master_port}/g" /app/.env
sed -i "s/db_master_user/${db_master_user}/g" /app/.env
sed -i "s/db_master_password/${db_master_password}/g" /app/.env
sed -i "s/db_master_name/${db_master_name}/g" /app/.env

cd /app/
python manage.py runserver 0.0.0.0:5034
