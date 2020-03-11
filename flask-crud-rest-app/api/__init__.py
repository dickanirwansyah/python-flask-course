from flask_restful import Api
from app import flaskAppInstance
from .Task import Task
from .TaskById import TaskById

restServer = Api(flaskAppInstance)

restServer.add_resource(Task, "/api/v1.0/task")
restServer.add_resource(TaskById, "/api/v1.0/task/id/<string:taskId>")