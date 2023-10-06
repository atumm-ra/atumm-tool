from atumm.core.types import Command, CommandUseCaseSync
from atumm.tool.domain.utils import create_module


class AddRestResourceCommand(Command):
    service_name: str
    resource_name: str


class AddRestResourceUseCase(CommandUseCaseSync[AddRestResourceCommand]):

    def execute(self, command: AddRestResourceCommand):
        """
        Create a new REST resource with the given service and resource names.
        """
        base_path = f"thisapp/services/{command.service_name}/entrypoints/rest/{command.resource_name}"
    
        modules = [
            (
                "",
                [
                    "controllers.py",
                    "presenters.py",
                    "responses.py",
                    "routers.py",
                ],
            ),
        ]
    
        for module, files in modules:
            create_module(f"{base_path}/{module}", files)

