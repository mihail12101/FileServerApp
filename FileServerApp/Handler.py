import json

from aiohttp import web

from FileServerApp.file_services import FileService, FileServiceSigned


class Handler:
    def __init__(self):
        self.file_service = FileService()
        self.file_service_signed = FileServiceSigned()

    async def get_file_list(self, *args) -> web.Response:
        try:
            files = await self.file_service.get_files()
        except Exception as e:
            raise web.HTTPBadRequest(text=str(e))

        return web.json_response(data={
            "status": 'success',
            "data": files
        })

    async def get_file_data(self, request: web.Request, *args) -> web.Response:

        file_name = request.rel_url.query['filename']
        try:
            file_data = await self.file_service.get_metadata(file_name)
        except Exception as e:
            raise web.HTTPBadRequest(text=str(e))

        return web.json_response(data={
            "status": 'success',
            "data": file_data
        })

    async def create_file(self, request: web.Request, *args) -> web.Response:

        try:
            result = await self.parse_request_content_from_stream(request)
            content = result.get("content")
            file_name = await self.file_service.create_file(content)
        except Exception as e:
            raise web.HTTPBadRequest(text=str(e))

        return web.json_response(data={
            "status": 'success',
            "data": await self.file_service.get_metadata(file_name)
        })

    async def delete_file(self, request: web.Request, *args) -> web.Response:

        file_name = request.match_info['file_name']

        try:
            await self.file_service.delete_file(file_name)
            return web.json_response(data={
                "status": 'success',
                "message": f"File {file_name} was removed"
            })
        except Exception as e:
            raise web.HTTPBadRequest(text=str(e))

    async def change_work_dir(self, request: web.Request, *args) -> web.Response:
        try:
            result = await self.parse_request_content_from_stream(request)
            new_path = result.get("new_path")
            await self.file_service.change_work_dir(new_path)
            return web.json_response(data={
                "status": 'success',
                "message": f"Work directory switched to {new_path}"
            })
        except Exception as e:
            raise web.HTTPBadRequest(text=str(e))

    @staticmethod
    async def parse_request_content_from_stream(request):
        stream = request.content

        result = ""
        while not stream.at_eof():
            line = await stream.read()
            result += line.decode("utf-8")

        return json.loads(result)

