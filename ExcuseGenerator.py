import random

excuses_list = [
    'I am taking a shower.',
    'I am taking a dump.',
    'my internet is so bad I can\'t even see your messages.',
    'there is a killer clown waiting for me outside.',
    'I might overdose on vitamin D.'
]
excuses_prefix = [
    'Sorry,',
    'I apologize butt',
    'My bad,',
    'This is so embarrassing, but',
    'This sucks but,',
]
random_excuse = random.randint(0, 4)
random_excuse2 = random.randint(0, 4)
print(excuses_prefix[random_excuse2] + ' I cannot go out because ' + excuses_list[random_excuse])
