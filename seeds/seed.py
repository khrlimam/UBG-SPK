from seeds.Seeders import DataSeeder

seeders = [DataSeeder()]


def start():
    for seeder in seeders:
        seeder.run()
