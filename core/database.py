from dataclasses import dataclass


@dataclass
class Resource:
    offset: int
    size: int
    kind: str
    description: str = ""
    references: list[int] | None = None


class ResourceDatabase:

    def __init__(self):
        self.resources = []

    def add(self, resource: Resource):
        self.resources.append(resource)

    def by_type(self, kind):
        return [r for r in self.resources if r.kind == kind]

    def __len__(self):
        return len(self.resources)