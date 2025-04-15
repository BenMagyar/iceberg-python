def model_serializer(func):
    func._is_model_serializer = True
    return func

def apply_model_serializer(cls):
    for attr in dir(cls):
        method = getattr(cls, attr)
        if getattr(method, "_is_model_serializer", False):
            def _dict(self, *args, **kwargs):
                return method(self)
            def _json(self, *args, **kwargs):
                import json
                return json.dumps(method(self))
            cls.dict = _dict
            cls.json = _json
            break
    return cls