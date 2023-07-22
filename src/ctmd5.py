"""a cli tool used to change the MD5 of files"""
import hashlib
import random
import string

import click
from _version import __version__

CHARACTERS = string.ascii_letters + string.digits


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("-s", "--show", is_flag=True, help="show the md5 value. (When the file is large, it will take a long time.)")
@click.version_option(version=__version__)
def cli(file, show):
    """A CLI tool used to change the MD5 of files"""
    if show:
        click.echo(f"before md5: {get_md5(file)}")
    change_the_md5(file=file)
    if show:
        click.echo(f"after md5: {get_md5(file)}")


def get_md5(file: str) -> str:
    """计算文件的MD5值。

    Args:
        file (str): 文件路径。

    Returns:
        str: 文件的MD5值。
    """
    md5 = hashlib.md5()
    with open(file, "rb") as f:
        while True:
            buffer = f.read(4096)
            if not buffer:
                break
            md5.update(buffer)
    return md5.hexdigest()


def change_the_md5(file: str) -> None:
    """更改文件的MD5值。

    Args:
        file (str): 要更改MD5值的文件路径。

    Returns:
        None
    """
    random_str = "".join(random.choice(CHARACTERS))
    with open(file, "ab") as f:
        f.write(random_str.encode("utf-8"))
    click.echo(f"The file[{click.format_filename(file)}] md5 value has been changed.")


if __name__ == "__main__":
    cli()
