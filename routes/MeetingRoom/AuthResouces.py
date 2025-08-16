from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv

from schema.MeetingRoom.MeetingRoomAuth import LoginRequest
from service.MeetingRoom.AuthResourceService import AuthResourceService
auth_resourse = APIRouter()


@cbv(auth_resourse)
class AuthResourse:
    def __init__(self, authService: AuthResourceService = Depends()):
        self.authService=authService

    @auth_resourse.post("/Login")
    def register(self,payload: LoginRequest):
        try:
            username = payload.username.strip()
            password = payload.password.strip()
            return self.authService.authCheck(username,password)
        except HTTPException as e:
                raise e
       

       