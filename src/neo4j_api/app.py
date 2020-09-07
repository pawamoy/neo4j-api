"""FastAPI app."""

from typing import Optional

import importlib_metadata
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Neo4J API", description="A personal API for Neo4J.", version=importlib_metadata.version("neo4j-api")
)


class Node(BaseModel):
    labels: List[str]
    properties: Dict[str, Any]


@app.get("/nodes")
async def get_nodes(labels: Optional[str] = None,) -> List[Node]:
    pass


@app.get("/nodes/{node_id}")
async def get_node(node_id: int):
    pass


@app.post("/nodes")
async def create_node(labels: List[str], properties: Dict[str, Any]) -> Node:
    pass


# add a person with properties
# add a todo item
# add a gift idea linked to a person
