#! /usr/bin/env python3

import click


@click.command()
@click.argument('sourcepath', type=click.Path(exists=True, readable=True, file_okay=True))
@click.argument('destpath', type=click.Path(exists=False, readable=False, file_okay=False))
def reverse_bytes(sourcepath, destpath):
    """Reverse the order of a file's bytes"""
    with open(sourcepath, 'rb') as sf:
        file_bytes = bytearray()
        file_bytes = sf.read()
        reversed_bytes = file_bytes[::-1]
        with open(destpath, 'wb') as df:
            df.write(reversed_bytes)


reverse_bytes()
