from flask_restful import Resource
import logging as logger

class TaskById(Resource):

    def get(self, taskId):
        logger.debug("inside method get by id")
        return {"message" : "inside method get by id TASK-ID={} ".format(taskId)},200

    def post(self, taskId):
        logger.debug("inside method post by id")
        return {"message" : "inside method post by id TASK-ID={}".format(taskId)},200

    def put(self, taskId):
        logger.debug("inside method put by id")
        return {"message" : "inside method put by id TASK-ID={}".format(taskId)},200

    def delete(self, taskId):
        logger.debug("inside method delete by id")
        return {"message" : "inside method delete by id TASK-ID={}".format(taskId)},200