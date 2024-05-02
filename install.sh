if ! command -v python3 &> /dev/null; then echo "python3 missing"; exit 1; fi
if ! command -v pip3 &> /dev/null; then echo "pip3 missing"; exit 1; fi

python3 -m pip install --upgrade pip > /dev/null

pip install black > /dev/null
pip install pipreqs > /dev/null

# dev: update list of dependencies
rm -rf requirements.txt > /dev/null
pipreqs . > /dev/null

# prod: install list of dependencies
pip install -r requirements.txt > /dev/null

# run
python3 ./src/julia.py --size 155 --nprocs 12 --benchmark
