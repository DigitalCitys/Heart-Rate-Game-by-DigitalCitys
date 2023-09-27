# Testing module for Heart Rate Game

import heart_rate_game

def test_plug():
    #setup
    avg_bpm = 90
    bpm = 90
    expected = 90, 90
    #invoke
    actual = heart_rate_game.plug(avg_bpm, bpm)
    #analyze
    assert actual == expected