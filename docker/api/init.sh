chmod 755 ./docker/api/wait-for-it.sh
poetry lock
poetry install
bash ./docker/api/wait-for-it.sh db:1836

alembic upgrade head

echo "http://localhost:1019/docs"
uvicorn app.main:app --host 0.0.0.0 --port 1019 --reload
