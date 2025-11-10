class Base:
    def _make_url(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
    def _prepare(self, **kwargs): ...
    def _parse(self, resp): ...

class Client(Base):
    def __init__(...): self._c = httpx.Client(...)
    def request(...): resp = self._c.request(...); return resp
    

class AsyncClient(Base):
    def __init__(...): self._c = httpx.AsyncClient(...)
    async def request(...): resp = await self._c.request(...); return resp

# короче в транспорте реализацию а тут просто обертку :)