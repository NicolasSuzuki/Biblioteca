from ui.cli import CLI
from services.library_facade import LibraryFacade
from utils.library_mediator import LibraryMediator

def main():
    library_facade = LibraryFacade()
    library_mediator = LibraryMediator(library_facade)

    cli = CLI(library_mediator)
    cli.run()

if __name__ == "__main__":
    main()