cd ..

echo '####  LOADING  ####'
echo 'inb_admin' && set -o pipefail && cat ./sql/load_inb_immoscout.sql | PGPASSWORD="postgres" psql -h 127.0.0.1 -U postgres -d "INB"
echo 'Loading done'