# Testing module for Heart Rate Game

import heart_rate_game

def test_plug(bpm):
    #setup
    bpm = 90
    expected = 90
    #invoke
    actual = heart_rate_game.plug(bpm)
    #analyze
    assert actual == expected