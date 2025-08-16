
from fastapi import HTTPException
from database.dataBase_Initializer import Meetingroom_collection

class MeetingRoomRepository:
    def __init__(self):
        self.meetingroom_collection = Meetingroom_collection

    def get_buildings(self,cluster_id: str):
        document = self.meetingroom_collection.find_one(
            {"Cluster_ID": cluster_id},
            {"_id": 0, "Buildings": 1} 
        )

        return document

    def get_timeslots(self,cluster_id: str):
        document = self.meetingroom_collection.find_one({"Cluster_ID": cluster_id})
        return document
        