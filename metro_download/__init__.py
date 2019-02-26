import click
import datetime
import requests
from tqdm import tqdm


BASEURL = 'https://rm.metrolatam.com/pdf/'


def get_target(edition_date=datetime.datetime.now(), city='curitiba'):
    path = edition_date.strftime('%Y/%m/%d')
    prefix = edition_date.strftime("%Y%m%d")

    return f"{BASEURL}{path}/{prefix}_metro-{city}.pdf"


def download(target_url, location):
    filename = target_url.split('/')[-1]
    response = requests.get(target_url, stream=True)
    total_size = int(response.headers['Content-Length'])

    with open(location + '/' + filename, 'wb') as fd:
        for data in tqdm(iterable=response.iter_content(chunk_size=1024), total=total_size / 1024, unit='KB'):
            fd.write(data)

# TODO: set save location to a no dash argument: ie: metro_download -c spo /home/user/desktop
@click.command()
@click.option('-d', default='./', help='Save location.')
@click.option('-c', default='curitiba', help='City')
def cli(d, c):
    """
    Downloads Brazilian Metro Newspaper pdf.

    City:
    * sao-paulo
    * brasilia
    * abc
    * rio
    * campinas
    * curitiba <DEFAULT>
    * metrobh
    * portoalegre
    * espiritosanto
    * maringa


    """

    valid_cities = ('sao-paulo', 'brasilia', 'abc', 'rio', 'campinas',
                    'curitiba', 'metrobh', 'portoalegre', 'espiritosanto', 'maringa')

    if c not in valid_cities:
        click.echo('Error: Invalid City.')
        exit(1)

    edition = get_target(city=c)
    download(edition, d)
    click.echo('Done!')
