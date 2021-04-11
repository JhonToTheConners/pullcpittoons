python delitems.py
mkdir pages/
bash "pull data.sh"
python "convert to list.py"
bash swgohpages.sh
python "pullguildmembers.py"
"C:\Program Files (x86)\Notepad++\notepad++.exe" guildroster.txt
