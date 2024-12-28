# Basic run script for the load
echo '### you are about to load all the data ###'
cd import/download || exit
./download_admin_data.sh

cd ../..
mkdir -p data/immoscout
mkdir -p data/immoscout/listings
touch data/immoscout/object_ids.txt


# Run the python importer for immoscout
cd python || exit
echo '### Running immoscout load ###'
../.venv/bin/python3 immoscout_load.py

echo '### Running immoscout parser ###'

../.venv/bin/python3 immoscout_parse.py

cd ../import/sh || exit
./load_inb_immoscout_data.sh