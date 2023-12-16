from typing import cast

import redis


class RedisConnection:
    def __init__(self, host_name: str, port: int, db_index: int):
        """コンストラクタ

        Args:
            self (Self@RedisConnection): このクラス自身

            host_name (str): ホスト名

            port (int): ポート番号

            db_index (int): RedisのDBインデックス

        Returns:
        """
        self.__host_name = host_name
        self.__port = port
        self.__db_index = db_index
        self.__instance: redis.Redis | None = None

    def host_name(self) -> str:
        """ホスト名

        Args:
            self (Self@RedisConnection): このクラス自身

        Returns:
            str: ホスト名
        """
        return self.__host_name

    def port(self) -> int:
        """ポート番号

        Args:
            self (Self@RedisConnection): このクラス自身

        Returns:
            int: ポート番号
        """
        return self.__port

    def db_index(self) -> int:
        """RedisのDBインデックス

        Args:
            self (Self@RedisConnection): このクラス自身

        Returns:
            int: RedisのDBインデックス
        """
        return self.__db_index

    def instance(self) -> redis.Redis:
        """Redisのインスタンスを取得する

        Args:
            self (Self@RedisConnection): このクラス自身

        Returns:
            redis.Redis|None: Redisのインスタンス
        """
        if self.__instance is None:
            self.__instance = redis.Redis(host=self.host_name(), port=self.port(), db=self.db_index())
        return self.__instance


def get_redis_record(redis_connection: RedisConnection, key: str) -> str | None:
    """Redisからデータを取得する

    Args:

    Returns:
        str|None: 取得したデータもしくは存在しない場合はNone
    """
    redis_instance = redis_connection.instance()

    record = redis_instance.get(key)
    if record is None:
        return None
    else:
        return str(record)


def set_redis_record(redis_connection: RedisConnection, key: str, value: str, expires_seconds_after: int) -> bool:
    """Redisにデータを追加する

    Args:
        key (str): 追加するデータのキー。

        value (str): 追加するデータ本体。

        expires_seconds_after (int): データの生存期間。データが追加されてから、この秒数が経過すると自動的にRedisから削除される。

    Returns:
        bool: データの追加および生存期間の設定が正常にできたかどうか。true: 追加成功、false: 追加失敗
    """
    redis_instance = redis_connection.instance()

    # Redisに追加する
    redis_set_succeeded = redis_instance.set(
        name=key,
        value=value,
    )

    # 追加したデータに対して生存期間を設定する
    redis_expiration_set_succeeded = redis_instance.expire(name=key, time=expires_seconds_after)

    return bool(redis_set_succeeded) and bool(redis_expiration_set_succeeded)


def delete_redis_record(redis_connection: RedisConnection, key: str) -> int:
    """Redisのデータを削除する

    Args:
        key (str): 削除するデータのキー。

    Returns:
        int: 削除した件数
    """

    redis_instance = redis_connection.instance()
    redis_instance.delete(key)

    return cast(int, redis_instance.delete(key))


def purge_redis_records(redis_connection: RedisConnection) -> None:
    """Redisのデータをすべて消し飛ばす

    Args:

    Returns:
    """

    redis_instance = redis_connection.instance()
    redis_instance.flushdb()
