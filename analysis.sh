#! /bin/bash
echo "\nVirtual environment activated"
pip install -r requirements.txt
echo "\nThis is for AudioApp Application"
pylint --load-plugins pylint_django AudioApp
echo "\nThis is for Valet Staticmanagement Application"
pylint --load-plugins pylint_django Static_Management
python3 manage.py test