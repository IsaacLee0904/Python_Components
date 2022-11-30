import click 

@click.command()
@click.option(
    '-p', '--port', 'port_account',
    help='all, amazon_TUS, amazon_TDC, amazon_Furniture',
    default='all',
    show_default=True
)

def main(port_account: str):
    print(f'type: {port_account}')

if __name__ == '__main__':
    main()

