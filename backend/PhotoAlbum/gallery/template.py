
class TemplateResponse:
    def __init__(self,status,error,message,body):
        self.status = status
        self.error = error
        self.message = message
        self.body = body

    def getResponse(self):
        return({
            "status":self.status,
            "error": self.error,
            "message": self.message,
            "body": self.body
        })
