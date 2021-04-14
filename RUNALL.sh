python delitems.py
mkdir pages/
bash "pull data.sh"
python "convert to list.py"
bash swgohpages.sh
python "pullguildmembers.py"
python "group2teams.py"