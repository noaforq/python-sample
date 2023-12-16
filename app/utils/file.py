import asyncio
import datetime
import os
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from google.cloud import storage

from app.configs import BASE_DIR, STATIC_DIR, STATIC_URL, settings

CLOUD_STORAGE_URL = "https://storage.googleapis.com"


async def upload_file(file: UploadFile, directory: str, private: bool = False) -> str:
    # TODO: 非同期対応する
    await asyncio.sleep(0)
    directory = directory.strip("/")
    if settings.use_cloud_storage:
        return _upload_file_cloud_storage(file, directory, private)
    else:
        return _upload_file_local(file, directory)


def _upload_file_cloud_storage(file: UploadFile, directory: str, private: bool = False) -> str:
    client = storage.Client()
    bucket = client.bucket(settings.cloud_storage_private_bucket if private else settings.cloud_storage_public_bucket)

    filename = _get_filename(file.filename)
    blob = bucket.blob(f"{directory}/{filename}")

    blob.upload_from_string(file.file.read(), content_type=file.content_type)

    if not private:
        blob.make_public()

    return blob.public_url


def _upload_file_local(file: UploadFile, directory: str) -> str:
    filename = _get_filename(file.filename)
    dir_path = f"{BASE_DIR}/{STATIC_DIR}/{directory}"
    file_path = f"{BASE_DIR}/{STATIC_DIR}/{directory}/{filename}"
    url_path = f"{settings.server_url}/{STATIC_URL}/{directory}/{filename}"

    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return url_path


def _get_filename(filename: str) -> str:
    return f"{os.path.splitext(filename)[0]}{uuid4()}{os.path.splitext(filename)[1]}"


async def delete_file(url_file: str, private: bool = False) -> None:
    await asyncio.sleep(0)
    if settings.use_cloud_storage:
        _delete_file_cloud_storage(url_file, private)
    else:
        _delete_file_local(url_file)


def _delete_file_local(url_file: str) -> None:
    link_file = url_file.replace(f"{settings.server_url}", f"{BASE_DIR}")
    if os.path.isfile(link_file):
        copied_file = Path(link_file)
        copied_file.unlink()


def _delete_file_cloud_storage(url_file: str, private: bool = False) -> None:
    client = storage.Client()
    bucket = client.bucket(settings.cloud_storage_private_bucket if private else settings.cloud_storage_public_bucket)

    blob_name = url_file.replace(f"{CLOUD_STORAGE_URL}/{bucket.name}/", "")
    blob = bucket.blob(blob_name)
    blob.delete()


async def get_signature_url(private_url: str) -> str:
    """private_urlから署名付きURLを取得"""
    await asyncio.sleep(0)
    if settings.use_cloud_storage:
        return _get_signature_url_cloud_storage(private_url, settings.chat_file_download_url_expiration_minutes)
    else:
        return private_url


def _get_signature_url_cloud_storage(private_url: str, expiration_minutes: int) -> str:
    client = storage.Client()
    bucket = client.bucket(settings.cloud_storage_private_bucket)

    blob_name = private_url.replace(f"{CLOUD_STORAGE_URL}/{bucket.name}/", "")
    blob = bucket.blob(blob_name)
    url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=expiration_minutes),
        method="GET",  # Allow GET requests using this URL.
    )
    return url


async def upload_file_judge(file: UploadFile, directory: str) -> str:
    """
    ジャッジの事前配置ファイルをアップロード
    """
    # TODO: 非同期対応する
    await asyncio.sleep(0)
    directory = directory.strip("/")
    if settings.use_cloud_storage:
        return _upload_file_cloud_storage_judge(file, directory)
    else:
        return _upload_file_local_judge(file, directory)


def _upload_file_cloud_storage_judge(file: UploadFile, directory: str) -> str:
    """
    ジャッジのprivateバケットに事前配置ファイルをアップロード
    """
    client = storage.Client()
    bucket = client.bucket(settings.cloud_storage_private_judge_bucket)
    filename = _get_filename(file.filename)
    blob = bucket.blob(f"{directory}/{filename}")
    blob.upload_from_string(file.file.read(), content_type=file.content_type)

    return blob.public_url


def _upload_file_local_judge(file: UploadFile, directory: str) -> str:
    """
    ジャッジの事前配置ファイルのローカルアップロード
    """
    filename = _get_filename(file.filename)
    dir_path = f"{BASE_DIR}/{STATIC_DIR}/{directory}"
    file_path = f"{BASE_DIR}/{STATIC_DIR}/{directory}/{filename}"
    url_path = f"{settings.server_url}/{STATIC_URL}/{directory}/{filename}"

    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return url_path
