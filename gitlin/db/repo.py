from pysondb import db
from typing import List,Dict

repo_db = db.getDb('repo.db',log=True)

# implement your oprations on db as functions in here

schema: Dict[str,int] = {
    "repo_id": 0,
    "chat_id": 0,
    "topic_id": 0
}

def addData(s: schema):
    repo_db.add(s)

def getRepoDetail(repo: int) -> List[Dict]:
    q = {"repo_id":repo}
    return repo_db.getByQuery(q)
