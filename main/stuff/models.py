from random import randint

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

character_arr = ['Squirrel', 'The Wolf', 'Panda', 'The Turtle', 'The Bear', 'The Hare', 'The Fox', 'The Owl', 'Wild Boar', 'Deer', 'Sparrow', 'The Pigeon', 'Duck', 'The Nightingale', 'Jay', 'Magpie', 'The Seagull', 'The Cat', 'Pug', 'Shepherd dog', 'The Tiger', 'Leo', 'The Leopard', 'Chihuahua', 'Zebra', 'Behemoth', 'Crocodile', 'The Parrot', 'Peacock', 'Chameleon', 'The Wizard', 'Flower Fairy', 'The child', 'The Magician', 'The Frog', 'The Dragon', 'The Dinosaur', 'The Pirate', 'The robber', 'Doctor', 'Musician', 'Scientist', 'Chicken', 'The old woman', 'Heron', 'Athlete', 'The Traveler', 'Photographer', 'The Hero', 'The Ghost', 'The robot', 'Student', 'Programmer', 'Music lover', 'The Knight', 'The Princess', 'The King', 'You yourself', 'The painter', 'The Sailor', 'The Spider', 'Penguin', 'Hedgehog', 'Giraffe', 'Santa Claus', 'Your favorite literary character', 'Alpaca', 'Koala', 'The Sloth', 'Badger', 'Raccoon', 'The Dwarf', 'Meteorologist', 'Tour guide', 'Coach', 'Detective', 'Gamer', 'Blogger', 'The Monster', 'Scarecrow', 'Corgi', 'The Bull', 'Ostrich', 'Skateboarder', 'Kangaroo', 'The Shadow', 'The Doll', 'Snail', 'The Giant', 'The Snake', 'The Swordsman', 'Director of a large company', 'Seal', 'The Elf', 'Teacher', 'Octopus', 'The last person you spoke to', 'The Unicorn', 'Skydiver']
location_arr = ['Roof of the castle', 'The lighthouse', 'Garden', 'A small island', 'Kitchen', 'Classroom', 'Lake', 'Vegetable garden', 'The attic', 'Basement', 'Spiral staircase', 'The car', 'Railway station', 'Bus stop', 'The surface of the Moon', 'Shed roof', 'Library', 'Rainforest', 'Desert with cacti', 'Courtyard', 'In front of a skyscraper', 'The market', 'Cinema hall', 'Stationery store', 'Grocery store', 'Circus', 'Theater stage', 'Cafe', 'The top of the mountain', 'The bank of a full-flowing river', 'Bridge', 'Observation platform', 'Balcony', 'Field', 'The Barn', 'Snowdrift', 'The deck of the ship', 'Berth', 'Embankment', "The artist's workshop", 'Stadium', 'Gym', 'Bike path', 'Broad highway', 'Toy Store', 'Park bench', 'The Palace', 'Wasteland', 'Underground passage', 'The cabin of the aircraft', 'On the bus', 'In the parking lot', 'Bakery', 'Beauty salon', 'Tropical island', 'The Swamp', 'Long corridor', 'Laboratory', 'Art Gallery', 'Factory', 'Escalator', 'Ballroom', 'Bowling', 'Skating rink', 'Tree house', ' The top of a giant tree', 'Glade', 'A path in the forest', 'Sandy beach', 'Meadow with colorful flowers', 'Bamboo grove', 'Veranda', 'Observatory', 'An unknown planet', 'The city on a rainy night', 'Sports ground', 'Concert', 'In a comfortable chair', 'The living room of a medieval castle', 'Zoo', 'Bookstore', 'University', 'Office', 'Recording Studio', 'Ski slope', 'Workplace (desk)', 'The hollow of a huge tree', 'Telephone booth', 'Farm', 'The room that is being renovated', 'Country house', 'The Cave', "A city built from a children's construction kit", 'Sports goods store', 'The North Pole', 'Lighting equipment store', 'Pizzeria', 'Large cabinet', 'Tent', 'Autumn Forest']
detail_arr = ['Striped scarf', 'A jar of strawberry jam', 'Large mirror', 'Iron', 'Refrigerator', 'Table lamp', 'Bright clothes', 'A flower in a pot', 'Cookies', 'Electric kettle', 'Blanket', 'Thermos', 'Flashlight', 'Shooting Star', 'Garland', 'Paper airplane', 'Inflatable circle', 'Soft toy', 'Cherry', 'Pet', 'Microphone', 'Camera', 'Radio receiver', 'Bouquet of flowers', 'Cap', 'Backpack', 'Big bag', 'Sunglasses', 'Helmet', 'Photography', 'Ice cream', 'Cotton candy', 'Fancy shoes', 'A hat with a wide brim', 'Raincoat', 'A glass of juice', 'Fan', 'Gift', 'Guitar', 'The Flute', 'Drum', 'Sunflower', 'Telescope', 'Binoculars', 'Puzzle', 'The Globe', 'Pasta', 'Notebook', 'Rubber boots', 'Something brilliant', 'Something colorful', 'Hoop', 'Basketball ball', 'Amulet', 'Hours', 'Chamomile', 'Berries', 'Ivy', 'Ribbon', 'Letter', 'Headphones', 'Soap bubbles', 'Sheet music', 'Hood', 'Umbrella', 'A non-working magic wand', 'The Jug', 'Fragile vase', 'Scotch tape', 'Mirror', 'Tea', 'Glasses', 'Fireworks', 'Candle', 'Rose', 'Big cake', 'Colored shadow', 'Some kind of knitted thing', 'Lollipop', 'Straight lines', 'Confetti', 'Beads', 'Buttons', 'Something checkered', 'Something striped', 'Bricks', 'Something made of glass', 'Ray of light', 'Plaid', 'Pillow', 'Packaging paper', 'Package', 'Watering can', 'Map', 'Board game', 'Stickers for notes', 'The light bulb', 'Any emojis', 'Suitcase', 'Net']

class RandomCombination(models.Model):
    character = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)

def create_combi():
    character = character_arr[randint(0, 99)]
    location = location_arr[randint(0, 99)]
    detail = detail_arr[randint(0, 99)]
    combi = RandomCombination(character=character, location=location, detail=detail)
    combi.save()
    return combi


class UserUpload(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='user_uploads/', blank=True, null=True,)
    story = models.TextField(blank=True,)
    created = models.DateField(auto_now_add=True)


class UserProgress(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    month_year = models.CharField(max_length=6)
    days = models.CharField(max_length=100)
