# @pytest.fixture(scope="session")
# def event_loop() -> AbstractEventLoop:
#     return asyncio.get_event_loop()


# @pytest_asyncio.fixture(scope="session")
# async def init_db() -> None:
#     async def _create_db() -> None:
#         async with async_engine.begin() as conn:
#             await conn.run_sync(BaseModel.metadata.create_all)

#     app.dependency_overrides[get_session] = get_test_session
#     await drop_test_database()
#     await create_test_database()
#     await _create_db()


# @pytest_asyncio.fixture(scope="session")
# async def init_db_data() -> None:
#     csv_files: list = []
#     data_mapping.items()
#     mapping = {k: v for k, v in data_mapping.items() if k in csv_files}

#     async with session_factory().begin() as s:
#         await register_fixtures_with_mapping(s.session, mapping)
#         await s.commit()


# @pytest_asyncio.fixture(scope="session", autouse=True)
# async def init(init_db: None, init_db_data: None) -> None:
#     return


# @pytest_asyncio.fixture(scope="function", autouse=True)
# async def session() -> AsyncGenerator:
#     async with session_factory().begin() as s:
#         yield s.session
#         await reset_sequence(s.session)
#         await s.rollback()
#     await session_factory.remove()


# @pytest.fixture(scope="module")
# def anyio_backend() -> str:
#     return "asyncio"


# @pytest_asyncio.fixture(scope="module")
# async def client() -> AsyncGenerator:
#     async with LifespanManager(app):
#         async with AsyncClient(app=app, base_url="http://test") as c:
#             yield c


# @pytest.fixture(scope="function", autouse=True)
# def reset_factory_boy_sequences() -> None:
#     for factory in inspect.getmembers(factories, inspect.isclass):
#         factory[1].reset_sequence()
