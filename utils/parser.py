from cpymad.madx import Madx


class Parser():

    def generate_ring_data(file):
        madx = Madx()
        madx.call(file = 'booster.madx')
