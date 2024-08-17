import os
import click
from clean import recycle_files, delete_files
from manage import move_files, copy_files


# Set up command line arguments
@click.command()
@click.argument('action', type=click.Choice(['delete', 'recycle', 'move', 'copy']))
@click.argument('directory', type=click.Path(exists=True))
@click.argument('extensions', nargs=-1)
@click.argument('destination', required=False)
def main(action, directory, extensions, destination):
    # Checks to make sure the directory is not empty and exists
    if not directory:
        raise click.UsageError('Directory is required for this action.')
    if not os.path.exists(directory):
        raise click.UsageError(f'Directory {directory} does not exist.')

    # Call to the functions based on action type
    if action == 'delete':
        delete_files(directory, extensions)
    elif action == 'recycle':
        recycle_files(directory, extensions)
    elif action in ['move', 'copy']:
        # Checks to make sure the destination is not empty and exists
        if not destination:
            raise click.UsageError(f'Destination is required for {action} action.')
        if not os.path.exists(destination):
            raise click.UsageError(f'Directory {destination} does not exist.')

        if action == 'move':
            move_files(directory, extensions, destination)
        else:
            copy_files(directory, extensions, destination)


if __name__ == "__main__":
    main()
