import json

from flask import Response

class APIError(Response):
    _base = {'success': False}
    def __init__(self, msg):
        self._base['message'] = msg
        kwargs = dict()
        kwargs['mimetype'] = 'application/json'
        kwargs['status'] = 400
        return super(APIError, self).__init__(
                json.dumps((self._base)), **kwargs)


MissingParameter = APIError('missing parameters')
InvalidData = APIError('invalid data')
DatabaseError = lambda err: APIError(str(err.__dict__['orig']))
CustomError = lambda msg: APIError(msg)
