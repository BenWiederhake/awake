#!/usr/bin/env python3

import hashlib
import hmac
import sys


PGP_WORDLIST = [
    'aardvark', 'adroitness',
    'absurd', 'adviser',
    'accrue', 'aftermath',
    'acme', 'aggregate',
    'adrift', 'alkali',
    'adult', 'almighty',
    'afflict', 'amulet',
    'ahead', 'amusement',
    'aimless', 'antenna',
    'Algol', 'applicant',
    'allow', 'Apollo',
    'alone', 'armistice',
    'ammo', 'article',
    'ancient', 'asteroid',
    'apple', 'Atlantic',
    'artist', 'atmosphere',
    'assume', 'autopsy',
    'Athens', 'Babylon',
    'atlas', 'backwater',
    'Aztec', 'barbecue',
    'baboon', 'belowground',
    'backfield', 'bifocals',
    'backward', 'bodyguard',
    'banjo', 'bookseller',
    'beaming', 'borderline',
    'bedlamp', 'bottomless',
    'beehive', 'Bradbury',
    'beeswax', 'bravado',
    'befriend', 'Brazilian',
    'Belfast', 'breakaway',
    'berserk', 'Burlington',
    'billiard', 'businessman',
    'bison', 'butterfat',
    'blackjack', 'Camelot',
    'blockade', 'candidate',
    'blowtorch', 'cannonball',
    'bluebird', 'Capricorn',
    'bombast', 'caravan',
    'bookshelf', 'caretaker',
    'brackish', 'celebrate',
    'breadline', 'cellulose',
    'breakup', 'certify',
    'brickyard', 'chambermaid',
    'briefcase', 'Cherokee',
    'Burbank', 'Chicago',
    'button', 'clergyman',
    'buzzard', 'coherence',
    'cement', 'combustion',
    'chairlift', 'commando',
    'chatter', 'company',
    'checkup', 'component',
    'chisel', 'concurrent',
    'choking', 'confidence',
    'chopper', 'conformist',
    'Christmas', 'congregate',
    'clamshell', 'consensus',
    'classic', 'consulting',
    'classroom', 'corporate',
    'cleanup', 'corrosion',
    'clockwork', 'councilman',
    'cobra', 'crossover',
    'commence', 'crucifix',
    'concert', 'cumbersome',
    'cowbell', 'customer',
    'crackdown', 'Dakota',
    'cranky', 'decadence',
    'crowfoot', 'December',
    'crucial', 'decimal',
    'crumpled', 'designing',
    'crusade', 'detector',
    'cubic', 'detergent',
    'dashboard', 'determine',
    'deadbolt', 'dictator',
    'deckhand', 'dinosaur',
    'dogsled', 'direction',
    'dragnet', 'disable',
    'drainage', 'disbelief',
    'dreadful', 'disruptive',
    'drifter', 'distortion',
    'dropper', 'document',
    'drumbeat', 'embezzle',
    'drunken', 'enchanting',
    'Dupont', 'enrollment',
    'dwelling', 'enterprise',
    'eating', 'equation',
    'edict', 'equipment',
    'egghead', 'escapade',
    'eightball', 'Eskimo',
    'endorse', 'everyday',
    'endow', 'examine',
    'enlist', 'existence',
    'erase', 'exodus',
    'escape', 'fascinate',
    'exceed', 'filament',
    'eyeglass', 'finicky',
    'eyetooth', 'forever',
    'facial', 'fortitude',
    'fallout', 'frequency',
    'flagpole', 'gadgetry',
    'flatfoot', 'Galveston',
    'flytrap', 'getaway',
    'fracture', 'glossary',
    'framework', 'gossamer',
    'freedom', 'graduate',
    'frighten', 'gravity',
    'gazelle', 'guitarist',
    'Geiger', 'hamburger',
    'glitter', 'Hamilton',
    'glucose', 'handiwork',
    'goggles', 'hazardous',
    'goldfish', 'headwaters',
    'gremlin', 'hemisphere',
    'guidance', 'hesitate',
    'hamlet', 'hideaway',
    'highchair', 'holiness',
    'hockey', 'hurricane',
    'indoors', 'hydraulic',
    'indulge', 'impartial',
    'inverse', 'impetus',
    'involve', 'inception',
    'island', 'indigo',
    'jawbone', 'inertia',
    'keyboard', 'infancy',
    'kickoff', 'inferno',
    'kiwi', 'informant',
    'klaxon', 'insincere',
    'locale', 'insurgent',
    'lockup', 'integrate',
    'merit', 'intention',
    'minnow', 'inventive',
    'miser', 'Istanbul',
    'Mohawk', 'Jamaica',
    'mural', 'Jupiter',
    'music', 'leprosy',
    'necklace', 'letterhead',
    'Neptune', 'liberty',
    'newborn', 'maritime',
    'nightbird', 'matchmaker',
    'Oakland', 'maverick',
    'obtuse', 'Medusa',
    'offload', 'megaton',
    'optic', 'microscope',
    'orca', 'microwave',
    'payday', 'midsummer',
    'peachy', 'millionaire',
    'pheasant', 'miracle',
    'physique', 'misnomer',
    'playhouse', 'molasses',
    'Pluto', 'molecule',
    'preclude', 'Montana',
    'prefer', 'monument',
    'preshrunk', 'mosquito',
    'printer', 'narrative',
    'prowler', 'nebula',
    'pupil', 'newsletter',
    'puppy', 'Norwegian',
    'python', 'October',
    'quadrant', 'Ohio',
    'quiver', 'onlooker',
    'quota', 'opulent',
    'ragtime', 'Orlando',
    'ratchet', 'outfielder',
    'rebirth', 'Pacific',
    'reform', 'pandemic',
    'regain', 'Pandora',
    'reindeer', 'paperweight',
    'rematch', 'paragon',
    'repay', 'paragraph',
    'retouch', 'paramount',
    'revenge', 'passenger',
    'reward', 'pedigree',
    'rhythm', 'Pegasus',
    'ribcage', 'penetrate',
    'ringbolt', 'perceptive',
    'robust', 'performance',
    'rocker', 'pharmacy',
    'ruffled', 'phonetic',
    'sailboat', 'photograph',
    'sawdust', 'pioneer',
    'scallion', 'pocketful',
    'scenic', 'politeness',
    'scorecard', 'positive',
    'Scotland', 'potato',
    'seabird', 'processor',
    'select', 'provincial',
    'sentence', 'proximate',
    'shadow', 'puberty',
    'shamrock', 'publisher',
    'showgirl', 'pyramid',
    'skullcap', 'quantity',
    'skydive', 'racketeer',
    'slingshot', 'rebellion',
    'slowdown', 'recipe',
    'snapline', 'recover',
    'snapshot', 'repellent',
    'snowcap', 'replica',
    'snowslide', 'reproduce',
    'solo', 'resistor',
    'southward', 'responsive',
    'soybean', 'retraction',
    'spaniel', 'retrieval',
    'spearhead', 'retrospect',
    'spellbind', 'revenue',
    'spheroid', 'revival',
    'spigot', 'revolver',
    'spindle', 'sandalwood',
    'spyglass', 'sardonic',
    'stagehand', 'Saturday',
    'stagnate', 'savagery',
    'stairway', 'scavenger',
    'standard', 'sensation',
    'stapler', 'sociable',
    'steamship', 'souvenir',
    'sterling', 'specialist',
    'stockman', 'speculate',
    'stopwatch', 'stethoscope',
    'stormy', 'stupendous',
    'sugar', 'supportive',
    'surmount', 'surrender',
    'suspense', 'suspicious',
    'sweatband', 'sympathy',
    'swelter', 'tambourine',
    'tactics', 'telephone',
    'talon', 'therapist',
    'tapeworm', 'tobacco',
    'tempest', 'tolerance',
    'tiger', 'tomorrow',
    'tissue', 'torpedo',
    'tonic', 'tradition',
    'topmost', 'travesty',
    'tracker', 'trombonist',
    'transit', 'truncated',
    'trauma', 'typewriter',
    'treadmill', 'ultimate',
    'Trojan', 'undaunted',
    'trouble', 'underfoot',
    'tumor', 'unicorn',
    'tunnel', 'unify',
    'tycoon', 'universe',
    'uncut', 'unravel',
    'unearth', 'upcoming',
    'unwind', 'vacancy',
    'uproot', 'vagabond',
    'upset', 'vertigo',
    'upshot', 'Virginia',
    'vapor', 'visitor',
    'village', 'vocalist',
    'virus', 'voyager',
    'Vulcan', 'warranty',
    'waffle', 'Waterloo',
    'wallet', 'whimsical',
    'watchword', 'Wichita',
    'wayside', 'Wilmington',
    'willow', 'Wyoming',
    'woodlark', 'yesteryear',
    'Zulu', 'Yucatan',
]


def encode_pgpwords(bytestring):
    """
    Takes a bytestring or byte-generator and produces a generator of
    words according to the PGP wordlist.
    """
    is_odd = False  # The zeroth byte will be even
    for b in bytestring:
        assert type(b) == int
        assert 0 <= b < 256
        yield PGP_WORDLIST[b * 2 + is_odd]
        is_odd = not is_odd  # The next byte will have opposite odd-ness


def biometric_mac(message, key):
    """
    Takes a message and a key as bytes,
    and outputs a "biometric" MAC for it, as a generator of strings.
    Formally, it computes:  PGP_wordlist(HMAC_SHA1(key, message))
    """
    assert type(key) == bytes
    assert type(message) == bytes

    signature_bin = hmac.new(key, message, hashlib.sha1).digest()
    return encode_pgpwords(signature_bin)


def run():
    if len(sys.argv) != 3:
        print('ERROR: You need to provide the two filenames.', file=sys.stderr)
        print('Usage: {} <KEYFILE> <MESSAGEFILE>'.format(sys.argv[0]), file=sys.stderr)
        print('Note that any and all whitespace is significant.', file=sys.stderr)
        exit(1)
    with open(sys.argv[1], 'rb') as fp:
        key = fp.read()
    with open(sys.argv[2], 'rb') as fp:
        message = fp.read()
    print('INFO: keylen={}, msglen={}'.format(len(key), len(message)), file=sys.stderr)
    print(' '.join(biometric_mac(message, key)))


if __name__ == '__main__':
    run()
