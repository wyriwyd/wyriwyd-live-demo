import argparse

dragon_names = [
    'Aido',
    'Apalala',
    'Apophis',
    'Azazel',
    'Qinglong',
    'Boitatá',
    'Fafnir',
    'Erenkyl',
    'Erensuge',
    'Guivres',
    'Huanglong',
    'Jörmungandr',
    'Knucker',
    'Kur',
    'Illuyankas',
    'Ikuchi',
    'Kukulkan',
    'Ladon',
    'Leviathan',
    'Mushussu',
    'Ouroboros',
    'Orochi',
    'Quetzalcoatl',
    'Ryūjin',
    'Sárkány',
    'Tiamat',
    'Zirnitra',
    'Motrax',
    'Maleficient'
    'Athron',
    'Khoth']

def dragon_name(name):
    num = sum([ord(c) for c in name])
    i = num % len(dragon_names)
    return dragon_names[i]

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('name', type=str)
    parser.add_argument('-b', '--backwards', action='store_true')

    args = parser.parse_args()

    dname = dragon_name(args.name)

    if args.backwards:
        dname = dname[::-1].capitalize()

    print("Your dragon name is: {}".format(dname))

if __name__ == '__main__':
    main()
