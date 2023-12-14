import typer

from .terminal import Terminal

cli = typer.Typer('Terminal for language models')

terminal = Terminal()

@cli.command()
def serve(port: int = typer.Option(..., help="The port to serve on")):
    terminal.serve(port)

@cli.command()
def cli():
    terminal.cli()

if __name__ == "__main__":
    cli()
