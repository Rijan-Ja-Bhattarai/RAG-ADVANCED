from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct, Distance

class Qdrant_Storage:
    def __init__(self, url = "http://localhost:6333",collection = "docx", dim = 2048):
        self.client = QdrantClient(url=url, timeout=30)
        self.collection = collection
        
        if not self.client.collection_exits(self.collection):
            self.client.create_collection(
                collection_name = self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
            )
            